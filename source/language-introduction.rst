Efene Introduction
==================

This section describes the language through simple working examples, for a
complete reference see :ref:`language-reference`.

We will introduce the data types as we need them, but for a quick introduction
let's say that if you know what JSON is, which data types it support and how to
read it then you know 80% of efene's data types and syntax.

A Simple Function
-----------------

Let's start defining the simplest function ever, a function
that receives no arguments and returns a number:

.. code-block:: javascript

    fn return_one
        case: 1
    end

That's the syntax to define a top level (or module level) function in efene,
it starts with the fn keyword, then comes the name of the function as an atom
(called symbols or keywords in other languages like lisp, scheme, clojure and ruby).

Then comes the case keyword, this keyword is there because in efene (as in erlang)
a function can have more than one case depending on the value of its arguments
and some conditions on those arguments.

In this case we have only one case, and since the function doesn't take any
argument it's followed by a colon.

After the colon and until the end keyword we have the body of the function,
in this case since it's a simple expression (the number 1) we can write it
in the same line as the case and the colon, but normally you would write it on
the next line indented.

Notice that we didn't have to write return to return the number 1, in efene
the last expression of a block is the returned value, in efene (almost) everything
is an expression, which means it returns a value.

So that's a verbose way to describe how to define such a simple function, don't
worry, as we go along we will asume undestanding on things explained before.

Variables on Function Arguments
-------------------------------

Not let's write a function that takes some arguments and does something,
let's make a function that adds two numbers:

.. code-block:: javascript

    fn add_two
        case A, B: A + B
    end

It's pretty similar to the function before but this time the case has two
arguments before the colon, you may have noticed that they are uppercase, in
efene (as in erlang) variables are uppercase or start with an underscore, words
that start with lowercase are atoms, like the function name **add_two**.

Atoms are objects whose value is its name, you can find them in other languages
like cloure, lisp, scheme and ruby sometimes with sligthly different syntax.

Now back to our, function, it takes to arguments, A and B and returns A + B,
no big deal right?

Like before we don't need to write return, it's implicit that the last
expression of a block is the returned value.

A Function with Two Cases
-------------------------

I mentioned before that functions can have more than one case, and that the case
that is executed depends on the value of the arguments and optionally on conditions
of those arguments.

Let's try our first function with two cases then:

.. code-block:: javascript

    fn bool_to_text
        case true: 'true'
        case false: 'false'
        else: 'not a boolean'
    end

Again we have our function cases inside "fn <name of function> ... end" as before
but now we have two cases, here the function takes one argument, which must be
a boolean and returns the string represenation for that boolean, if the value
is not a boolean it will return the string 'not a boolean'.

There are two things to notice here, first in the argument we can write values
instead of just variable names as in most programming languages, that's called
pattern matching, each case is a "clause" that will only match and execute its
body **if** the values match the patterns.

the last clause is an else clause, which we can write to match any value for the
arguments but where we don't care about those values, it's kind of a catch all,
clause. We use it to return when the argument is not a boolean.

Here is an alternative way of writting that function:

.. code-block:: javascript

    fn bool_to_text
        case true: 'true'
        case false: 'false'
        case _: 'not a boolean'
    end

here instead of else we are writting a case clause that uses the special
variable **_** which in efene is used to express that we want to ignore that
value.

We use the **_** variable to be explicit that we don't care about the value and
to avoid a compiler warning about a variable being declared and not being used.


Same Variable in multiple Function Arguments
--------------------------------------------

We just saw pattern matching and binding variables on the function argument
list, but what happens if we write the same variable name in more than one
argument in the argument list?

well, the same as it will happen in any other place, the first time efene sees
a variable it is unbound, this means that if we try to match against it, it will
try to make it match by making it equal to the value being matched, so now it's
bound to that value.

The second time it sees the variable, since now it's bound, the process of matching
both values will mean it will check if they are equal.

This allows for a really nice trick which is to check if two arguments have the
same value, let's try it creating a function that returns true if both
parameters are equal:

.. code-block:: javascript

    fn two_are_the_same
        case A, A: true
        case _, _: false
    end

Notice both function arguments have the same name **A**, so that case clause
will only match if both arguments have the same value, then it will evaluate
the case body and return true.

the next case uses the special variable **_** that means "I don't care about
the value of this thing" and it's used to match anything and return false for
all the other cases.

As before we can use the else clause instead of matching with **__**, notice
that efene is smart enough to match all the arguments in the function, this
means the else is "expanded" to "case _, _:" so you don't have to.

.. code-block:: javascript

    fn two_are_the_same_1
        case A, A: true
        else: false
    end

Still, all the function case clauses that are not an else must have the same
number of arguments or you will get a compiler error.

There's still a third way to write this function which may surprise you, let's
see it first and later discus it:

.. code-block:: javascript

    fn two_are_the_same_2
        case _A, _A: true
        else: false
    end

