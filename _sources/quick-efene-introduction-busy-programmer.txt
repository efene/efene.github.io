.. quick-intro:

Efene Quick Introduction for the Busy/Lazy Programmer
=====================================================

This is a quick and concise introduction to the efene programming language
intended for someone who already programs in some programming language, it will
only cover syntax and data types so you can familiarize with the language in a
short read and maybe use it as a reference in the future.

Data Types
----------

Do you know `JSON <http://JSON.org/>`_?

Yes: great! you know almost all of the data types and their syntax

No: you should click on the above link then...

Let's see a quick example:

.. code:: ruby

    {
        "object?": "it's the thing wrapping this fields, we call it a map",
        "string": "I'm a string!",
        "integer": 42,
        "float": 3.14,
        "bool": true,
        "null": nil,
        "empty list": [],
        "list": [1, 2, true, false, ["nested!"]],
        "other object please": {"ok": true}
    }

But wait, there is more!

.. code:: ruby

    {
        what: '<- that's an atom, like clojure :atom and a ruby :symbol',
        'wait!': 'yes, strings in single quotes are a different type of strings';
        'how?': (binary, strings, are, just, another, type, of, strings),
        'and that?': 'those are tuples, like python tuples'
        'tuple examples': {
            empty: (),
            one_item: (1,),
            two: (1, 2),
            three: (1, 2, 3)
        }
    }

lets recap, efene data types are:

* boolean: true, false
* null: nil

Those two aren't actual types, just atoms, but by convention they are used
as booleans and null, the undefined atom is also used in many places.

* atoms: symbolic identifiers that evaluate to themselves. They provide very fast equality tests.
* integers: 1, 2, 42
* floats: 1.2, 3.0, 42.7
* strings: "with double quotes"
* binary strings: 'with single quotes'

* tuples: ((,), (1,), (1, 2, 3))
* lists:  [[],  [1],  [1, 2, 3]]
* maps: {empty: {}, one: {one: 1}, more: {one: 1, two: 2}}

Strings vs Binary Strings, the Short Version
--------------------------------------------

Strings are actually lists or integers representing unicode code points.

Binary strings are the binary type with the content being a string encoded in
utf8.

Expressions
-----------

