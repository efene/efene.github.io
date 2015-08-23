Efene Toolbox
=============

A list of tools and libraries that are useful for efene projects.

.. contents::
   :local:
   :depth: 1

Testing
.......

* `Commom Test <http://www.erlang.org/doc/apps/common_test/basics_chapter.html>`_
* `EUnit <http://www.erlang.org/doc/apps/eunit/chapter.html>`_

Generative Testing
..................

* `Triq <http://krestenkrab.github.io/triq/>`_
* `QuickCheck <http://www.quviq.com/products/erlang-quickcheck/>`_
* `PropEr <http://proper.softlab.ntua.gr/>`_

Mocking
.......

* `Meck <https://github.com/eproxus/meck>`_

Load Generators
...............

* `Ponos <https://github.com/klarna/ponos>`_
* `Tsung <http://tsung.erlang-projects.org/>`_

Networking
...........

* `Damocles <https://github.com/lostcolony/damocles>`_

Build Tools
...........

* `Rebar3 <http://www.rebar3.org/>`_
* `Erlang.mk <https://github.com/ninenines/erlang.mk>`_

Release Management
..................

* `Relx <https://github.com/erlware/relx>`_

Web Servers
...........

* `Cowboy <https://github.com/ninenines/cowboy>`_
* `Mochiweb <https://github.com/mochi/mochiweb/>`_
* `WebMachine <https://github.com/webmachine/webmachine/>`_
* `Elli <https://github.com/knutin/elli>`_
* `Yaws <http://yaws.hyber.org/>`_

Web Server Utilities
....................

* `Cowboy Swagger <https://github.com/inaka/cowboy-swagger>`_: Swagger integration for Cowboy (built on trails)

Web Frameworks
..............

* `Axiom <https://github.com/tsujigiri/axiom>`_
* `ChicagoBoss <https://github.com/ChicagoBoss/ChicagoBoss>`_

Routing
.......

* `Router <https://github.com/zotonic/router>`_
* `Cowboy Trails <https://github.com/inaka/cowboy-trails>`_: A couple of improvements over Cowboy Routes

HTTP Clients
............

* `Shotgun <https://github.com/inaka/shotgun>`_
* `Gun <https://github.com/extend/gun/>`_
* `Hackney <https://github.com/benoitc/hackney>`_

Web Sockets Servers
...................

* `Bullet <https://github.com/extend/bullet/>`_
* `N2O <https://github.com/synrc/n2o>`_

Web Sockets Clients
...................

* `Gun <https://github.com/extend/gun/>`_

Server Sent Events Clients
..........................

* `Shotgun <https://github.com/inaka/shotgun>`_
* `Gun <https://github.com/extend/gun/>`_

Logging
.......

* `Lager <https://github.com/basho/lager>`_

Configuration
..............

* `Cuttlefish <https://github.com/basho/cuttlefish>`_

Databases
.........

* `eleveldb <https://github.com/basho/eleveldb>`_
* `ETS <http://www.erlang.org/doc/man/ets.html>`_
* `DETS <http://www.erlang.org/doc/man/dets.html>`_
* `Mnesia <http://www.erlang.org/doc/man/mnesia.html>`_
* `Bitcask <https://github.com/basho/bitcask>`_
* `sumo_db <https://github.com/inaka/sumo_db>`_

Database Clients
................

* `odbc <http://www.erlang.org/doc/apps/odbc/databases.html>`_
* `epgsql <https://github.com/epgsql/epgsql>`_
* `emysql <https://github.com/eonblast/Emysql/>`_
* `couchbeam <https://github.com/benoitc/couchbeam>`_
* `mongodb <https://github.com/mongodb/mongodb-erlang>`_
* `redo <https://github.com/heroku/redo>`_: pipelined erlang redis client

Clients
.......

* `kafkerl <https://github.com/HernanRivasAcosta/kafkerl>`_: Apache Kafka producer/consumer for erlang

Package Manager
...............

* `Hex <https://hex.pm/>`_
* `Rebar3 Hex Plugin <https://github.com/hexpm/rebar3_hex>`_: plugin to use hex from rebar3

Interop
.......

* `jinterface <http://www.erlang.org/doc/apps/jinterface/index.html>`_
* `NIFs <http://www.erlang.org/doc/tutorial/nif.html>`_
* `Ports <http://www.erlang.org/doc/reference_manual/ports.html>`_

Data Formats
............

* `edn-erlang <https://github.com/seancribbs/edn-erlang>`_
* `erldn <https://github.com/marianoguerra/erldn>`_

Cryptography
............

* `crypto <http://www.erlang.org/doc/man/crypto.html>`_
* `pbkdf2 <https://github.com/basho/erlang-pbkdf2>`_

Auth
....

* `OAuth2 <https://github.com/kivra/oauth2>`_

Encoding/Decoding
.................

* `protobuffs <https://github.com/basho/erlang_protobuffs>`_
* `thrift <https://thrift.apache.org/lib/erl>`_
* `eavro <https://github.com/SIfoxDevTeam/eavro>`_
* `transit <https://github.com/isaiah/transit-erlang>`_

Templates
.........

* `Mustache <https://github.com/soranoba/bbmustache>`_
* `ErlyDtl <https://github.com/erlydtl/erlydtl>`_

Command Line
............

* `getopt <https://github.com/jcomellas/getopt>`_
* `clique <https://github.com/basho/clique>`_
* `escript <http://www.erlang.org/doc/man/escript.html>`_

Distributed Programming
.......................