The arguments on the first case start with underscore but still they seem
to be used to match the same value.

This is so because in efene (and erlang) the only "special" variable that can
be used multiple times and can contain multiple values is **_** any other
variable, even if they start with an underscore are normal variables and will
be bound the first time and matched thereafter.

So, why would I start a variable with an underscore if they work the same as
normal variables?

There's a reason, it's for clarity and to avoid compiler warnings, the clarity
comes from stating that you don't care about the variable content but you still
want to give it a name so the reader (normally you in the future) can know what
that ignored variable is.

The second reason is that even if variables that start with an underscore are
normal variables the compiler treats them a little different, if a variable
starts with an underscore the compiler understands that you aren't going to use
it so it won't raise a warning if the variable isn't used.

But there's still another way of writing this function:

.. code-block:: javascript

    fn two_are_the_same_3
        case A, B when A == B: true
        else: false
    end

In this example the first case receives two arguments with different names but
after the arguments we have the "when A == B" which is called a "guard" and is
an expression that we can add to a case clause to do additional checks on the
arguments of a case clause.

In this case we are chacking that A is equal to B, but the guard can be much
more complex.

One more thing..., those guards look a lot like if statements on other languages,
can we use them standalone too?

well, yes we can, let's rewrite the previous function one more time:

.. code-block:: javascript

    fn two_are_the_same_3
        case A, B:
            when A == B:
                true
            else:
                false
            end
    end

well, that looks really similar, isn't it? you can use guards as kind of **if
statements** but there's a catch, since guards in functions must execute quick
(you don't want to slow down your function calls evaluating slow guards) and
they also must be free of side effects (you don't want two successive calls to
a function to be different because some guard is doing something weird) the
erlang VM only allows a restricted set of operations to be used in a guard,
this means you can't call your own functions in a guard, only a subset of
erlang functions are allowed in guards, you can see a list of allowed operations
in this `Stack Overflow Answer <http://stackoverflow.com/a/11177231>`_.

If you want to use something more similar to an if statement then use a match
expression and match against true and false (or against true and else), future
versions of efene may introduce if expressions, but not before 1.0.

Putting it All Together
-----------------------

Let's put all the things we learned about function definitions together in a
simple example.

Let's write a function that divices two numbers:

.. code-block:: javascript

    fn divide_two_unsafe
        case A, B: A / B
    end

From the name (or from experience) you may have noticed that this function
has a little problem, what happens if B is 0? well, in the erlang virtual machine
this will raise an exception.

Let's rewrite it to avoid raising an exception:

.. code-block:: javascript

    fn divide_two
        case _A, 0: (error, division_by_zero)
        case A, B: (ok, A / B)
    end

Here we have to cases, the first ignores the first parameter (by naming it with
an undescore prefix) and matches the second parameter with 0.

If this case matches then we return a tuple, which is a fixed sequence of values
(you may know them if you come from python), where the first item is the atom error
and the second item is an atom describing the error type.

You will see this type of return values in efene/erlang code, it's normally
called "tagged values", where the returned value is a tuple with the first item
specifying the type of return and the rest (normally just one extra item)
containing the result for that type.

If the first case doesn't match (in efene case clauses are evaluated from top
to bottom, this means order of case clauses matters), then the second case
will match and it will return a two item tuple where the first item is the atom
ok and the second item is the result of the division.

Calling Functions (in other Modules)
------------------------------------

Now that we know almost all there is to know about defining functions let's
call some, in this case functions in other modules.

Since efene follows erlang in almost every aspect, we also follow the erlang
way of structuring code.

In efene functions are defined inside modules, and modules are only one level
deep, this means you can't have a module inside a module.

a module in efene is defined by writing top level functions inside a file
with the .fn extension.

There's a module that you will use frequently and it's the `io module <http://erlang.org/doc/man/io.html>`_

the most useful function it has is the `io.format function <http://erlang.org/doc/man/io.html#format-1>`_

Let's create a simple function that wraps the io.format function:

.. code-block:: javascript

    fn print
       case Text:
            io.format(Text ++ "~n")
    end

The print function takes one argument, called Text, and prints it by calling
io.format(Text ++ "~n").

There are some new things to describe here.

First, function calls are done similarly to all algol-like languages::

    function_name()
    function_name(argument1)
    function_name(argument1, argument2)

And so on.

Second, calling a function in another module is done also in a similar way
than algol-like languages, by specifying the module and the function joined by
a dot::

    module_name.function_name()
    module_name.function_name(argument1)
    module_name.function_name(argument1, argument2)

Then there is the "~n" thing, first **~n** is a control sequence that efene
translates to a new line, in other languages you may use \\n instead.

Second, only if you are really obseervant is that in this case the string uses
double quotes and in an example before we used single quotes.

In some other languages like python and javascript this doesn't make a
difference since both single quoted and double quoted strings are treated the
same, but in efene they are different, I will leave the details for the
:ref:`language-reference` but I will say that single quote strings are binary
strings and double quote strings are list strings.

