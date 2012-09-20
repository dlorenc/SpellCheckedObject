Spell Checking for Python
==================

For when spelling is hard


Usage
-----

>>> from SpellCheckedObject import SpellCheckedObject
>>> class CantSpell(SpellCheckedObject):
        def test(self, x, y):
            return x + y
        @property
        def prop(self):
            return 7

>>> c = CantSpell()
>>> c.test(3, 4)
7
>>> c.testt(3, 4)
7
