.. _quick-start:

Quick Start
===========

Here is a screencast of this procedure:

.. raw:: html

    <script type="text/javascript" src="https://asciinema.org/a/18378.js" id="asciicast-18378" async></script>

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
    Hello mariano!
    ok

    2> myfnapp:add(2, 3).
    5

you can quit the shell by calling the q function like this::

    3> q().
    ok

we can also try the logging version of the hello function, which uses the
`lager logging library <https://github.com/basho/lager/>`_, for that we need to
start the lager application before running the function, this needs to be done
manually on the shell but will be done automatically by the virtual machine
when running an application::

    ./rebar3 shell

    1> application:ensure_all_started(myfnapp).
    {ok,[syntax_tools,compiler,goldrush,lager,myfnapp]}
    20:21:49.127 [info] Application lager started on node nonode@nohost
    20:21:49.127 [info] Application myfnapp started on node nonode@nohost

    2> myfnapp:log_hello("bob").
    20:22:11.517 [info] Hello bob!
    ok

    3> q().
    ok

given that we are good software citizens we test our code, that's why we want
to run some unit tests to be sure that this works::

    ./rebar3 ct

this will compile the tests and run them for you.

in the template one test should fail, open test/{{name}}_SUITE.fn
(test/myfnapp_SUITE if you didn't change the app name) and fix it,
then run the test task again::

    ./rebar3 ct

that's it, now you can make changes, run *./rebar3 ct* again and
keep going.