For now I will just say that most functions in the standard library expect list
strings and will fail if binary strings are used.

With this clarification I can now talk about the **++** operator, which is the
string concatenation operator, it works with lists and the result is the result
of concatenating two lists.

But those aren't lists, those are list strings you may say.

Well that's the list part in list string, list strings are simply a list of
numbers each representing a character, this means it's really easy to operate
on list strings with operations and functions that expect lists, the bad part
is that it's almost imposible to distinguis a list string from a list of
numbers, that's why sometimes we use binary strings.

It took a lot of text to describe what::

            io.format(Text ++ "~n")

does, but now that we clarified everything we can sum it up with:

it calls the format function in the io module passing the result of concatenating
the string contained in the Text variable with the literal string "~n" which
contains a control sequence which io.format replaces for a new line.

A Function with the same Name but Different Number of Arguments
---------------------------------------------------------------

In efene to refer to a function you need to specify it's name (if the module
name is not specified it's asumed that the function is in the current module)
but also the number of arguments it received (normally called "arity" of the
function).

This is needed since two functions in efene can have the same name but different
number of arguments and they will be different functions.

To try this let's define a new function with the same name as the one we defined
above but with a different *arity*:

.. code-block:: javascript

    fn print
        case Format, Args:
            io.format(Format ++ "~n", Args)
    end

Here we define the function print with arity 2, the first argument is called
Format and it contains a string optionally with control sequences that
io.format will replace for it's meaning. The second argument is called Args and
contains the values needed for the control secuences contained in the Format
string.

So, what are this magical control sequences we talk about other than "~n"?

For a full list of them you can see `the documentation of io.format:2 <http://erlang.org/doc/man/io.html#format-2>`_.

.. note::

    Notice how I included the arity of the function in there? it's a common
    practice in efene/erlang to refer to functions including its arity, you can see
    it on the left section on the linked documentation.

The one you should learn right now other than ~n is ~p, which means "replace
this control sequence for the value provided in the Args list in this position".

For example, calling

.. code-block:: javascript

    print("first argument is ~p second argument is ~p", [1, false])

will print::

    first argument is 1 second argument is false

Many Ways to Call a Function
----------------------------

Let's now see all the ways you can call a function in efene other than the common
case where you write the name and arguments and optionally the module name.

Say you want to call a function dinamically, that is, some part is defined in
a variable, how would you do that? let's see:

.. code-block:: javascript

    fn dynamic_call
        @doc("this function shows all the ways you can call a function")
        case:
            Mod = lists
            Fun = seq
            From = 1
            To = 4

            R = lists.seq(From, To)
            R = lists.Fun(From, To)
            R = Mod.seq(From, To)
            R = Mod.Fun(From, To)

            F1 = fn lists.seq:2
            F2 = fn lists.Fun:2
            F3 = fn Mod.seq:2
            F4 = fn Mod.Fun:2

            R = F1(From, To)
            R = F2(From, To)
            R = F3(From, To)
            R = F4(From, To)

            Fn = fn case: lists.seq(From, To) end

            R = Fn()

            R = apply(lists, seq, [From, To])
            R = apply(lists, Fun, [From, To])
            R = apply(Mod, seq, [From, To])
            R = apply(Mod, Fun, [From, To])

            print("all calls returned the same result")
    end

First you may have noticed the @doc thing after the function name and before
the case clause, this is a function annotation, efene allows you to attach
metadata to functions for many purposes like documentation, visibility outside
the module, types and any other use you may think of, in this case we attach
the docs for the function.

the function dynamic_call receives no arguments and calls the function `lists.seq:2 <http://www.erlang.org/doc/man/lists.html#seq-2>`_ in any way it can.

first the usual way:

.. code-block:: javascript

            R = lists.seq(From, To)

then using the Fun variable to provide the function name:

.. code-block:: javascript

            R = lists.Fun(From, To)

then using the Mod variable to provide the module name

.. code-block:: javascript

            R = Mod.seq(From, To)

then using both Mod and Fun

.. code-block:: javascript

            R = Mod.Fun(From, To)

Notice that all function calls **match** the result against the same variable
(R) this is because all functions are the same function and hence return the
same result, we are using the same variable to match and make sure all function
calls return the same value.

If some call returned a different value efene would raise a bad match exception.

Now instead of calling the function let's build a function reference, this is
we hold a reference to the function in a variable which we can pass around.

Again there are many ways to get a function reference, in all of them we need
to specify the module (optionally), the function name and the arity:

.. code-block:: javascript

            F1 = fn lists.seq:2
            F2 = fn lists.Fun:2
            F3 = fn Mod.seq:2
            F4 = fn Mod.Fun:2

Like before we can use variables which hold the name of the module, function
or both, now we can call the function with our function references:

.. code-block:: javascript

            R = F1(From, To)
            R = F2(From, To)
            R = F3(From, To)
            R = F4(From, To)

