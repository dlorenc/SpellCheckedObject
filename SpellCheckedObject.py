import difflib
from functools import partial
import warnings


class SpellCheckedObject(object):
    def __handler__(self, attr, *args, **kwargs):
        return attr.__call__(*args, **kwargs)

    def __getattr__(self, attr):
        possible_attrs = self.__class__.__dict__.keys()
        closest_attrs = difflib.get_close_matches(attr, possible_attrs, 1)
        if closest_attrs:
            closest_attr_name = closest_attrs[0]
            warnings.warn("You spelled %s wrong.  You probably wanted %s" % (attr, closest_attr_name))
            closest_attr = getattr(self, closest_attr_name)
            if hasattr(closest_attr, '__call__'):
                return partial(self.__handler__, closest_attr)
            return closest_attr
        raise AttributeError