Yes, expressions, not statements, all the expressions covered below return a
value, so you can use expressions on the right side of an assignment to assign
(match) the returned value to a variable (well, they don't vary that much).

Simple Conditions with Guards
-----------------------------

A guard is similar to an if in other languages but with some restrictions, since
they are used in many places in the language (for example function clauses),
the conditions should evaluate fast and be free of side effects, this means
the subset of functions you can call in a guard condition is very restricted,
you shouldn't use guards as if, use the match expression instead.

But let's see some examples:

.. code:: ruby

    R1 = when true: ok end
    IsInteger = when is_integer(R1): true else: false end
    IsInteger1 = when is_integer(R1):
        true
    else:
        false
    end

    IsNumber = when is_integer(A): true
        else is_float(A): true
        else: false
    end

As you can see guards are defined starting with the when keyword followed by
a condition, followed by a colon and then one or more expressions separated
by a new line.

Also you can see that we can assign the result of the when expression to a
variable (variables start with an uppercase letter), the result of a guard
expression is the result of the last expression of the guard clause that
evaluated to true.

More Complex Conditions with Match
----------------------------------

As we said, guards are pretty restrictive in what you can put in the condition,
that's why normally we use the match expression or pattern matching, pattern
matching is at the core of efene and is used extensively, let's see some examples:

.. code:: ruby

    Result = match some_function(A, B):
        case 42: the_answer
        else: something_else
    end

A simple match expression starts with the match keyword followed by an
expression that will be evaluated and matched against all case clauses from
top to bottom, when one matches the body of that case clause will be evaluated
and the last evaluated expression of the body will be the returned value of
the match expression.

you can add an else clause at the end to act as a catch all (as in the when
expression)

another example:

.. code:: ruby

    B = 43
    Result = match some_function(true, 14):
        case 42: the_answer
        case 41: almost_there
        case B: missed_it
        case A when is_integer(A): (at_least_an_integer, A)
        case _: something_else
    end

This one is a little more complex, we match against a literal value in the
first two case clauses, but in the third we match against an bound variable,
that is a variable that is bound to a value already, this will match if the
result of evaluating some_function(true, 14) returns 43, since B is bound to
that value.

The fourth case clause matches against an unbound variable, that is a variable
that doesn't have a value yet, but then it has a guard expression that checks
that A is an integer, this case clause will only match if A is an integer, and
the A variable will be bound in the case clause body to the result of calling
some_function, so we can use it for example to return the value inside a tuple.

The last case clause is another way of writing the else clause from the first
example, in this case we match against the *special* variable **_**, this
variable in efene is used to signify that we are not interested in that value and
will match against anything, even if used more than once in the same scope.

Normal variables once they are matched they will only match against the same
value, if they are matched against something else they will throw a bad match error,
but the **_** variable will happily match against anything you throw at it, let's
see an example:

.. code:: ruby

    fn my_xor case V1, V2:

      R1 = match (V1, V2):
        case A, A: false
        case _, _: true
      end

      R2 = match V1, V2:
        case B, B: false
        case _, _: true
      end

      T = (V1, V2)

      R3 = match T:
        case C, C: false
        case _, _: true
      end

      R4 = match T:
        case D, D: false
        else: true
      end

      R5 = match T:
        case (E, E): false
        case _: true
      end

      (R1, R2, R3, R4, R5)
    end

Here we define a function (new stuff!) that has only one case clause that
receives two arguments (V1 and V2) and in the body it does the same thing 5
times in slightly different ways.

Notice that the first case clause in the 5 match expressions will match when V1
and V2 have the same value, since A, B, C, D and E are unbound when evaluating
the first argument of the case clause they are bound to the value passed in.
Since then they are bound for the rest of the current case clause evaluation,
this means that when matching V2 to A (and B, C etc.) since A is already bound
to V1, it will only match if V1 is equal to V2.

The second case clause in the first 3 match expressions could be replaced with
an else as shown in the fourth or with a simpler case that matches just one
**_** the difference between the first 3 and the last 2 is that the last two
would even match something that is not a two item tuple, but since here we are
in control of the expression we are matching against it won't make a difference.

You may already have noticed that if you write more than one item separated
by coma in the match condition or in case clauses they are treated as tuples,
this is to have a more terse syntax with something that is really common when
writing efene.

When only one item is available in the match condition or in case clauses it's
evaluated as is, it could be a tuple itself or something else, this means you
can write tuples surrounded with parenthesis if you prefer but we recommend the
cleaner version without them. Notice that the last match has the tuple wrapped
in parenthesis (E, E).

Functions
---------

Yes, I wrote a function there without introducing it, I also said "only one case clause", let's
rewrite the previous code as a function:

.. code:: ruby

    fn first_example
      case 42: the_answer
      else: something_else
    end

    fn second_example
      case 42: the_answer
      case 41: almost_there
      case B: missed_it
      case A when is_integer(A): (at_least_an_integer, A)
      case _: something_else
    end

    fn my_xor case
      case A, A: false
      case _, _: true
    end

That should require little explanation, we define a top level function starting
with the fn keyword followed by an atom that will be the name of the function,
then one or more case clauses, in the case of functions all case clauses must
have the same number of arguments and that defines what we call the **arity**
of the function, in human words, the number of arguments it expects, we can
have two or more functions with the same name but different arity.

to call the functions:

.. code:: ruby

    first_example(42)
    second_example(43)

    my_xor(true, false)
    my_xor(true, true)

Notice also that we use guard clauses like in the match expression and that
the case clauses are exactly the same as match expressions, you should start
noticing this recurring pattern in the following sections.

Anonymous Functions
-------------------

The previous section covered top level (module level) functions, but what if
we want to create a temporary function inside a function?

.. code:: ruby

    fn build_functions case:
        FirstExample = fn
          case 42: the_answer
          else: something_else
        end

        SecondExample = fn
          case 42: the_answer
          case 41: almost_there
          case B: missed_it
          case A when is_integer(A): (at_least_an_integer, A)
          case _: something_else
        end

        MyXor = fn
          case A, A: false
          case _, _: true
        end

        (FirstExample, SecondExample, MyXor)
    end

Here we define a top level function called build_functions with arity 0 that
when called will return a 3 item tuple with 3 functions that are identical
to the ones defined in the previous section, the only difference is that
anonymous functions (as their name implies) don't carry a name after the fn
keyword, other than that they are the same as top level functions.

let's now use them

.. code:: ruby

    (Example1, Example2, Xor) = build_functions()

    Example1(42)
    Example2(43)

    Xor(true, false)
    Xor(true, true)

I think it doesn't require further explanations, after all this is the quick
introduction :)

