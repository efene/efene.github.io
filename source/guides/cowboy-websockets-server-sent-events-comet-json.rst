Cowboy WebSockets/Server Sent Events/COMET JSON API Guide
=========================================================

Initial Setup
-------------

Like in the :ref:`quick-start` we will use `rebar3 <http://www.rebar3.org/>`_

First let's start installing the template we will use, this needs to be done only once::

    mkdir -p ~/.config/rebar3/templates
    git clone https://github.com/efene/rebar3_efene_template_push_app.git ~/.config/rebar3/templates/fn_push_app

Now we create the folder where our new project will live::

    mkdir mypushapp
    cd mypushapp

Then we install rebar inside our project folder::

    wget https://s3.amazonaws.com/rebar3/rebar3
    chmod u+x rebar3

We can then create the project using the installed template, change mypushapp for the name of your project but if you do remember to change it in the following commands too::

    ./rebar3 new fn_push_app name=mypushapp

We can then run the project::

    ./rebar3 run