We can also *wrap* the function in an anonymous function and assign that
anonymous function to a variable, then call it:

.. code-block:: javascript

            Fn = fn case: lists.seq(From, To) end
            R = Fn()

If we had the arguments to the function in a list we can also call the function
dynamically using `erlang.apply:3 <http://www.erlang.org/doc/man/erlang.html#apply-3>`_

.. code-block:: javascript

            R = apply(lists, seq, [From, To])
            R = apply(lists, Fun, [From, To])
            R = apply(Mod, seq, [From, To])
            R = apply(Mod, Fun, [From, To])

That's it, all the ways there is to call a function!

Some more Pattern Matching
--------------------------

If now we want to print the result of calling divide_two we can do::

    print("result is: ~p", [divide_two(4, 2)])

Which will work but it will print the tuple directly, what we want to do
is to pattern match against the result and print a different message depending
if the result was successful or not.

For that we can define the following function:

.. code-block:: javascript

    fn print_div_result
        case (ok, Result):
            print("result is: ~p", [Result])
        case (error, Reason):
            print("error is: ~p", [Reason])
    end

print_div_result is a function that receives one argument and has two cases, in
the first it matches the tuple (ok, Result) and if it matches it will display
the message "the result is ~p", where ~p will be replaced by the content of
Result (which was bound during the argument pattern matching process since
Result was seen for the first time there).

The second case matches the tuple (error, Reason) and prints the message
"error is: ~p", where ~p is replaced by the content of Reason.

but what if we want to do this pattern matching in other places? do we have
to create a function to do the pattern match?

luckily the answer is no, there's a way to do pattern matching with multiple
cases inside the body of a function, let's see how by defining the same
functionality as above but with a function with a single case clause:

.. code-block:: javascript

    fn print_div_result_1
        case A, B:
             match divide_two(A, B):
                case (ok, Result):
                    print("result is: ~p", [Result])
                case (error, Reason):
                    print("error is: ~p", [Reason])
             end
    end

in this case the function print_div_result_1, receives two arguments, which
are the numbers we want to divide.

Then we use the *match expression* which calls divide_two(A, B) and matches
the result of that against two clauses.

You may notice that the content of the match expression is the same as
the content of the print_div_result function.

since pattern matching against tuples is so common in efene we provide you with
a convenient syntax that will "unroll" the tuple for you in the case clauses
without having to write the parenthesis yourself, let's see a version that uses
this feature:

.. code-block:: javascript

    fn print_div_result_2
        case A, B:
             match divide_two(A, B):
                case ok, Result:
                    print("result is: ~p", [Result])
                case error, Reason:
                    print("error is: ~p", [Reason])
             end
    end

As you can see parenthesis aren't needed, if the case clause in a match expression
has more than one argument then efene assumes you are matching on a tuple (since
the expression in match can be only one).

This introduces a small "special case" (we don't like special cases but we think
this one justifies its existence).

if you want to match a tuple of one item in a match expression you need to write
it explicitly, a small example to see why:

.. code-block:: javascript

    Value = (42,)

    match Value:
        case (42,): ok
        else: wat
    end

    Value1 = 42

    match Value1:
        case 42: ok
        else: wat
    end

This is because if we assumed that a case clause with one argument inside a match
expression was a one item tuple then we wouldn't be able to match things other
than tuples!

The good thing is that one item tuples isn't a common thing on efene/erlang
so you won't need to use this special case that often.

Looping
-------

If you need to apply operations to the items in the list efene provides the
for comprehension, which is similar to a list comprehension (or a map operation
if you come from more functional background).

The for comprehension will assign each item of the list to a variable and
execute the block of code with it:

.. code-block:: javascript

        for I in lists.seq(1, 10):
            print("I: ~p", [I])
        end

Notice that like almost everything in efene, the for comprehension is an expression, which
means that it returns a value that can be used or assigned to a variable.

What value does it return? the accumulation of results returned by all
iterations, in this case as in any other case, the results are the result of
the last expression in the for block.

Take this into account if you are looping over a big collection and the last
expression generates some big value, if you don't use it you will be generating
a huge list for nothing. If you want to avoid this, you can write a simple value
like **nil** as the last expression in the for body.

Like everything else in efene you can write guards to restrict the values generated
from the collection you are iteration over, for example, let's skip the odd values:

.. code-block:: javascript

        for I1 in lists.seq(1, 10); I1 % 2 == 0:
            print("I1: ~p", [I1])
        end

In a for comprehension you can have one or more generators and filters separated
by semicolons, here we can have more than one filter, let's skip odd values and
the number 8:

.. code-block:: javascript

        for I2 in lists.seq(1, 10); I2 % 2 == 0; I2 != 8:
            print("I2: ~p", [I2])
        end

We can also have more than one generator, here we will generate two values and
will print them only if thy are not equal:

