Rebar Plugin
============

Efene is used as a library through a `rebar3 <http://www.rebar3.org>`_ plugin
that is already available in efene rebar templates.

Compile Task
------------

Efene compile task can be used as follows::

    rebar3 efene compile

Options
.......

--format
    output format of the compile task, by default is "beam", values:

    * rawlex: output of the lexer step
    * lex: cleaned up lexer
    * ast: efene abstract syntax tree
    * erlast: erlang abstract syntax tree
    * mod: erlang abstract syntax tree with module nodes
    * erl: erlang code
    * beam: beam bytecode

--file
    file to compile, by default it will compile all files in the project

Example Usage
.............

This section uses the project described in the :ref:`quick-start` section.

Compile All Files
:::::::::::::::::

::

    rebar3 efene compile

Compile One File to Erlang
::::::::::::::::::::::::::

::

    rebar3 efene compile --format erl --file src/myfnapp.fn

Common Test Task
----------------

Efene `commmon test <http://www.erlang.org/doc/man/common_test.html>`_ task
can be used as follows::

    rebar3 efene ct

Shell Task
----------

Efene shell task can be used as follows::

    rebar3 efene shell
