Efene Introduction
==================

This section describes the language through simple working examples, for a
complete reference see:ref:`language-reference`.

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

