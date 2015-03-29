Language Tradeoffs
==================

Efene syntax is designed to be regular and avoid introducing inconsistencies,
but at the same time it tries to make it easy to write common code, trying to
balance this introduces some inconsistencies or tradeoffs that are documented
here.

Record Pattern Matching vs Map Pattern Matching
-----------------------------------------------

Record pattern matching::

    #r.person {name: Name} = P1

Map pattern matching::

    {name = Name} = P1


Function Call vs Function Declaration
-------------------------------------

In Erlang a function call has the same syntax as a function declaration, in
efene it isn't

Chaining = and ! Operations
---------------------------

Efene doesn't allow chaining = and ! ops in the same expression.

Refactoring Match to a Function
--------------------------------

For convenience in a match expression elements separated with commas match like
a tuple, if you refactor it to be a funcion and you still want to match a tuple
you have to wrap it in parenthesis.

One Item Case in Match is a Special Case
----------------------------------------

Given the design described above a case with one item would match a one item
tuple instead of one value, since this isn't normally the expected behaviour a
one item case will be special cased to match a value and not a one item tuple,
it you want to match a one item tuple you have to write it explicity.

Not Necessarily Tradeoffs
-------------------------

Zero Items Case Matches Empty Tuple
...................................

Not necessarily a tradeoff since it's not something you will write frequently.
