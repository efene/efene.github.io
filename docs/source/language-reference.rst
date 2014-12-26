Language Reference
==================

Boolean
-------

`Boolean Data Type in Wikipedia <https://en.wikipedia.org/wiki/Boolean_data_type>`_

This is the simplest data type, it can take two values:

* true
* false

Efene has another data type that allows far more flexibility to signal "states"
in your program called atoms, they are covered bellow.

Numbers
-------

Integers
........

`Integer Data Type in Wikipedia <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>`_

This data type represents an integer number, it has only one syntax, the one
you are used to, the following are examples of integers:

* 0
* 1
* 42
* 9002

Efene doesn't have notation for hexadecimal, binary or other bases, they can
be added using tagged data which is covered below.

Floats
......

`Float Data Type in Wikipedia <https://en.wikipedia.org/wiki/Floating_point>`_

This data type represents a decimal number, it has only one syntax, the one
you are used to, the following are examples of floats: 

* 0.0
* 1.2
* 42.3
* 9002.2009

Efene doesn't have notation for scientific notation, they may be added in the
future, for now it can be added using tagged data which is covered below.

Strings
-------

`String Data Type in Wikipedia <https://en.wikipedia.org/wiki/String_%28computer_science%29>`_

There are two ways of representing text (strings) in erlang they have different
pros and cons, we won't cover them here.

List Strings
............

A List String is simply a list of characters represented as numbers, it's
actually not a data type on itself "hello" is shorthand for the list [104,101,108,108,111].

List Strings are enclosed in double quotes ("), examples of List Strings:

* ""
* "a"
* "hi there"
* "this \"is\" also a string"

Binary Strings
..............

A Binary String is a binary representation of text, Binary Strings are enclosed
in single quotes ('), examples of Binary Strings:

* ''
* 'a'
* 'hi there'
* 'this \'is\' also a string'

.. note::

    The Erlang atom syntax with single quotes is supported in efene with tagged
    data, see below.

Lists
-----

`List Data Type in Wikipedia <https://en.wikipedia.org/wiki/List_%28abstract_data_type%29>`_

A List is a variable sequence of elements, it's represented by a comma separated sequence
of other data types (including nested lists) enclosed in opening and closing
square brackets ([ and  ]), examples of lists:

* []
* [1]
* [1, 2]
* [[[]]]

the last element of a list can have a trailing comma:

* [1,]
* [1, 2,]

Maps
----

`Map Data Type in Wikipedia <https://en.wikipedia.org/wiki/Associative_array>`_

A Map is a sequence of elements associating keys to values, it's represented by a comma separated sequence of association pairs enclosed in opening and closing
curly brackets ({ and }), examples ofmaps 

* {}
* {one: 1}
* {one: 1, 1: one}

the last element of a map can have a trailing comma:

* {one: 1,}
* {one: 1, 1: one,}

Tuples
------

A Tuple is a fixed sequence of elements, it's represented by a comma separated sequence
of other data types (including nested tuples) enclosed in opening and closing
square brackets ([ and  ]), examples of tuples: 

* {}
* {1}
* {1, 2}
* {{{}}}

the last element of a list can have a trailing comma:

* {1,}
* {1, 2,}

Atoms
-----

An atom is a literal, a constant with name, examples of atoms:

* ok
* error
* hi_there

Process Id (Pid)
----------------

A process identifier, pid, identifies a process.

spawn/1,2,3,4, spawn_link/1,2,3,4 and spawn_opt/4,
which are used to create processes, return values of this type.

Reference
---------

A reference is a term which is unique in an Erlang runtime system, created by
calling make_ref/0.

Function
--------

Tagged Data
-----------

Ta

Records
-------

Binary
------

