.. _language-reference:

Language Reference
==================

.. contents::
   :local:
   :depth: 2

Values
------

Boolean
.......

`Boolean Data Type in Wikipedia <https://en.wikipedia.org/wiki/Boolean_data_type>`_

This is the simplest data type, it can take two values:

* true
* false

Efene has another data type that allows far more flexibility to signal "states"
in your program called atoms, they are covered bellow.

Numbers
.......

Integers
::::::::

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
::::::

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
.......

`String Data Type in Wikipedia <https://en.wikipedia.org/wiki/String_%28computer_science%29>`_

There are two ways of representing text (strings) in erlang they have different
pros and cons, we won't cover them here.

List Strings
::::::::::::

A List String is simply a list of characters represented as numbers, it's
actually not a data type on itself "hello" is shorthand for the list [104,101,108,108,111].

List Strings are enclosed in double quotes ("), examples of List Strings:

* ""
* "a"
* "hi there"
* "this \"is\" also a string"

Binary Strings
::::::::::::::

A Binary String is a binary representation of text, Binary Strings are enclosed
in single quotes ('), examples of Binary Strings:

* ''
* 'a'
* 'hi there'
* 'this \'is\' also a string'

.. note::

    The Erlang atom syntax with single quotes is supported in efene with tagged
    values and backticks, see below.

Chars
:::::

A character is a number representing a character in a string::

    A = #c "A"
    Hello = [#c "h", #c "e", #c "l", #c "l", #c "o"]

Lists
.....

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
..........

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
....

`Map Data Type in Wikipedia <https://en.wikipedia.org/wiki/Associative_array>`_

A Map is a sequence of elements associating keys to values, it's represented by a comma separated sequence of association pairs enclosed in opening and closing
curly brackets ({ and }), examples of maps:

* {}
* {one: 1}
* {one: 1, 1: one}

The last element of a map can have a trailing comma:

* {one: 1,}
* {one: 1, 1: one,}

You can extract fields from a map by using pattern match replacing : for =

* M = {one: 1, two: 2}
* {one = One, two = Two} = M

You can update an existing map:

* M1 = M#{three: 3}

Tuples
......

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
.....

An atom is a literal, a constant with name, examples of atoms:

* ok
* error
* hi_there

If you want to have spaces or symbols in an atom you can wrap it in "`":

* \`hello world!\`

or use a tagged string:

* #atom "hello world!"

Variables
.........

If a variable is bound to a value, the return value is this value. Unbound
variables are only allowed in patterns.

Variables start with an uppercase letter or underscore (_) and may contain
alphanumeric characters and underscores. Examples::

    X
    Name1
    PhoneNumber
    Phone_number
    _
    _Height

Variables are bound to values using pattern matching. Erlang uses single
assignment, a variable can only be bound once.

The anonymous variable is denoted by underscore (_) and can be used when a
variable is required but its value can be ignored. Example::

    [H :: _] = [1,2,3]

Variables starting with underscore (_), for example _Height, are normal
variables, not anonymous. They are however ignored by the compiler in the sense
that they will not generate any warnings for unused variables.

Note that since variables starting with an underscore are not anonymous, this will match::

    (_,_) = (1,2)

But this will fail::

    (_N,_N) = (1,2)

Process Id (Pid)
................

A process identifier, pid, identifies a process.

spawn/1,2,3,4, spawn_link/1,2,3,4 and spawn_opt/4,
which are used to create processes, return values of this type.

Reference
.........

A reference is a term which is unique in an Erlang runtime system, created by
calling make_ref/0.

Function
........

Anonymouse Functions
::::::::::::::::::::

Functions can be created and assigned to variables inside other functions, the
syntax is::

    fn [case <parameter>*: <body>]+ [else: <body>] end

Simples function::

    One = fn one case: 1 end

Receiving arguments::

    Identity = fn case Val: Val end

    AddTwo = fn case A, B: A + V end

Multiple case clauses::

    Division = fn
        case A, 0:
            (error, division_by_zero)
        case A, B:
            A / B
    end

Cases with else::

    MyXor = fn
        case true, false: true
        case false, true: true
        else: false
    end

Named Functions
:::::::::::::::

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
:::::::::::::::::::

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

Function Calls
::::::::::::::

There are many ways to call a function, it depends if the function is local,
from another module and if we know the name and/or the module in advance or
we have a reference to it in a variable.

The simples way to call a local function (or an automatically imported function) is
just giving the name and passing the parameters.

Local call::

    One = identity(1)

Call to a function in another module::

    R = lists.seq(1, 10)

Dynamic local call::

    I = fn identity:1
    One = I(1)

Dynamic call to a function in another module::

    L = lists
    S = seq
    R = L.S(1, 10)
    R = lists.S(1, 10)
    R = L.seq(1, 10)

    L1 = fn lists.seq:2
    L2 = fn lists.S:2
    L3 = fn L.seq:2
    L4 = fn L.S:2

    R = L1(1, 10)
    R = L2(1, 10)
    R = L3(1, 10)
    R = L4(1, 10)

Threading function calls:

::

    IsOdd = fn case X:
      X % 2 is 0
    end

    Increment = fn case X:
      X + 1
    end

    MyMap = fn case List, Fun:
      lists.map(Fun, List)
    end

    lists.seq(1, 10) ->>
        lists.filter(IsOdd) ->
        MyMap(Increment)

(I define MyMap to reverse the order of the arguments of lists.map so I can
use -> in the example)

the ->> operator inserts the value from the left as the last argument in the
function on the right (imagine that ->> sends the value to the other side)

the -> operator inserts the value from the left as the first argument in the
function on the right (imagine that -> sends the value to the closest side)

Higher order function calls::

    MapR = fn case List, Fun:
      lists.map(Fun, List)
    end

    R = lists.seq(1, 10)

    lists.map(R) <<- case X:
      X + 1
    end

    MapR(R) <- case X:
      X + 1
    end

The <- operator inserts the anonymous function as the last argument in the
function (imagine that <- sends the value to the closest side).

The <<- operator inserts the anonymous function as the first argument in the
function (imagine that <<- sends the value to the other side).

Tagged Values
.............

Expressions and values can be tagged in efene, this is inspired from
`the edn format <https://github.com/edn-format/edn>`_.

This allows to transform a value or expression at compile time to some other
value or expression by tagging it.

a tagged value is comprised of the # sign followed by a path, that is a
sequence of atoms or variables joined with dots, examples of tagged values::

    #atom "I'm an atom"
    #c "A"

The first case transforms the string to an atom at compile time, it has the same
effect as the single quotes in erlang.

The second case transforms a string of length 1 into a character type, it has
the same effect as the dolar sign in erlang.

a tagged expression works the same as a tagged value but applies to expressions,
the syntax is the same except that the ^ symbol is used instead of #::

    ^_ begin "this is ignored" end

It just "ignores" the expression or value that follows.

Efene adds support for some erlang syntax via tagged values and expressions
as you can see above.

In the future this functionality will be provided to compiler extensions that
can convert at compile time values or expressions into extra functionality,
imagine string internationalization, logging, profiling, stdlib type
constructors using values etc.

Records
.......

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

To get the value of a field::

    Counter = #r.state.counter State

To get the tuple index of a field:

Binary
......

Binary is a data type to express erlang's bit syntax, where you can specify
the format of a binary, you can read more at `erlang's bit syntax docs <http://www.erlang.org/doc/reference_manual/expressions.html#bit_syntax>`_

In efene binaries are implemented using a tagged map that contains a sequence
of key/value pair for each field describing format of that field, here is an
example covering all the alternatives::

    #b {_: _,
        A: _,
        JustSize: 8,
        JustType: binary,
        E: {},
        _: {size: 8},
        _: {type: float},
        _: {sign: unsigned},
        _: {endianness: big},
        _: {unit: 8},
        B: {size: 8, type: float, sign: signed, endianness: little, unit: 16}}

You can use `_` on the key to ignore that field and on the value to provide
defaults, on the value you can also provide `{}` to specify defaults.

If the value is an int it's assumed to be the size property, if it's an atom
it's assumed to be the type attribute.

Here is an example pattern matching an IPv4 packet::

    #b {Version:4, IHL:4, TypeOfService:8, TotalLength:16,  Identification:16,
        FlagX:1, FlagD:1, FlagM:1,  FragmentOffset:13, TTL:8, Protocol:8,
        HeaderCheckSum:16, SourceAddress:32, DestinationAddress:32,
        Rest: binary} = Packet

On a field you can specify the variable to match to, the size, type, sign,
endianness and unit.

For a detailed explanation of what each of those values do please refer to
`erlang's bit syntax docs <http://www.erlang.org/doc/reference_manual/expressions.html#bit_syntax>`_.

Compile Time Information
........................

Using tagged values we can get some information at compile time.

Current line::

    Line = #i line

Current module name as an atom::

    Module = #i module

Current module name as a string::

    Module = #i module_string

Current function name::

    FnName = #i function_name

Current function arity::

    FnArity = #i function_arity

Operations
----------

Boolean Operations
..................

==== ======================= =================================================
Op   Description             Erlang Equivalent
==== ======================= =================================================
or   Short Circuit Or        orelse
and  Short Circuit And       andalso
xor  Xor                     xor
orr  Non Short Circuit Or    or
andd Non Short Circuit And   and
==== ======================= =================================================

Comparisson Operations
......................

==== ========================== ==============================================
Op   Description                Erlang Equivalent
==== ========================== ==============================================
==   equal to                   ==
!=   not equal to               /=
<    less than                  <
<=   less than or equal to      =<
>    greater than               >
>=   greater than or equal to   >=
is   exactly equal to           =:=
isnt exactly not equal to       =/=
==== ========================== ==============================================

The arguments may be of different data types. The following order is defined::

    number < atom < reference < fun < port < pid < tuple < list < bit string

Lists are compared element by element.

Tuples are ordered by size, two tuples with the same size are compared element by element.

When comparing an integer to a float, the term with the lesser precision will
be converted into the other term's type, unless the operator is one of *is* or
*isnt*.

A float is more precise than an integer until all significant figures of the
float are to the left of the decimal point.

This happens when the float is larger/smaller than +/-9007199254740992.0. The
conversion strategy is changed depending on the size of the float because
otherwise comparison of large floats and integers would lose their
transitivity.

Concat Operations
..................

==== ========================== ==============================================
Op   Description                Erlang Equivalent
==== ========================== ==============================================
++   list concatenation         ++
--   list substraction          --
==== ========================== ==============================================

The list concatenation operator ++ appends its second argument to its first and returns the resulting list.

The list subtraction operator -- produces a list which is a copy of the first argument, subjected to the following procedure: for each element in the second argument, the first occurrence of this element (if any) is removed.

.. warning::

    The complexity of A -- B is proportional to length(A) * length(B), meaning
    that it will be very slow if both A and B are long lists.


Aritmetic Operations
....................

==== ========================== ==============================================
Op   Description                Erlang Equivalent
==== ========================== ==============================================
\+   addition                   \+
\-   substraction               \-
\*   multiplication             \*
/    division                   /
%    remainder                  rem
//   integer division           div
==== ========================== ==============================================

Binary Operations
.................

==== ========================== ==============================================
Op   Description                Erlang Equivalent
==== ========================== ==============================================
\|   binary or                  bor
&    binary and                 band
^    binary xor                 bxor
<<   shift left                 bsl
>>   shift right                bsr
==== ========================== ==============================================

Unary Operations
................

==== ========================== ==============================================
Op   Description                Erlang Equivalent
==== ========================== ==============================================
\-   integer negative           \-
not  boolean not                not
~    binary not                 bnot
==== ========================== ==============================================

Expressions
-----------

When
....

Abstract Syntax
:::::::::::::::

Simple::

    when GuardSeq1:
        Body1
    else:
        ElseBody
    end

Complete::

    when GuardSeq1:
        Body1
    else GuardSeq2:
        Body2
    ...
    else GuardSeqN:
        BodyN
    else:
        ElseBody
    end

Examples
::::::::

::

    when true:
        io.format("guard evaluated to true")
    else:
        io.format("no guard evaluated to true")
    end

::

    when A < 10:
        io.format("A < 10")
    else A < 20:
        io.format("A < 20 and >= 10")
    else A < 30:
        io.format("A < 30 and >= 20")
    else:
        io.format("A > 30")
    end

Description
:::::::::::

When expression is similar to if/else if/else in other languages but with some
extra limitations.

This limitations come from the fact that when expressions
are identical to function guard expressions.

The set of valid guard expressions (sometimes called guard tests) is a subset
of the set of valid Erlang expressions. The reason for restricting the set of
valid expressions is that evaluation of a guard expression must be guaranteed
to be free of side effects. Valid guard expressions are:

* the atom true,
* other constants (terms and bound variables), all regarded as false,
* term comparisons,
* arithmetic expressions,
* boolean expressions
* short-circuit expressions (and/or)
* calls to the BIFs

    + is_atom/1
    + is_binary/1
    + is_bitstring/1
    + is_boolean/1
    + is_float/1
    + is_function/1
    + is_function/2
    + is_integer/1
    + is_list/1
    + is_map/1
    + is_number/1
    + is_pid/1
    + is_port/1
    + is_record/2
    + is_record/3
    + is_reference/1
    + is_tuple/1

If an arithmetic expression, a boolean expression, a short-circuit expression,
or a call to a guard BIF fails (because of invalid arguments), the entire guard
fails. If the guard was part of a guard sequence, the next guard in the
sequence (that is, the guard following the next semicolon) will be evaluated.

A guard sequence is a sequence of guards, separated by semicolon (;).
The guard sequence is true if at least one of the guards is true.
(The remaining guards, if any, will not be evaluated.)::

    Guard1;...;GuardK

A guard is a sequence of guard expressions, separated by comma (,).
The guard is true if all guard expressions evaluate to true::

    GuardExpr1,...,GuardExprN

example::

    when Cond1, Cond2; Cond3:
        1
    else Cond4; Cond5, Cond6, Cond7:
        2
    else:
        3
    end

Match
.....

Abstract Syntax
:::::::::::::::

::

    match Expr:
        case Pattern1 [when GuardSeq1]:
            Body1
        ...
        [case PatternN [when GuardSeqN]:
            BodyN]
        [else:
            BodyElse]
    end

Examples
::::::::

Simple::

    match Result:
        case ok, Value:
            io.format("everything ok ~p~n", [Value])
            do_something(Value)
        case error, Reason:
            io.format("error: ~p~n", [Reason])
            fail(Reason)
    end

When and Else::

    match Result:
        case ok, Value when is_integer(Value), Value < 10:
            io.format("everything ok, value is < 10: ~p~n", [Value])
            do_something(Value)
        case ok, Value when is_atom(Value):
            io.format("everything ok, value is atom~p~n", [Value])
            do_something_atom(Value)
        case error, Reason:
            io.format("error: ~p~n", [Reason])
            fail(Reason)
        else:
            io.format("Value doesn't match any case")
    end

Description
:::::::::::

The expression Expr is evaluated and the patterns Pattern are sequentially
matched against the result. If a match succeeds and the optional guard sequence
GuardSeq is true, the corresponding Body is evaluated.

The return value of Body is the return value of the case expression.

If else is present and no Pattern matched BodyElse will be executed.

If there is no matching pattern with a true guard sequence, a case_clause
run-time error will occur.

For
...

Abstract Syntax
:::::::::::::::

::

    for (<generator>;<filter>)+:
        <body>
    end

The for expression starts with the **for** reserved keywords followed with at
least one *generator* and zero or more *generators* or *filters* separated by
semicolons finished by a colon.

After the colon one or more expressions that will be evaluated as the body
of the for for each element in the generators that pass the filter expressions.

Note that for is an expression, this means it returns a list with each item
being the result of evaluating the last expression in the body. This means
that if you are not interested in the result of the for expression, for example
if you are only interested in side effects like printing sending messages or
logging, then you should take care to avoid having a big value being generated
as the last expression in the body, since this will be acumulated in a list
and returned when the for finishes.

A generator is an expression like::

    A in B

Where B should be evaluated to a sequence and each element of that sequence
will be assigned to A and be available in the for body.

A filter is an expresion like::

    when <condition>

where condition should be an expression that evaluates to true of false, if
a filter returns false then the body wont be generated for that value.

Examples
::::::::

For with one generator::

   for X in lists.seq(1, 10):
     X + 1
   end

For with one generator and one filter::

   for X in lists.seq(1, 10); when X % 2 is 0:
     X + 1
   end

For with two generators::

   for X in lists.seq(1, 10); Y in lists.seq(10, 20):
     (X, Y)
   end

Try/Catch/After
...............

Abstract Syntax
:::::::::::::::

::

    try
        <body>
    [catch <case>+ [<else>]]
    [after <body>]
    end

A try expression is an expression used to handle one or more expressions that
may raise an exception, the expression starts with the **try** keyword followed
by one or more expressions as the try body.

Optionally a catch section can be included starting with the **catch** keyword
followed by one or more case clauses and optionally an else clause used when
we want to catch any type of exception but we don't care about the value being
thrown.

Optionally an *after** section can be included starting with the **after**
keyword and followed by one or more expressions in the after body which will be
executed no mather if an exception is being thrown or not, this is useful to
run code that should run to do cleanup in both cases like closing a file
handle.

The case clauses in the try expression are restricted to one or two arguments.

In case of having one argument the type of exception is assumed to be throw,
in case of having two arguments the first must be the type of exception that
the case clause will handle, the exception type must be one of:

* throw
* error
* exit
* an expression that evaluates to one of the above
* an unbound variable which will be bound with the exception type

the second argument can be used to pattern match or an unbound variable can
be used to get the details of the exception.

Examples
::::::::

No catch::

       try
         1/0
       after
         ok
       end

Catch type and reason::

       try
         1/0
       catch
           case error, badarith: ok
       end

Catch and after::

       try
         1/0
       catch
           case error, badarith: ok
       after
         ok
       end

All possible catchs::

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

Receive/After
.............

Abstract Syntax
:::::::::::::::

::

    receive
        case Pattern1 [when GuardSeq1]:
            Body1
        ...
        [case PatternN [when GuardSeqN]:
            BodyN]
        [else:
            BodyElse]
    after ExprT:
        BodyAfter
    end

Examples
::::::::

::

       receive
            case throw, T1: T1
            case error, E1: E1
            case exit, X1: X1
            case A, C: C
            else: iselse
       after 1000:
            ok
       end

Description
:::::::::::

Receives messages sent to the process.

The patterns Pattern are sequentially matched against the first message in time
order in the mailbox, then the second, and so on.

If a match succeeds and the optional guard sequence GuardSeq is true, the
corresponding Body is evaluated.

The matching message is consumed, that is removed from the mailbox, while any
other messages in the mailbox remain unchanged.

The return value of Body is the return value of the receive expression.

receive never fails. Execution is suspended, possibly indefinitely, until a
message arrives that does match one of the patterns and with a true guard
sequence.

It is possible to augment the receive expression with a timeout, ExprT should
evaluate to an integer. The highest allowed value is 16#ffffffff, that is, the
value must fit in 32 bits. receive..after works exactly as receive, except that
if no matching message has arrived within ExprT milliseconds, then BodyT is
evaluated instead and its return value becomes the return value of the
receive..after expression.

There are two special cases for the timeout value ExprT:

infinity
    The process should wait indefinitely for a matching message, this is the same as not using a timeout. Can be useful for timeout values that are calculated at run-time.
0
    If there is no matching message in the mailbox, the timeout will occur immediately.

Begin
.....

Abstract Syntax
:::::::::::::::

::

    begin
        Expr1
        ...
        ExprN
    end

Examples
::::::::

::

    Value = begin
        io.format("returning 42")
        42
    end

Description
:::::::::::

Block expressions provide a way to group a sequence of expressions, similar to
a clause body. The return value is the value of the last expression ExprN.

Macros
------

Macros are an extension to support using Erlang Macros defined in Erlang modules
from efene, to use Erlang Macros from a module you need first to include that
module in your efene module and then use them.

Macro Constants
...............

Macro Constants are macros that are a definition of a name that expands to
an expression, it can be used to name constants or to expand an expression in
multiple places, to expand a macro constant you have to write the name of
the macro constant tagged with the #m tag::

    #m Author
    #m LINE
    #m PI

Macro Functions
...............

Macro Functions are macros that receive arguments and use them to expand
its definition using those arguments, to expand a macro call you have to write
the macro as a function call tagged with the #m tag::

    #m AUTHOR(bob)
    #m Text(1 * 2 + 3)
    #m AddPlusOne(2, 3)

Module Level Expressions
------------------------

Top Level Function
..................

Abstract Syntax
:::::::::::::::

::

    fn <name> [attribues] [cases] end

A top level function is defining by starting with the reserved keyword **fn**
followed by the name as an atom.

Them zero or more attributes and then one or more case clauses finished with
the **end** keyword.

Examples
::::::::

Simples function::

    fn one case: 1 end

Simple with attributes::

    fn one @public case: 1 end

    fn two @public
        @doc("returns the number two")
        case:
            2
    end

Receiving arguments::

    fn identity case Val: Val end

    fn add_two case A, B: A + V end

Multiple case clauses::

    fn division
        case A, 0:
            (error, division_by_zero)
        case A, B:
            A / B
    end

Cases with else::

    fn my_xor_
        case true, false: true
        case false, true: true
        else: false
    end

Well Known Function Attributes
::::::::::::::::::::::::::::::

@public
#######

Exports the function to be used from other modules.

@spec
#####

Defines the types of function arguments and return type for current function.

Attributes
..........

Well Known Attributes
:::::::::::::::::::::

Export
######

::

    @export(hello/0, plus/2)

Has the same behavior as adding the @public attribute to a function, exports
the function to be used from other modules.

Export Type
###########

::

    @export_type(tint/0, c2/1)

Exports the types to be used from other modules.

Record Definition
#################

::

    @record(foo) -> (a, b = 12, c = true, d = 12)

Defined a record by providing a name and a tuple with field names as atoms
and optionally a default value in case a value is not providing on construction.

For more information see `Erlang's Record Manual Page <http://www.erlang.org/doc/reference_manual/records.html>`_

Record Definition with Types
############################

::

    @record(person) -> (first = "" is string(), last is list(char()), age is integer())

Record fields can contain a type definition to help tools like `Dialyzer <http://www.erlang.org/doc/man/dialyzer.html>`_

Type Attributes
:::::::::::::::

Literal Type
############

::

    @type(tint) -> 42
    @type(tatom) -> asd
    @type(tbool) -> false
    @type(lempty) -> []

List Type
#########

::

    @type(lone) -> [42]
    @type(l3) -> [tatom()]

Range Type
##########

::

    @type(trange) -> range(1, 10)

Union Type
##########

::

    @type(tres) -> (ok, integer()) or (error, term()) or (stop, normal)

Binary Type
###########

::

    @type(bsempty) -> binary(0, 0)
    @type(bsone) -> binary(4, 0)
    @type(bsonemul) -> binary(0, 5)
    @type(bstwo) -> binary(4, 5)


Parameterized Type
##################

::

    @type(p1(X)) -> (ok, X, X)
    @type(p2(X, Y)) -> (ok, X, Y)

Function Type
#############

::

    @type(f1) -> fun()
    @type(f2) -> fun(any, integer())
    @type(f3) -> fun([boolean(), term()], integer())
    @type(f4) -> fun([], integer())

Opaque Type and Record Type
###########################

::

    @opaque(tperson) -> #r person

Version Attribute (vsn)
:::::::::::::::::::::::

::

    @vsn("1.2.0")
    @vsn((1, 2, 0))

Module version. The parameter is any literal term and can be retrieved using
`beam_lib.version:1 <http://www.erlang.org/doc/man/beam_lib.html#version-1>`_.

If this attribute is not specified, the version defaults to the MD5 checksum of
the module.

On Load Attribute (on_load)
:::::::::::::::::::::::::::

::

    @on_load(fname/0)

This attribute names a function that is to be run automatically when a module
is loaded. For more information, see `Running a Function When a Module is
Loaded <http://www.erlang.org/doc/reference_manual/code_loading.html#on_load>`_.

Import Attribute (import)
:::::::::::::::::::::::::

::

    @import(erlang, [phash2/1])

Imported functions. Can be called the same way as local functions, that is,
without any module prefix.

Module, an atom, specifies which module to import functions from. Functions is
a list similar as for export.

Include Attribute (include)
:::::::::::::::::::::::::::

::

    @include("path/to/file.hrl")

Include an erlang file in the current module, code is included in the current
module and macros are available for use, see
`macro use example on how to use them <https://github.com/efene/efene/blob/master/examples/use_macros.fn>`_
here is the included file `ms.hrl <https://github.com/efene/efene/blob/master/examples/ms.hrl>`_

