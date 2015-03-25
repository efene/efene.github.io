Help Needed
===========

Here we list how you can help this project, there are tasks for every knowledge
level.

Wants to Play with Efene
------------------------

* Try efene report anything that confuses you or doesn't work

  + This includes incomplete, confusing or hard to understand error messages

* Explicitly test error detection and report errors that aren't handled correclty

  + For example if they end up in an internal error or traceback
  + Incomplete, confusing or hard to understand error messages

* Look for missing Erlang syntax support

  + Expressions that you can write in erlang but you can't in efene

No Erlang Knowledge Required
----------------------------

* `LightTable <http://lighttable.com/>`_ syntax highlighting support
* Vim syntax highlighting support
* Emacs syntax highlighting support
* `Pygments <http://pygments.org/>`_ syntax highlighting support

Erlang Knowledge Required
-------------------------

Improve the Pretty Printer
..........................

Efene pretty printer (fn_pp.erl) has some corner cases where indentation is
broken, take it to go fmt level.

Lager Interoperability
......................

`Lager <https://github.com/basho/lager/>`_ works by using parse transforms, we
have to look for a way to allow using lager without duplicating all the ast
generation.

Efene REPL
..........

A `rebar3 <http://www.rebar3.org/>`_ plugin to run an efene repl/shell

Erlang Compatibility Tests
..........................

Write tests that check that efene and erlang code that do the same thing
actually do the same thing.

For example write the code twice generating output and diffing the output.

A more complex solution is to compare the generated ast ignoring line numbers.
