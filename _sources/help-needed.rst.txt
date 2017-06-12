Help Needed
===========

Here we list how you can help this project, there are tasks for every knowledge
level.

Please visit `Efene Community Issue Tracker <https://github.com/efene/community/issues>`_
for top level tasks that don't fit in a specific project (or the project
doesn't exist yet). Visit each specific project issue tracker for issues
specific to existing projects at https://github.com/efene/

Wants to Play with Efene
------------------------

* Try efene report anything that confuses you or doesn't work

  + This includes incomplete, confusing or hard to understand error messages

* Explicitly test error detection and report errors that aren't handled correclty

  + For example if they end up in an internal error or traceback
  + Incomplete, confusing or hard to understand error messages

* Look for missing Erlang syntax support

  + Expressions that you can write in erlang but you can't in efene

* Write Rebar3 templates for common modules

No Erlang Knowledge Required
----------------------------

* `Visual Studio <https://code.visualstudio.com/>`_ syntax highlighting support

  + `Issue 10 <https://github.com/efene/community/issues/10>`_

* Vim syntax highlighting support

  + `Issue 6 <https://github.com/efene/community/issues/6>`_

* Emacs syntax highlighting support

  + `Issue 7 <https://github.com/efene/community/issues/7>`_

* `Pygments <http://pygments.org/>`_ syntax highlighting support

  + `Issue 9 <https://github.com/efene/community/issues/9>`_

Erlang Knowledge Required
-------------------------

Improve rebar3 plugins
......................

* Add options to `compile <https://github.com/efene/rebar3_efene_compile>`_
* Add options to `ct plugin <https://github.com/efene/rebar3_efene_ct>`_

Improve the Pretty Printer
..........................

Efene pretty printer (fn_pp.erl) has some corner cases where indentation is
broken, take it to go fmt level.

Erlang Compatibility Tests
..........................

Write tests that check that efene and erlang code that do the same thing
actually do the same thing.

For example write the code twice generating output and diffing the output.

A more complex solution is to compare the generated ast ignoring line numbers.
