Templates
=========

Providing a simple "getting started" experience is part of the efene
project, for this we focus on documentation, support, error messages but
also on templates so you can get started quickly using the best practices
from the community.

For this, efene mantains official rebar3 templates that you can use to
create a wide variety of projects, here we will give a brief description
of each, what they're for and how to install and use them.

Initial Setup Common to All Templates
-------------------------------------

First of all you need a recent version of rebar3 installed in your $PATH, for
instruction on how to install rebar3 please read `rebar3's getting started page <http://www.rebar3.org/docs/getting-started>`_.

Then you need the root template folder available to install the templates, to
do this run::

    mkdir -p ~/.config/rebar3/templates

Escript Template
----------------

This templates allows the creation of an `escript <erlang.org/doc/man/escript.html>`_ project.

Escripts are runnable erlang programs that are packed in a single file, to run
them you need erlang installed in your system.

Install
.......

::

    git clone https://github.com/efene/rebar3_efene_template_escript.git ~/.config/rebar3/templates/fn_escript

Use
...

::

    rebar3 new fn_escript name=myscript
    cd myscript
    rebar3 escriptize

Now you have your script at `_build/default/bin/myscript`, you can put it on your path to use it, let's test it::

    $ ./_build/default/bin/myscript
    Args: []

    $ ./_build/default/bin/myscript foo bar
    Args: ["foo","bar"]

Library Template
----------------

Install
.......

::

    git clone https://github.com/marianoguerra/rebar3_efene_template_lib.git ~/.config/rebar3/templates/fn_lib

Use
...

::

    rebar3 new fn_lib name=mylib
    cd mylib
    rebar3 compile
    rebar3 ct

Try
...

::

    $ rebar3 efene shell

    Erlang/OTP 18 [erts-7.0] [source] [64-bit] [smp:4:4] [async-threads:10] [kernel-poll:false]

    efene shell (call q() to quit, help() for help, Ctrl+g for Job Control Mode)

    >>> mylib.add(2, 3)
    5

    >>> q()

    Bye!

OTP Application Template
------------------------

Install
.......

::

    git clone https://github.com/efene/rebar3_efene_template_app.git ~/.config/rebar3/templates/fn_app

Use
...

::

    rebar3 new fn_app name=myapp
    cd myapp
    rebar3 compile
    rebar3 ct

Try
...

::

    $ rebar3 efene shell
    /home/mariano/tmp/myapp/_build/default/plugins/efene/fnshell -pz /home/mariano/tmp/myapp/_build/default/lib/*/ebin/
    Erlang/OTP 18 [erts-7.0] [source] [64-bit] [smp:4:4] [async-threads:10] [kernel-poll:false]

    efene shell (call q() to quit, help() for help, Ctrl+g for Job Control Mode)

    >>> myapp_util.add(2, 3)
    5

    >>> q()

    Bye!

OTP Release Template
--------------------

Install
.......

::

    git clone https://github.com/efene/rebar3_efene_template_rel.git ~/.config/rebar3/templates/fn_rel

Use
...

::

    rebar3 new fn_rel name=myrel
    cd myrel
    rebar3 release

Try
...

::

   $ make console

    ...

    Erlang/OTP 18 [erts-7.0] [source] [64-bit] [smp:4:4] [async-threads:30] [kernel-poll:true]

    22:29:17.141 [info] starting myrel
    22:29:17.141 [info] Application lager started on node 'myrel@127.0.0.1'
    22:29:17.141 [info] Application myrel started on node 'myrel@127.0.0.1'

    ...

    22:29:17.156 [info] Application sasl started on node 'myrel@127.0.0.1'
    Eshell V7.0  (abort with ^G)
    (myrel@127.0.0.1)1> q().
    ok