.. code-block:: javascript

        for I3 in lists.seq(1, 4); J3 in lists.seq(1, 4); I3 != J3:
            print("I3, J3: ~p, ~p", [I3, J3])
        end

Catching Exceptions
-------------------

Before we declared the function divide_two_unsafe,if we called it with the
second argument being 0 an exception would occur, how do we handle that exception?

As is common in languages with exceptions there's a way to catch them, let's
see how it works in efene:

.. code-block:: javascript

        try
            divide_two_unsafe(8, 2)
        catch
            case T, E:
                 print("Error doing 8/2: ~p ~p", [T, E])
        end

        try
            divide_two_unsafe(8, 0)
        catch
            case T1, E1:
                 print("Error doing 8/0: ~p ~p", [T1, E1])
        after
            print("After division attempt")
        end

        try
            throw(hi)
        catch
            case E2:
                 print("Error was: ~p", [E2])
        end

First we call divide_two_unsafe(8, 2), which won't result in an exception, this
will return the result of the division, given that try/catch is an expression
too in efene.

Then we call divide_two_unsafe(8, 0), which will throw an exception, the body
of the try is followed by the catch keyword and after that by the already
known case clauses.

In this case we can match against either one or two values, if we match against
two values the first one will be the exception type (which can be throw, exit
or error). If we match against a single value the type of the error is assumed
to be throw.

We also can optionally provide an after section that will be executed both when
there's no exception and when there is, usually to do some cleanup like closing
a file or a socket.

In the third example we use the builting `erlang.throw:1 <http://www.erlang.org/doc/man/erlang.html#throw-1>`_
function to throw an exception of type throw and we inmediatly catch it and
print what the error was.

Arithmetic Operations
---------------------

If you come from a mainstream programming language the arithmetic operations
won't be a surprise for you, here is a simple operation to illustrate them:

.. code-block:: javascript

        print("add ops ~p", [1 + 2 - 3 + -4])
        print("mul ops ~p", [1 * 2 / 3 % 4])

For more details on operations described in this and the following sections see
the :ref:`language-reference`.

Comparison Operations
---------------------

Like before, comparison operations are really similar to mainstream programming
languages with a little difference:

.. code-block:: javascript

        R = 1 < 2 <= 3 == 4 is 5 != 6 isnt 7 >= 8 > 9
        print("comp ops ~p", [R])

the little difference is that instead of === and !== we use is and isnt.

Boolean Operations
------------------

Without further ado, here are the boolean operations:

.. code-block:: javascript

        R = true and false or true xor false andd not true orr not false
        print("bool ops ~p", [R])

A little note on some of them, you may have noticed two strange ones:

* andd
* orr

Those are available for erlang compatibility, andd is the non short cirquit
version of and and orr is the non short cirquit version of or, this means that
when used all the terms of the bool operation will be evaluated no matter if it
wasn't required.

Normally boolean operations in most programming languages are short cirquited so
you shouldn't use andd/orr unless you know what you are doing or you want some
erlang compatibility.

Binary Operations
-----------------

Here are the binary operations:

.. code-block:: javascript

        R = ~1 & 2 ^ 3 | 4
        print("bin ops ~p", [])

If you need them, then the syntax should be what you would expect, if you don't
know what they are for you can come back later when you need them or check the
:ref:`language-reference`

Data Types Overview
-------------------

Until here we have seen most of the data types available in efene, let's list
them here:

* Booleans: true, false
* Integers: 1, 2, 42 etc.
* Floats: 1.2, 3.1415 etc.
* Atoms: ok, error, print, hi, some_atom
* Strings

  + binary strings: 'hi there', ''
  + list strings:   "hi there", ""

* Lists: [], [1, 2, 3]
* Tuples: (), (1,), (1, 2)

Here we will cover two data types that are used for the same thing, olding key
-> value pairs, you may call them objects, maps, dicts, hash maps, associative
arrays depending on the language you use.

In efene there are two types that fulfil the same need, the new way, which is
more flexible, and the old way, which you will need to know to understand erlang
libraries and code.

The New Way: Maps
.................

Maps are really similar to what you are used in other languages, you can put
a key of any type and a value of any type and then get them by key, let's see
an example:

.. code-block:: javascript

    fn use_maps
        case:
            Account1 = {username: 'bob', password: 'secret', email: 'bob@gmail.com'}

            print("account1 ~p", [Account1])
            print("account1 username ~p email ~p", [maps.get(username, Account1),
                                                    maps.get(email, Account1)])

            {username = Username, email = Email} = Account1
            Account2 = Account1#{email: 'bob@nickelodeon.com'}

            print("account1 username ~p email ~p", [Username, Email])

            print("account2 ~p", [Account2])
            print("account2 username ~p email ~p", [maps.get(username, Account2),
                                                    maps.get(email, Account2)])

            Post = {title: "My Post"}
            print("post ~p", [Post])
    end

As I said near the beginning of this article the syntax is almost like JSON,
except that you can have any type as keys, not only strings.