Named Anonymous Functions (WAT)
-------------------------------

With a top level function you can call the function from one of the case
clauses to do recursion, but what happens if you want to do the same with an
anonymous function?

Well you do something like this:

.. code:: ruby

        Factorial = fn Fact
            case 0: 1
            case N: N * Fact(N - 1)
        end

The name Fact is only visible inside the function's case clauses and is only
used for recursion, you have to assign it to something to use it.

Holding a Reference to a Top Level Function
--------------------------------------------

We saw that we can assign an anonymous function to a variable, but what if
we want to do the same for a top level function or a function in another module?

We just write the fn keyword followed by the name of the function and
optionally the module if it's in another module followed by a colon and the
function's arity.

.. code:: ruby

        CR1 = fn a:0
        CR3 = fn a.b:2
        CR4 = fn a.B:3
        CR5 = fn A.b:4
        CR6 = fn A.B:5

Now you have a reference to the function, this is also useful to pass a top
level function to a higher order function.

Handling Exceptions
-------------------

Yes, efene supports exceptions and has the familiar try/catch/after expression
to handle them, let's jump straight to it:

.. code:: ruby

       R1 = try
         1/0
       after
         ok
       end

       R2 = try
         1/0
       catch
         case error, badarith: ok
       end

       R3 = try
         1/0
       catch
         case error, badarith: ok
       after
         ok
       end

       R4 = try
         1/0
       catch
         case throw, T1: T1
         case Throw: Throw
         case error, E1: E1
         case exit, X1: X1
         case A, C: C
         else: iselse
       end

As I said earlier and like all other expressions, try/catch/after expression
(from now on try expressions) return a value that you can match to something (if you want).

The expression starts with the try keyword followed by one or more expressions
in the try body separated by new lines, if the body doesn't throw an exception
the result of evaluating the last expression of the body will be returned.

If an exception is thrown and no catch section is available the after body will
be evaluated and the exception will be re-thrown.

If the catch section is available the thrown value will be matched against each
case clause from top to bottom, if a case clause matches the body will be
evaluated and the result of the last expression will be returned, if no case
clause matches the exception will the re-thrown. If an after section is defined
it will be executed before re-throwing.

case clauses in the catch section have one restriction, they can only have one
or two arguments, if they have one argument the value will be matched against
the exception's details and the type of the exception is assumed to be **throw**.

If the case clause has two arguments the first will be matched against the exception type
which can be one of **throw**, **error** or **exit** and the second against the
exception's details.

You can also have an else clause as the last one which will match against
anything.

Notice that case clauses in the catch section are equal to case clauses
everywhere else except for the number of arguments restriction, this mean they
can have guard expressions.

Receiving Messages
------------------

Efene thanks to it's runtime provided by the Erlang VM supports message passing,
to send messages we use the "bang" operator **!** where the left side is where
we want to send the message (a process id or an atom) and the right side is the message we want to send, let's see some examples:

.. code:: ruby

    some_registered_process ! 42
    Pid ! ok

On the other side we want to receive that message, we do it with the receive expression:

.. code:: ruby

    receive
      case 42: the_answer
      case 41: almost_there
      case B: missed_it
      case A when is_integer(A): (at_least_an_integer, A)
      case _: something_else
    end

