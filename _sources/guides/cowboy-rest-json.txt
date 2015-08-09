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

We can then build the project::

    ./rebar3 release

And start it::

    ./_build/default/rel/myrestapp/bin/myrestapp console

From another shell we can test our API::

    curl http://localhost:8080/
    curl http://localhost:8080/ -H "Accept: text/plain"
    curl http://localhost:8080/ -H "Accept: application/json"

We can open our browser and go to http://localhost:8080/ to see the html version.

You can quit the console by running **q().** like this::

    (myrestapp@127.0.0.1)1> q().
    ok

Adding a Resource
-----------------

We have our basic REST API running but we want to add a resource, for that we
can use another template, the first time we will need to add it to our template
directory::

    git clone https://github.com/efene/rebar3_efene_template_rest_resource.git ~/.config/rebar3/templates/fn_rest_resource

After this we can create our new resource, let's create a user resource::

    cd apps/myrestapp/src
    rebar3 new fn_rest_resource name=user
    cd ../../..

Finally we need to add our resource to the routes of our API, open apps/myrestapp/src/myrestapp_app.fn and change this::

    Dispatch = cowboy_router.compile([(`_`, [("/", myrestapp_handler, []) ])

For this::

    Dispatch = cowboy_router.compile([(`_`,
                                       [("/", myrestapp_handler, []),
                                        ("/user", user_rest_handler, [])])
                                     ])

Stop the shell if you are running it (call "q()."), build and start it again::

    ./rebar3 release
    ./_build/default/rel/myrestapp/bin/myrestapp console

Now we can test our resource from the command line::

    curl -X GET http://localhost:8080/user -H "Content-Type: application/json"
    {"method":"GET"}

    curl -X DELETE http://localhost:8080/user -H "Content-Type: application/json"

    curl -X POST http://localhost:8080/user -H "Content-Type: application/json" -d "[1,2,3]"
    {"body":[1,2,3],"method":"POST"}

    curl -X PUT http://localhost:8080/user -H "Content-Type: application/json" -d "[1,2,3]"
    {"body":[1,2,3],"method":"PUT"}

Changing the Configuration
--------------------------

Say we want to change the port where the app is running, how do we do it?

Well, this template has it all covered, we use `cuttlefish <https://github.com/basho/cuttlefish>`_ to handle the configuration.

Open the file at **./_build/default/rel/myrestapp/etc/myrestapp.conf** and search for the line that contains "http.port = 8080",

change the port to something else, like 8081, save and quit.

Now start the server again and look at the logs while it starts, it should print a line like this::

    [info] App myrestapp started at port 8081

this configuration file and its parser are generated from the file at
config/config.schema, read the cuttlefish documentation for more information,
but as a start you can modify/remove the existing fields that are there as
examples.
