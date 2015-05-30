Cowboy REST JSON API Guide
==========================

Initial Setup
-------------

Here is a screencast of this procedure:

.. raw:: html

    <script type="text/javascript" src="https://asciinema.org/a/18417.js" id="asciicast-18417" async></script>

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

We can then run the project::

    ./rebar3 run

From another shell we can test our API::

    curl http://localhost:8080/
    curl http://localhost:8080/ -H "Accept: text/plain"
    curl http://localhost:8080/ -H "Accept: application/json"

We can open our browser and go to http://localhost:8080/ to see the html version.

Adding a Resource
-----------------

We have our basic REST API running but we want to add a resource, for that we
can use another template, the first time we will need to add it to our template
directory::

    git clone https://github.com/efene/rebar3_efene_template_rest_resource.git ~/.config/rebar3/templates/fn_rest_resource

After this we can create our new resource, let's create a user resource::

    rebar3 new fn_rest_resource name=user

Finally we need to add our resource to the routes of our API, open src/myrestapp_app.fn and change this::

    Dispatch = cowboy_router.compile([(`_`, [("/", myrestapp_handler, []) ])

For this::

    Dispatch = cowboy_router.compile([(`_`,
                                       [("/", myrestapp_handler, []),
                                        ("/user", user_rest_handler, [])])
                                     ])

Stop the shell if you are running it (press Control + C) and start it again::

    ./rebar3 run

Now we can test our resource from the command line::

    curl -X GET http://localhost:8080/user -H "Content-Type: application/json"
    {"method":"GET"}

    curl -X DELETE http://localhost:8080/user -H "Content-Type: application/json"

    curl -X POST http://localhost:8080/user -H "Content-Type: application/json" -d "[1,2,3]"
    {"body":[1,2,3],"method":"POST"}

    curl -X PUT http://localhost:8080/user -H "Content-Type: application/json" -d "[1,2,3]"
    {"body":[1,2,3],"method":"PUT"}