That set of case clauses should be familiar to you, this expression will block
waiting for a message sent to the current process and when one is received it
will match it against the case clauses, if one matches the result of evaluating
its body will be returned (yes, it's an expression, and yes, case clauses work
like everywhere else).

But what happens if no message is sent? well the code above will block forever,
we can solve this by adding an after section:

.. code:: ruby

    receive
      case A, A: false
      case _, _: true
    after 1000:
        timeout
    end

The after section starts with the after keyword and is followed by an expression
that should evaluate to a number of milliseconds (or the atom infinity), after
that time (or never if infinity is passed) the after body will be run and its
result returned as the result of the receive expression.

If the timeout value is 0 the after body will be run inmediatly if no message
is in the process' inbox.

For/List Comprehension Expression
---------------------------------

For with one generator:

.. code:: ruby

   for X in lists.seq(1, 10):
     X + 1
   end

For with one generator and one filter:

.. code:: ruby

   for X in lists.seq(1, 10); when X % 2 is 0:
     X + 1
   end

For with two generators:

.. code:: ruby

   for X in lists.seq(1, 10); Y in lists.seq(10, 20):
     (X, Y)
   end

The for expression in efene works similarly to a list comprehension in other
languages, you can have one or more generator expressions that assign each
value of the sequence to a variable and execute the body with the variable
bound to that value. You can also have zero or more guards that if evaluated to
false will skip the body for that combination of variables, think of them as
filters.

The body of the for expression is evaluated and the last expression on each
iteration is accumulated in a list and after the for finishes the list is
returned.

Begin/End Expression
--------------------

You need to put more than one expression in a place where only one expression
is expected? then begin/end is for you:

.. code:: ruby

    Value = begin
        io.format("returning 42")
        42
    end

The result of evaluating the last expression will be returned as the result
of the begin/end expression

Tagged Values and Expressions
-----------------------------

Values and expressions in efene can be tagged, what each tag means is unknown
to efene the language, tags are handled by compiler plugins to give them meaning,
let's explore the "official" tags, which are the ones shipped with the standard
efene compiler (but you can run efene without them if you wish):

.. code:: ruby

    #atom "I'm an atom"
    #_ "I'm ignored, useful for comments, yes, we don't have comment syntax"

    #_ "The following line evaluated to the integer that represents the character 'A'"
    #c "A"

    ^_ begin
        "this begin/end expression is ignored, useful to comment a whole expression"
        42
    end

    #_ "The following is a binary pattern"
    #b [{},
        {val: A},
        {size: 8},
        {type: float},
        {sign: unsigned},
        {endianness: big},
        {unit: 8},
        {val: B, size: 8, type: float, sign: signed, endianness: little, unit: 16}]

    #_ "Compile time information"
    CurrentLine = #i line
    CurrentModule = #i module

    #_ "Erlang macro expansion (yes we support erlang macros, defined in erlang modules :)"
    #m Author
    #m LINE
    #m PI

    #m AUTHOR(bob)
    #m Text(1 * 2 + 3)
    #m AddPlusOne(2, 3)

    #_ "Erlang record support defined using tagged values"
    P = #r.person {name: "bob", lastname: "sponge", age:29}
    P1 = #r.person P#{age:28}
    #r.person {age: Age} = P1
    Counter = #r.state.counter State

    #_ "Binary Comprehension as an extension too"
    ^b for A <- foo(10):
      A + 1
    end

Higher Order Functions
----------------------

Higher order functions are functions that take functions as parameter and
may return functions as result, common higher order functions are map, filter and reduce.

Passing functions around is so common in efene that we provide a nicer syntax
for it which also enables some really lightweight dsl construction:

.. code:: ruby

    #_ "lists.map:2 takes a function as first argument"
    lists.map(List) <<- case X:
      X + 1
    end

    #_ "mymap takes a function as last argument"
    mymap(List) <- case X:
      X + 1
    end



The <- operator inserts the anonymous function as the last argument in the
function (imagine that <- sends the value to the closest side).