* `Riak Core <https://github.com/basho/riak_core>`_: distributed system framework, the core of riak_kv
* `chash <https://github.com/Licenser/chash>`_: consistent hashing library extracted from riak_core
* `plumtree <https://github.com/helium/plumtree>`_: epidemic broadcast protocol
* `disco <https://github.com/discoproject/disco>`_: Map/Reduce framework for distributed computing http://discoproject.org
* `nkdist <https://github.com/Nekso/nkdist>`_: Erlang distributed processes
* `nkcluster <https://github.com/Nekso/nkcluster>`_: A framework to manage jobs at huge Erlang clusters

Metrics
.......

* `Exometer <https://github.com/Feuerlabs/exometer>`_
* `Folsom <https://github.com/basho/folsom>`_

XML
...

* `Xmerl <http://www.erlang.org/doc/man/xmerl.html>`_
* `exml <https://github.com/paulgray/exml>`_

JSON
....

* `jsx <https://github.com/talentdeficit/jsx>`_
* `jiffy <https://github.com/davisp/jiffy>`_

JSON Schema
...........

* `jesse <https://github.com/klarna/jesse>`_

JSON Web Token
..............

* `ejwt <https://github.com/inaka/ejwt>`_
* `jwt-erl <https://github.com/marianoguerra/jwt-erl>`_

JSON Patch
..........

* `json-patch <https://github.com/marianoguerra/json-patch.erl>`_

Javascript
..........

* `erlang_js <https://github.com/basho/erlang_js>`_

Pub/Sub
.......

* `ErlBus <http://cabol.github.io/erlbus-erlang-message-bus/>`_
* `gen_event <http://www.erlang.org/doc/man/gen_event.html>`_
* `West <https://github.com/cabol/west>`_
* `TinyMQ <https://github.com/ChicagoBoss/tinymq>`_

Worker/Resource Pools
.....................

* `Sidejob <https://github.com/basho/sidejob>`_
* `Poolboy <https://github.com/devinus/poolboy>`_
* `worker_pool <https://github.com/inaka/worker_pool>`_
* `episcina <https://github.com/erlware/episcina>`_
* `gascheduler <https://github.com/GameAnalytics/gascheduler>`_

Rate Limiting
.............

* `Pobox <https://github.com/ferd/pobox>`_
* `Backoff <https://github.com/ferd/backoff>`_

Statistics
..........

* `basho_stats <https://github.com/basho/basho_stats>`_

Cloud
.....

* `erlcloud <https://github.com/gleber/erlcloud>`_

Sockets
.......

* `Ranch <https://github.com/ninenines/ranch>`_
* `gen_tcp <http://www.erlang.org/doc/man/gen_tcp.html>`_

Utils
.....

* `Katana <https://github.com/inaka/erlang-katana>`_
* `uuid <https://github.com/ferd/uuid>`_
* `erlware_commons <https://github.com/erlware/erlware_commons>`_
* `hope <https://github.com/ibnfirnas/hope>`_

Parsing
.......

* `Leex <http://www.erlang.org/doc/man/leex.html>`_: lexer
* `Yeec <http://www.erlang.org/doc/man/yecc.html>`_: LLR(1) parser generator
* `Spell1 <https://github.com/rvirding/spell1>`_: LL(1) parser generator
* `Neotoma <https://github.com/seancribbs/neotoma>`_: packrat parser-generator for parsing expression grammars

* `Aleppo <https://github.com/ErlyORM/aleppo>`_: Alternative Erlang Pre-Processor

Static Checkers
...............

* `Xref <http://www.erlang.org/doc/apps/tools/xref_chapter.html>`_
* `Dialyzer <http://www.erlang.org/doc/man/dialyzer.html>`_
* `Elvis <https://github.com/inaka/elvis>`_

Performance and Debugging
.........................

* `Eper <https://github.com/massemanet/eper>`_
* `Recon <https://github.com/ferd/recon>`_
* `eflame <https://github.com/proger/eflame>`_

Data Structures
...............

* `StateBox <https://github.com/mochi/statebox>`_
* `riak_dt <https://github.com/basho/riak_dt>`_

Data Structure Manipulation
...........................

* `Hubble <https://github.com/ferd/hubble>`_
* `Dotto <https://github.com/marianoguerra/dotto>`_

Scheduling
..........

* `ErlCron <https://github.com/erlware/erlcron>`_

Access Control
..............

* `snarl <https://github.com/project-fifo/snarl>`_: A Erlang based RBAC server.
* `nkrole <https://github.com/Nekso/nkrole>`_: a framework for managing complex relations among arbitrary objects in a riak_core cluster

Products
.........

* `CouchDB <http://couchdb.org/>`_: Database that uses JSON for documents, JavaScript for MapReduce indexes, and regular HTTP for its API
* `RabbitMQ <http://www.rabbitmq.com/>`_: Robust messaging for applications
* `Riak <http://basho.com/products/#riak>`_: Distributed NoSQL database with a key/value design and advanced local and multi-cluster replication
* `LeoFS <http://leo-project.net/>`_: Unstructured Object Storage for the Web and a highly available, distributed, eventually consistent storage system.
* `Ejabberd <https://www.process-one.net/en/ejabberd/>`_: World's Most Popular XMPP Server
* `MongooseIM <https://www.erlang-solutions.com/products/mongooseim-massively-scalable-ejabberd-platform>`_:  Base platform for building high performance messaging systems leveraging XMPP
* `OpenFlow <https://www.erlang-solutions.com/products/openflow>`_: Software Defined Networking (SDN)
* `Zotonic <http://zotonic.com/>`_: The Erlang Web Framework & CMS
* `logplex <https://github.com/heroku/logplex>`_:  Heroku log router
* `Chef <https://www.chef.io/>`_: Automation for Web-Scale IT


