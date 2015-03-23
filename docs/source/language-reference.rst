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

Cons Lists
----------

`Cons List Type in Wikipedia <https://en.wikipedia.org/wiki/Cons>`_

You can create a list like [1,2,3] with an alternative syntax:

* [1 :: [2 :: [3]]]

It's useful to extract the head and keep the tail:

* [H :: T] = [1,2,3]

Now *H* is 1, and *T* is [2, 3]

You can do the reverse and create a new list by "consing" a new head to an existing list:

* L = [1 :: [2, 3]]

Now *L* is [1,2,3]


Maps
----

`Map Data Type in Wikipedia <https://en.wikipedia.org/wiki/Associative_array>`_

A Map is a sequence of elements associating keys to values, it's represented by a comma separated sequence of association pairs enclosed in opening and closing
curly brackets ({ and }), examples ofmaps 

* {}
* {one: 1}
* {one: 1, 1: one}

The last element of a map can have a trailing comma:

* {one: 1,}
* {one: 1, 1: one,}

You can extract fields from a map by using pattern match replacing : for =

* M = {one: 1, two: 2}
* {one = One, two = Two} = M

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

If you want to have spaces or symbols in an atom you can wrap it in "`":

* \`hello world!\`

or use a tagged string:

* #atom "hello world!"

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

    #r.person {age: Age} = P1

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

Hardcode Language Reference
---------------------------

Global Attributes
.................

Export
::::::

::

    @export(hello/0, plus/2)

Export Type
:::::::::::

::

    @export_type(tint/0, c2/1)

Literal Type
::::::::::::

::

    @type(tint) -> 42
    @type(tatom) -> asd
    @type(tbool) -> false
    @type(lempty) -> []

List Type
:::::::::

::

    @type(lone) -> [42]
    @type(l3) -> [tatom()]

Range Type
::::::::::

::

    @type(trange) -> range(1, 10)

Union Type
::::::::::

::

    @type(tres) -> (ok, integer()) or (error, term()) or (stop, normal)

Binary Type
:::::::::::

::

    @type(bsempty) -> binary(0, 0)
    @type(bsone) -> binary(4, 0)
    @type(bsonemul) -> binary(0, 5)
    @type(bstwo) -> binary(4, 5)


Parameterized Type
::::::::::::::::::

::

    @type(p1(X)) -> (ok, X, X)
    @type(p2(X, Y)) -> (ok, X, Y)

Function Type
:::::::::::::

::

    @type(f1) -> fun()
    @type(f2) -> fun(any, integer())
    @type(f3) -> fun([boolean(), term()], integer())
    @type(f4) -> fun([], integer())

Opaque Type and Record Type
:::::::::::::::::::::::::::

::

    @opaque(tperson) -> #r person

Record Definition
:::::::::::::::::

::

    @record(foo) -> (a, b = 12, c = true, d = 12)

Record Definition with Types
::::::::::::::::::::::::::::

::

    @record(person) -> (first = "" is string(), last is list(char()), age is integer())

Function with else case
:::::::::::::::::::::::

::

    fn plus
        case A, B:
            A + B
        else:
            42
    end

String Likes
::::::::::::

::

    A = 'I\'m a binary string'
    B = "I'm a regular string"
    C = #atom "I'm an atom"
    C1 = `I am an atom too`
    D = #c "C"

Function References
:::::::::::::::::::

::

    CR1 = fn a:0
    CR3 = fn a.b:2
    CR4 = fn a.B:3
    CR5 = fn A.b:4
    CR6 = fn A.B:5

Anonymous Functions
:::::::::::::::::::

::

    F = fn case 1: one end

    F1 = fn
        case 1: one
        case _: other
    end

    F2 = fn
        case 1: one
        else: other
    end

    Plus = fn
        case A, B: A + B
        else: 42
    end


Named Anonymous Functions
:::::::::::::::::::::::::

::

    F3 = fn Fact
        case 0: 1
        case N: N * Fact(N - 1)
    end

Record Syntax
:::::::::::::

::

    State = #r.state {counter: 1, last_modification: now()}
    State1 = #r.state State#{counter: 2}
    Counter = #r.state.counter State
    CounterIdx = #r.state counter
    #r.state {counter: Counter} = State

Compile Time Information
::::::::::::::::::::::::

::

    Line = #i line
    Module = #i module

Tuples
::::::

::

    Empty = ()
    One = (1,)
    One1 = (4 - 1,)
    OneExpr = (1)
    OneExpr1 = (4 - 1)
    Two = (1, 2)

List
::::

::

    Cons = [a :: b]
    L = [2,3,4]
    L0 = [2,3,4,]
    L1 = [1 :: L]
    L10 = [1, :: L]
    L2 = [0, 1 :: L]
    L20 = [0, 1, :: L]
    L3 = [0, 1, 2 :: L]
    L30 = [0, 1, 2, :: L]

Maps
::::

::

    {}
    A = {a: b}
    A0 = {a: b,}
    {atom: atom, 'bstr': 'hi', "str": "hi", 42: 24, 1.2: 2.1, true: false}
    {atom = atom, 'bstr' = 'hi', "str" = "hi", 42 = 24, 1.2 = 2.1, true = false} = A

Function Calls
::::::::::::::

::

    L = lists
    S = seq
    R = lists.seq(1, 10)
    R = L.S(1, 10)
    R = lists.S(1, 10)
    R = L.seq(1, 10)
    One = identity(1)

    I = fn identity:1
    One = I(1)

    L1 = fn lists.seq:2
    L2 = fn lists.S:2
    L3 = fn L.seq:2
    L4 = fn L.S:2
    R = L1(1, 10)
    R = L2(1, 10)
    R = L3(1, 10)
    R = L4(1, 10)

    MapR = fn case List, Fun:
      lists.map(Fun, List)
    end

    lists.map(R) <<- case X:
      X + 1
    end

    MapR(R) <- case X:
      X + 1
    end

Tagged Expressions
::::::::::::::::::

::

    ^_ "this is kind of a comment?"
    ^_ match A
        case 1: one
        case 2: two
        else: dontknow
    end

    A = ^b [{}, {val: A}, {size: 8}, {type: float}, {sign: unsigned}, {endianness: big},
        {unit: 8},
        {val: B, size: 8, type: float, sign: signed, endianness: little, unit: 16}]

    for A in range(10); A < 10; A <- foo(10): A + 1 end
    ^b for A in range(10); A < 10; A <- foo(10): A + 1 end

When
::::

::

    when true, false; true, false; true; false:
        1
    else true, false; true, false; true:
        2
    else true, false; true, false:
        3
    else true, false:
        4
    else true:
        5
    else:
        6
    end

    when true: ok
    else: error
    end

For (List Comprehensions)
:::::::::::::::::::::::::

::

   for X in lists.seq(1, 10):
     X + 1
   end

   for X in lists.seq(1, 10); X % 2 is 0:
     X + 1
   end

   for X in lists.seq(1, 10); Y in lists.seq(10, 20):
     (X, Y)
   end

Match
:::::

::

   match Error
        case throw, T1: T1
        case error, E1: E1
        case exit, X1: X1
        case A, C: C
        else: iselse
   end

Sequence Types
::::::::::::::

::

    A = (a, 1, true)
    D = {a: 1, b: 2}
    ED = {}
    ET = ()
    {a := A, b := B} = D

Receive
:::::::

::

   receive
        case throw, T1: T1
        case error, E1: E1
        case exit, X1: X1
        case A, C: C
        else: iselse
   end

   receive
        case throw, T1: T1
        case error, E1: E1
        case exit, X1: X1
        case A, C: C
        else: iselse
   after 1000:
        ok
   end

Expressions
:::::::::::

::

    A = 1 * 2 + 3
    B = 1 * (2 + 3)
    C = 3 - 5 - 7
    C = (3 - 5) - 7
    D = 3 - (5 - 7)
    E = 1 < 2 and 2 >= 3 or 4 + 5

Function Attributes
:::::::::::::::::::

::

    fn hello
        @public
        @http.get("/foo/:num") -> json
        @doc("some hello world function")
        @accept -> json
        @produces(json, xml, edn)
        @spec(integer(), ok) -> (ok, term()) or notfound

        case A, B: A + B
    end

String Escaping
:::::::::::::::

::

    A = "a \"hi\" \\\" \\' 'there'"
    B = 'a "hi" \\" \\\' \'there\''

Chars
:::::

::

    A = #c "A"
    Hello = [#c "h", #c "e", #c "l", #c "l", #c "o"]

Try Catch
:::::::::

::

   try
     1/0
   after
     ok
   end

   try
     1/0
   catch
       case error, badarith: ok
   end

   try
     1/0
   catch
       case error, badarith: ok
   after
     ok
   end

   try
     1/0
   catch
        case throw, T1: T1
        case Throw: Throw
        case error, E1: E1
        case exit, X1: X1
        case A, C: C
        else: iselse
   end

