Cowboy REST JSON API Guide
==========================

Here is a screencast of this procedure:

.. raw:: html

    <script type="text/javascript" src="https://asciinema.org/a/18378.js" id="asciicast-18378" async></script>

Like in the :ref:`quick-start` we will use `rebar3 <http://www.rebar3.org/>`_

First let's start installing the template we will use, this needs to be done only once::

    mkdir -p ~/.config/rebar3/templates
    git clone https://github.com/efene/rebar3_efene_template_rest_app.git ~/.config/rebar3/templates/fn_rest_app

Now we create the folder where our new project will live::

    mkdir myrestapp
    cd myrestapp

Then we install rebar inside our project folder::

    wget https://s3.amazonaws.com/rebar3/rebar3
    chmod u+x rebar3

We can then create the project using the installed template, change myrestapp for the name of your project but if you do remember to change it in the following commands too::

    ./rebar3 new fn_rest_app name=myrestapp

We can then compile the project::

    ./rebar3 compile

And start it via the erlang shell::

    ./rebar3 shell

Inside the shell we run::

    application:ensure_all_started(myrestapp).

From another shell we can test our API::

    curl http://localhost:8080/
    curl http://localhost:8080/ -H "Accept: text/plain"
    curl http://localhost:8080/ -H "Accept: application/json"

We can open our browser and go to http://localhost:8080/ to see the html version.