To get a value from its key you can do it two ways, calling a function or
with pattern matching.

In the example above we use both ways, first we use the function `maps.get:2 <http://www.erlang.org/doc/man/maps.html#get-2>`_:

.. code-block:: javascript

            print("account1 username ~p email ~p", [maps.get(username, Account1),
                                                    maps.get(email, Account1)])

Then we do pattern matching on the map to extract the same fields:

.. code-block:: javascript

    {username = Username, email = Email} = Account1

Like we saw before the **=** sign in efene means "match" not "assign", this
means that efene will try to make both sides match, if there are unbound
variables it will bound them to the value on the right side so they match, if
they are bound then they must match otherwise a bad match exception will ocurr.

Notice that we use **=** on maps to signify match and **:** to signigy that we
are assigning them, this is to make it explicit when we are matching and when
we are assigning.

Finally to update a map by changing the content of one or more fields on a previous
map we can do:

.. code-block:: javascript

            Account2 = Account1#{email: 'bob@nickelodeon.com'}

On the right side we write the name of the variable that contains the map we
want to update, then the **#** sign and then the assignment of the fields we
want to add or update.

The Old Way: Records
--------------------

Maps are a relative new feature in the Erlang world, before them the only
way to have something similar to objects/dicts/maps from other languages were
records, let's see the same example as before but with record:

