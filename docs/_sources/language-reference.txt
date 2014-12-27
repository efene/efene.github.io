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
parenthesis ( and ), examples of tuples:

* ()
* (1,)
* (1, 2)
* (((),),)

the last element of a list can have a trailing comma, it's obligatory in one
item tuples to distinguish from an expression in parenthesis:

* (1,)
* (1, 2,)

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

Anonymouse Functions
....................

Functions can be created and assigned to variables inside other functions, the
syntax is::

    fn [case [parameters]: body]+ end

for example, the simples case with one function clause::

        F = fn case 1: one end

we can use pattern matching to match different cases::

        F1 = fn
            case 1: one
            case _: other
        end

in the case where the last clause is a "catch all" clause we can use else instead::

        F2 = fn
            case 1: one
            else: other
        end

Named Functions
...............

Named Functions exist to refer to a function inside of it to do recursion as you
would do with a toplevel function.

The syntax is the same as an anonymous function but with a variable as it's name,
for example::

        F3 = fn Fact
            case 0: 1
            case N: N * Fact(N - 1)
        end

Notice that the resulting function is stored in F3 and you must use that name
to call it, the "named" part is only to refer to itself, if a function doesn't
refer to itself then you don't need a named function.

You can see more details and examples in this article: http://joearms.github.io/2014/02/01/big-changes-to-erlang.html

Function References
...................

If we want to pass a reference to a function as a parameter or set it to a
variable we can use the function reference syntax.

It's composed of the keyword **fn**, the function name, including module if
needed and it's arity, that is, the number of parameters it receives.

Examples::

        CR1 = fn a:0
        CR3 = fn a.b:2
        CR4 = fn a.B:3
        CR5 = fn A.b:4
        CR6 = fn A.B:5

Notice you can't make a function reference to a function stored on a variable like this::

        CR2 = fn A:1

since it's already a function reference on itself, this will result in an error.

Tagged Expressions
------------------

Expressions and data types can be tagged in efene, this is insipired from
`the edn format <https://github.com/edn-format/edn>`_.

This allows to transform a value or expression at compile time to some other
value or expression by tagging it.

a tag is comprised of the # sign followed by a path, that is a sequence of
atoms or variables joined with dots, examples of tagged values::

    #atom "I'm an atom"
    #c "A"
    #_ "this is ignored"

The first case transforms the string to an atom at compile time, it has the same
effect as the single quotes in erlang.

The second case transforms a string of length 1 into a character type, it has
the same effect as the dolar sign in erlang.

The last one is quite useful, it just "ignores" the expression or value that
follows, actually it doesn't ignore it, it just replaces it by a special atom,
as long as you don't assign the result or return it the value of the atom
doesn't matter.

Efene adds support for some erlang syntax via tagged values and expressions
as you can see above.

In the future this functionality will be provided to compiler extensions that
can convert at compile time values or expressions into extra functionality,
imagine string internationalization, logging, profiling, stdlib type
constructors using values etc.

Records
-------

A record is a compile time data structure that erlang transforms into tuples at
run time with the name of the record in it, it's kind of a named tuple where
at run time field names are translated into tuple indexes.

To declare a record you have to add a record declaration at the top level of
your modules, for example::

    @record(person) -> (name, lastname, sex=female, age)

The person part is the name of the record, the items after the arrow in
parenthesis are the record fields, you can provide default values for fields.

To instantiate a record::

        P = #r.person {name: "bob", lastname: "sponge", age:29}

To update a record::

        P1 = #r.person P#{age:28}

To pattern match against a record::

        (#r.person {age: Age}) = P1

Since tags can be applied to expressions and the match expression is used after
the first tag we need to wrap the tag and map in parenthesis so it applies
only to the map and not to the whole expression.

Binary
------

Binary is a data type to express erlang's bit syntax, where you can specify
the format of a binary, you can read more at `erlang's bit syntax docs <http://www.erlang.org/doc/reference_manual/expressions.html#bit_syntax>`_

In efene binaries are implemented using a tagged list that contains a map
for each field describing the format of that field, here is an example covering
all the alternatives::

    #b [{},
        {val: A},
        {size: 8},
        {type: float},
        {sign: unsigned},
        {endianness: big},
        {unit: 8},
        {val: B, size: 8, type: float, sign: signed, endianness: little, unit: 16}]

On a field you can specify the variable to match to, the size, type, sign, endianness and unit.

For a detailes explanation of what each of those values do please refer to
`erlang's bit syntax docs <http://www.erlang.org/doc/reference_manual/expressions.html#bit_syntax>`_.