The <<- operator inserts the anonymous function as the first argument in the
function (imagine that <<- sends the value to the other side).

Threading Values
----------------

efene is a lot about symmetry and consistency, this means if we have arrows
pointing in one way surely we should have arrows pointing in the opposite way
and doing something similar, right?

Well, we actually do:

.. code:: ruby

    IsOdd     = fn case X: X % 2 is 0 end
    Increment = fn case X: X + 1 end
    MyMap     = fn case List, Fun: lists.map(Fun, List) end

    lists.seq(1, 10) ->>
        lists.filter(IsOdd) ->
        MyMap(Increment)

(I define MyMap to reverse the order of the arguments of lists.map so I can
use -> in the example)

The ->> operator inserts the value from the left as the last argument in the
function on the right (imagine that ->> sends the value to the other side)

The -> operator inserts the value from the left as the first argument in the
function on the right (imagine that -> sends the value to the closest side)

This allows you to "pipe" results from one operation to another one without
creating temporary variables.

Operators
---------

I won't introduce operators in detail, you have the language reference for that
and you told me you are a programmer and you are busy (or lazy), so, without
further ado:

Boolean Operations
..................

==== ======================= ================= ===============================
Op   Description             Erlang Equivalent JS Equivalent
==== ======================= ================= ===============================
or   Short Circuit Or        orelse            ||
and  Short Circuit And       andalso           &&
xor  Xor                     xor               No Equivalent
orr  Non Short Circuit Or    or                No Equivalent
andd Non Short Circuit And   and               No Equivalent
==== ======================= ================= ===============================

**orr** and **andd** are only available for compatibility with erlang and
shouldn't be used.

Comparison Operations
......................

==== ========================== ================= ============================
Op   Description                Erlang Equivalent JS Equivalent
==== ========================== ================= ============================
==   equal to                   ==                == (Not so much coercion)
!=   not equal to               /=                != (Not so much coercion)
<    less than                  <                 <
<=   less than or equal to      =<                <=
>    greater than               >                 >
>=   greater than or equal to   >=                >=
is   exactly equal to           =:=               ===
isnt exactly not equal to       =/=               !==
==== ========================== ================= ============================

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

==== ========================== ================= ============================
Op   Description                Erlang Equivalent JS Equivalent
==== ========================== ================= ============================
++   list concatenation         ++                Array.prototype.concat
--   list subtraction           --                No Equivalent
==== ========================== ================= ============================

The list concatenation operator ++ appends its second argument to its first and returns the resulting list.

The list subtraction operator -- produces a list which is a copy of the first argument, subjected to the following procedure: for each element in the second argument, the first occurrence of this element (if any) is removed.

.. warning::

    The complexity of A -- B is proportional to length(A) * length(B), meaning
    that it will be very slow if both A and B are long lists.


Arithmetic Operations
.....................

==== ========================== ================= ============================
Op   Description                Erlang Equivalent JS Equivalent
==== ========================== ================= ============================
\+   addition                   \+                \+
\-   subtraction                \-                \-
\*   multiplication             \*                \*
/    division                   /                 /
%    remainder                  rem               %
//   integer division           div               No Equivalent
==== ========================== ================= ============================

Binary Operations
.................

==== ========================== ================= ============================
Op   Description                Erlang Equivalent JS Equivalent
==== ========================== ================= ============================
\|   binary or                  bor               \|
&    binary and                 band              &
^    binary xor                 bxor              ^
<<   shift left                 bsl               <<
>>   shift right                bsr               >>
==== ========================== ================= ============================

Unary Operations
................

==== ========================== ================= ============================
Op   Description                Erlang Equivalent JS Equivalent
==== ========================== ================= ============================
\-   integer negative           \-                \-
not  boolean not                not               !
~    binary not                 bnot              ~
==== ========================== ================= ============================

Where to Go from Here
---------------------

This is a quick introduction of a lot of topics, if you want to learn more you
should check the following resources:

* :ref:`language-reference`
* :ref:`introduction`
* :ref:`quick-start`
