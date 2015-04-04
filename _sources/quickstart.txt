.. _quick-start:

Quick Start
===========

Here is a screencast of this procedure:

.. raw:: html

    <script type="text/javascript" src="https://asciinema.org/a/18167.js" id="asciicast-18167" async></script>

We will use `rebar3 <http://www.rebar3.org/>`_ to make our lifes easier.

first we need to install the efene app template to use it later, this only
needs to be done once::

    mkdir -p ~/.config/rebar3/templates
    git clone https://github.com/efene/rebar3_efene_template_app.git ~/.config/rebar3/templates/fn_app

you can install other templates to use later running the following commands::

    git clone https://github.com/efene/rebar3_efene_template_gen_server.git ~/.config/rebar3/templates/fn_gen_server
    git clone https://github.com/efene/rebar3_efene_template_gen_fsm.git ~/.config/rebar3/templates/fn_gen_fsm
    git clone https://github.com/efene/rebar3_efene_template_supervisor.git ~/.config/rebar3/templates/fn_supervisor

now let's create a project called myfnapp by creating the directory::

    mkdir myfnapp

then we download the latest version of rebar3 inside our app folder and make it
executable::

    cd myfnapp
    wget https://s3.amazonaws.com/rebar3/rebar3
    chmod u+x rebar3

and we create a new app called myfnapp using the fn_app template::

    ./rebar3 new fn_app name=myfnapp

now we can compile our app::

    ./rebar3 compile

and try it in the erlang shell (sorry, no stable efene shell yet)::

    ./rebar3 shell

and try it::

    1> myfnapp:hello("mariano").
    Hello mariano!ok

but given that we are good software citizens we test our code with unit tests,
that's why we want to run some unit tests to be sure that this works::

    ./rebar3 ct

this will compile the tests and run the tests for you.

that's it, now you can make changes, run *./rebar3 ct* again and
keep going.