.. code-block:: javascript

    @record(account) -> (username, password, email)
    @record(post) -> (title is string(), content = "" is string(), author = "anonymous")

    fn use_records
        case:
            Account1 = #r.account {username: 'bob', password: 'secret'}

            print("account1 ~p", [Account1])
            print("account1 username ~p email ~p", [#r.account.username Account1,
                                                    #r.account.email Account1])

            #r.account {username: Username, email: Email} = Account1
            Account2 = #r.account Account1#{email: 'bob@nickelodeon.com'}

            print("account1 username ~p email ~p", [Username, Email])

            print("account2 ~p", [Account2])
            print("account2 username ~p email ~p", [#r.account.username Account2,
                                                    #r.account.email Account2])

            UsernameIndex = #r.account username
            print("username field index is ~p", [UsernameIndex])

            Post = #r.post {title: "My Post"}
            print("post ~p", [Post])
    end

First we need to declare the record, since it's a "compile time trick" that
the erlang compiler does, it needs to know the fields before hand to check
and transform records to its underlying representation.

.. code-block:: javascript

    @record(account) -> (username, password, email)

Now that we declared our record we can create an instance of it:

.. code-block:: javascript

            Account1 = #r.account {username: 'bob', password: 'secret'}

It looks really similar to the map example except that the map is "tagged" with
the record name.

To access the record fields we need a special syntax since record are
transformed at compile time and all information about them is lost at run time.

This means for example that you can't list the fields of a record at run time.

Here is how you access to a field in a record:

.. code-block:: javascript

            print("account1 username ~p email ~p", [#r.account.username Account1,
                                                    #r.account.email Account1])

Like before you "tag" a variable with the name of the record and the name of the field.

To extract more than one field at a time you can use pattern matching:

.. code-block:: javascript

            #r.account {username: Username, email: Email} = Account1

Notice that in this case we also use **:** on the left side, this is because
that's how erlang handles it (it doesn't make a distinction between assigning
and matching for records as it does for maps).

To update a record again is similar to how you would do it with a map, you
just "tag" the map update with the name of the record:

.. code-block:: javascript

            Account2 = #r.account Account1#{email: 'bob@nickelodeon.com'}

You may have noticed that the record declaration for the type **post** is a
little bit different.

This is because in record declarations you can provide defaults and also annotate the types of the fields:

.. code-block:: javascript

    @record(post) -> (title is string(), content = "" is string(), author = "anonymous")

We will see more about types later, now about the defaults, if you don't assign
a value when creating a record and the field doesn't have a default set its value
will be the atom **undefined**, if that's not what you want you can provide a
better default like we did in the **post** record declaration.

Even some more Pattern Matching
-------------------------------

We already saw how to pattern match on tuples, numbers, maps, records and whole
lists, let's see a little bit more about pattern matching on lists.

Lists in efene are of a particular type that allows for some useful operations
on them, if you come from lisp/scheme/clojure you will know what a cons list
is, if not here is a quick introduction.

Lists in efene are not like arrays in other languages which are a continuos
chunk of memory with pointer to its items (you may call them vectors depending
on the language).

In efene lists are what is normally known as cons lists, a list in efene
is constucted by a structure that has two items, the first is called the head
and the second is called the tail.

So, how do you build a list with that? well, you put the first item in the head
and the rest in the tail.

So, what goes on the tail then? another pair, with the second item in the head
and the rest in the tail

And so on recursively until the last item is an empty list to signal that theres
nothing else and that's the end of the list.

Let's see an example:

.. code-block:: javascript

        [One, Two, Three, Four] = [1, 2, 3, 4]
        print("items on the list are: ~p ~p ~p ~p", [One, Two, Three, Four])
        print("the list is ~p", [[1, 2, 3, 4]])
        print("the list is ~p", [[1 :: [2 :: [3 :: []]]]])

        [Head1 :: Tail1] = [1, 2, 3, 4]
        [Head2 :: Tail2] = [1]
        print("head ~p, tail ~p", [Head1, Tail1])
        print("head ~p, tail ~p", [Head2, Tail2])

First we pattern match against a list of four items:

.. code-block:: javascript

        [One, Two, Three, Four] = [1, 2, 3, 4]

That's simple and easy, but what happens if the list has 100 elements or we
don't know exaclty how many elements it has?

Here's where the list structure comes handy, we can match against the head and
the rest:

.. code-block:: javascript

        [Head1 :: Tail1] = [1, 2, 3, 4]
        print("head ~p, tail ~p", [Head1, Tail1])

This will print::

    head 1, tail [2,3,4]

We get the first valie in the Head1 variable and the rest of the list in the
Tail1 variable, notice that we use a special operator **::** to express that
we are not matching a list of two items like we would if we wrote [Head1, Tail1]
but that we want to extract the head and tail of the list.

But what if the list has just one item?, let's see:

.. code-block:: javascript

        [Head2 :: Tail2] = [1]
        print("head ~p, tail ~p", [Head2, Tail2])

This will print::

    head 1, tail []

As I said above, the "marker" for the end of the list is an empty list, we
could also match this list as [Head2] = [1] and it would have worked, but it
wouldn't match if the list has more than one item.

More about Tagging
------------------

In the section about records we saw that there's a way to tag values to tell
the compiler to treat them a differently, here we will see other uses of tagged
values:

.. code-block:: javascript

    fn tagged_values
        case:
            print("the code for character C is ~p", [#c "C"])

            Hello1 = "hello"
            Hello2 = [#c "h", #c "e", #c "l", #c "l", #c "o"]
            Hello3 = [#c "h" :: [#c "e" :: [#c "l" :: [#c "l" :: [#c "o" :: []]]]]]

            print("this three strings are equivalent ~p ~p ~p", [Hello1, Hello2, Hello3])

            print("this two atoms are equivalent ~p ~p", [#atom "an atom", `an atom`])
            print("this print is at line ~p in module ~p", [#i line, #i module])
    end

Let's see them line by line:

.. code-block:: javascript

            print("the code for character C is ~p", [#c "C"])

The #c tag is used to convert a string of one character into the integer
representing that character, as we said before lis strings in efene are simply
lists of characters, and we also said that lists are simple nested pairs,
let's reinforce that with the following example:

.. code-block:: javascript

            Hello1 = "hello"
            Hello2 = [#c "h", #c "e", #c "l", #c "l", #c "o"]
            Hello3 = [#c "h" :: [#c "e" :: [#c "l" :: [#c "l" :: [#c "o" :: []]]]]]

            print("this three strings are equivalent ~p ~p ~p", [Hello1, Hello2, Hello3])

As you can see the string syntax and the list syntax are just a convenience
to write nested pairs, the three are the same from the language perspective.

Let's continue with the following line:

.. code-block:: javascript

            print("this two atoms are equivalent ~p ~p", [#atom "an atom", `an atom`])

If you wanted to know how to express an atom with spaces or with weird symbols,
there you have the answer.

You can tag a string with the #atom tag and the compiler will convert it into an
atom or you can use backticks if you prefer amore "native" syntax.

And lastly, something that may be useful to help you print diagnostic messages
and find problems easier:

.. code-block:: javascript

            print("this print is at line ~p in module ~p", [#i line, #i module])

if you tag the atoms line and module with the #i tag they will be converted at
compile time to the current line as a number and to the module name as an atom
respectively.

Finally, the code above will print something like the following::

    the code for character C is 67
    this three strings are equivalent "hello" "hello" "hello"
    this two atoms are equivalent 'an atom' 'an atom'
    this print is at line 307 in module reference

of course the line and module will change depending on where they were in your
code.

Tagged values and tagged expressions are two of the ways erlang provides to
extend the language in the future withouth changing or complicating its syntax,
this will be available after 1.0 as compiler plugins so that developers can
write their own tag handlers that will be used at compile time to be
transformed into something else.

Blocks of Code as Values
------------------------

If for some reason we need to have more than one line of code in a place where
only a value is expected we can use a little known feature of erlang which of
course as its efene counterpart, the begin ... end block:

.. code-block:: javascript

        io.format("block result: ~p", [begin
                             A = 8
                             B = 0
                             divide_two(A, B)
                         end])

Instead of prividing a variable or a simple function call we wanted to do three
operations, if that's what's required then what you need is a begin ... end
block.

It's not something you need every day but here it's documented for completeness.

Sending and Receiving Messages
------------------------------

If you came to efene it may be because you heard that the erlang VM supports
cheap processes and message passing, here we will cover them, let's see an
example:

.. code-block:: javascript

    fn receive_and_print
        case:
            Pid = self()
            receive
                case ping:
                     print("~p received ping", [Pid])
                case Other:
                     print("~p received something else: ~p", [Pid, Other])
            after 1000:
                  print("Nothing received after 1000ms")
            end
    end

    fn spawn_receive
        case:
            OuterPid = self()
            spawn(fn case:
                  SpawnPid = self()
                  print("Process ~p sending to ~p", [SpawnPid, OuterPid])
                  OuterPid ! ping
            end)

            receive_and_print()

            receive_and_print()
    end

We define two functions, receive_and_print which will wait for a message and print
something depending on what it got and spawn_receive, which will spawn a new
process that will interact with the current process we are running.

Let's see it line by line, first we get the process id (pid) of the current process
by calling the builting function `erlang.self:0 <http://www.erlang.org/doc/man/erlang.html#self-0>`_:

.. code-block:: javascript

            OuterPid = self()

Then we spawn a new process by calling the builtin function `erlang.spawn:1 <http://www.erlang.org/doc/man/erlang.html#spawn-1>`_:

.. code-block:: javascript

            spawn(fn case:
                  SpawnPid = self()
                  print("Process ~p sending to ~p", [SpawnPid, OuterPid])
                  OuterPid ! ping
            end)

We pass one argument to spawn, which is an anonymous function that takes no
arguments, in it's body it gets its process id, then prints a message and
finally it sends the ping atom as a message to the process identified by the
process id stored in the variable OuterPid by using the **!** operator.

.. code-block:: javascript

            receive_and_print()

            receive_and_print()

Then we call receive_and_print twice, the output of running this code will be
something like::

    Process <0.81.0> sending to <0.44.0>
    <0.44.0> received ping
    Nothing received after 1000ms

The printed process ids will probably differ on your machine.

Now let's analyze the receive_and_print function, first we get the pid of the
current process:

.. code-block:: javascript

            Pid = self()

Then we use the receive expression to receive messages:

.. code-block:: javascript

            receive
                case ping:
                     print("~p received ping", [Pid])
                case Other:
                     print("~p received something else: ~p", [Pid, Other])
            after 1000:
                  print("Nothing received after 1000ms")
            end

The syntax should be already familiar, it starts with the receive keyword and
continues with zero or more case clauses, optionally an after section that
specifies the amount of milliseconds to wait for a message to arrive, if no
message arrives then the after body will be executed.

In the case clauses we pattern match against the ping atom to display a specific
message and then we match against anything to display a "catch all message",
if no message is received after a second we give up and print a message.

That's why we call it two times even when we spawned one process that sent
one message.

The first time it will receive a message and match against ping, but the second
time it will timeout and print the timeout message.

If you read carefully you will notice I said "with zero or more case clauses",
when I described the receive expression, it wasn't an error, you can have
zero case clauses, here is a useful example of that:

.. code-block:: javascript

    fn sleep
        case TimeMs:
             print("sleeping ~pms", [TimeMs])

             receive
             after TimeMs:
                   ok
             end
    end

The sleep function will print a message and sleep for the specified amount of
milliseconds, then return ok.

Like any other expression, the receive expression will return the last value
evaluated on the case clause it matches or in the after section.

Adding some Types
-----------------

At some point you may want to add some types to your code, for documentation
purposes or to help tools like `dialyzer <http://www.erlang.org/doc/man/dialyzer.html>`_
spot bugs for you, efene as usual provides the same features as erlang to add
types to your code, let's see an example:

.. code-block:: javascript

    @type(result(E, V)) -> (error, E) or (ok, V)
    @type(division_error()) -> result(division_by_zero, number())

    fn divide_two_typed
        @spec(number(), number()) -> division_error()
        case _A, 0: (error, division_by_zero)
        case A, B: (ok, A / B)
    end

First we declare a new generic type called **result** which receives two arguments,
this means you can "parameterize" the type providing your own types to it.

The result type is defined as either a two item tuple with the first item being
the atom error and the second item being the type passed as first argument to
the result type **or** a two item tuple containing the ok atom as first item
and the second item being the type passed as second argument to the result
type.

After the result type declaration we declare another type called
**division_error**, which doesn't receive arguments and is defined as the
result type where the error type can be the atom division_by_zero amd the value
type can be any number.

Notice that types are like function calls, a bare atom is just the atom value.

Then we define our divide_two_typed function and after the name we add a function
anotation *@spec* that is used to provide a type specification for the function,
there we define that the function receives two arguments of type number and
returns a value that satisfies the division_error type.

For more details on the syntax see the :ref:`language-reference`.

For more details on types see `Erlang's Types and Function Specifications <http://www.erlang.org/doc/reference_manual/typespec.html>`_ documentation about it.

