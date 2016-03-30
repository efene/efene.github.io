BEAM Toolbox
============

A list of tools and libraries that are useful for BEAM languages like efene,
erlang, LFE and Elixir projects.

.. contents::
   :local:
   :depth: 1

Access Control
..............

* `snarl <https://github.com/project-fifo/snarl>`_: A Erlang based RBAC server.
* `nkrole <https://github.com/Nekso/nkrole>`_: a framework for managing complex relations among arbitrary objects in a riak_core cluster

Auth
....

* `OAuth2 <https://github.com/kivra/oauth2>`_

Build Tools
...........

* `Rebar3 <http://www.rebar3.org/>`_
* `Erlang.mk <https://github.com/ninenines/erlang.mk>`_

Cache
.....

* `Fling <https://github.com/basho-labs/fling>`_:  Cache library that promotes keys and values into mochiglobal objects
* `e2qc <https://github.com/arekinath/e2qc>`_: Erlang 2Q NIF cache
* `cherly <https://github.com/leo-project/cherly>`_: Cherly (sher-lee) is an in-VM caching library for Erlang
* `leo_mcerl <https://github.com/leo-project/leo_mcerl>`_: leo_mcerl is a memory cache lib for Erlang

Clients
.......

* `kafkerl <https://github.com/HernanRivasAcosta/kafkerl>`_: Apache Kafka producer/consumer for erlang
* `ekaf <https://github.com/helpshift/ekaf>`_: A minimal, high-performance Kafka client in Erlang
* `cqerl <https://github.com/matehat/cqerl>`_: Native Erlang CQL client for Cassandra
* `etorrent <https://github.com/jlouis/etorrent>`_: Erlang Bittorrent Client
* `amqp_client <https://github.com/jbrisbin/amqp_client>`_: Rebar-friendly fork of rabbitmq-erlang-client
* `zeta <https://github.com/tel/zeta>`_: An Erlang client for Riemann

Cloud
.....

* `erlcloud <https://github.com/gleber/erlcloud>`_

Command Line
............

* `getopt <https://github.com/jcomellas/getopt>`_
* `clique <https://github.com/basho/clique>`_
* `escript <http://www.erlang.org/doc/man/escript.html>`_
* `cf <https://github.com/project-fifo/cf>`_: Colored output for io and io_lib 
* `etermcap <https://github.com/project-fifo/etermcap>`_: Pure erlang termcap library

Compression
...........

* `erlang-lz4 <https://github.com/szktty/erlang-lz4>`_: LZ4 bindings for Erlang

Configuration
..............

* `Cuttlefish <https://github.com/basho/cuttlefish>`_
* `econfig <https://github.com/benoitc/econfig>`_: simple Erlang config handler using INI files

Cryptography
............

* `crypto <http://www.erlang.org/doc/man/crypto.html>`_: Crypto functions
* `pbkdf2 <https://github.com/basho/erlang-pbkdf2>`_: A PBKDF2 implementation for Erlang extracted from Apache CouchDB
* `enacl <https://github.com/jlouis/enacl>`_: Erlang bindings for NaCl / libsodium
* `erlsha2 <https://github.com/vinoski/erlsha2>`_: SHA-224, SHA-256, SHA-384, SHA-512 implemented in Erlang NIFs

Database Clients
................

* `odbc <http://www.erlang.org/doc/apps/odbc/databases.html>`_
* `epgsql <https://github.com/epgsql/epgsql>`_
* `pgpool <https://github.com/ostinelli/pgpool>`_: A PosgreSQL client that automatically uses connection pools and handles reconnections in case of errors. 
* `emysql <https://github.com/eonblast/Emysql/>`_
* `couchbeam <https://github.com/benoitc/couchbeam>`_
* `mongodb <https://github.com/mongodb/mongodb-erlang>`_
* `redo <https://github.com/heroku/redo>`_: pipelined erlang redis client

Databases
.........

* `eleveldb <https://github.com/basho/eleveldb>`_
* `ETS <http://www.erlang.org/doc/man/ets.html>`_
* `DETS <http://www.erlang.org/doc/man/dets.html>`_
* `Mnesia <http://www.erlang.org/doc/man/mnesia.html>`_
* `Bitcask <https://github.com/basho/bitcask>`_
* `sumo_db <https://github.com/inaka/sumo_db>`_
* `erocksdb <https://github.com/leo-project/erocksdb>`_:  Erlang bindings to RocksDB datastore

Data Formats
............

* `edn-erlang <https://github.com/seancribbs/edn-erlang>`_
* `erldn <https://github.com/marianoguerra/erldn>`_
* `transit-erlang <https://github.com/isaiah/transit-erlang>`_: Transit format for erlang
* `msgpack-erlang <https://github.com/msgpack/msgpack-erlang>`_: MessagePack (de)serializer implementation for Erlang
* `protobuffs <https://github.com/basho/erlang_protobuffs>`_
* `thrift <https://thrift.apache.org/lib/erl>`_
* `eavro <https://github.com/SIfoxDevTeam/eavro>`_
* `benc <https://github.com/jlouis/benc>`_: Erlang BEncode parser/unparser
* `leo_csv <https://github.com/leo-project/leo_csv>`_: CSV Parser for Erlang

Data Structures
...............

* `StateBox <https://github.com/mochi/statebox>`_
* `riak_dt <https://github.com/basho/riak_dt>`_
* `pqueue <https://github.com/okeuday/pqueue>`_: Erlang Priority Queues
* `erlang-lru <https://github.com/barrel-db/erlang-lru>`_: Erlang LRU: a fixed size LRU cache

Data Structure Manipulation
...........................

* `Hubble <https://github.com/ferd/hubble>`_
* `Dotto <https://github.com/marianoguerra/dotto>`_

Date and Time
.............

* `dh_date <https://github.com/daleharvey/dh_date>`_: Date formatting / parsing library for erlang
* `strftimerl <https://github.com/gmr/strftimerl>`_: Erlang implementation of strftime

Distributed Programming
.......................

* `Riak Core <https://github.com/basho/riak_core>`_: distributed system framework, the core of riak_kv
* `chash <https://github.com/Licenser/chash>`_: consistent hashing library extracted from riak_core
* `plumtree <https://github.com/helium/plumtree>`_: epidemic broadcast protocol
* `disco <https://github.com/discoproject/disco>`_: Map/Reduce framework for distributed computing http://discoproject.org
* `nkdist <https://github.com/Nekso/nkdist>`_: Erlang distributed processes
* `nkcluster <https://github.com/Nekso/nkcluster>`_: A framework to manage jobs at huge Erlang clusters
* `dht <https://github.com/jlouis/dht>`_: DHT implementation in Erlang
* `syn <https://github.com/ostinelli/syn>`_: global process registry for Erlang

Fault Tolerance
...............

* `fuse <https://github.com/jlouis/fuse>`_: A Circuit Breaker for Erlang
* `safetyvalve <https://github.com/jlouis/safetyvalve>`_: A safety valve for your erlang node
* `breaky <https://github.com/mmzeeman/breaky>`_: supervise and manage modules and processes depending on external resources.
* `circuit_breaker <https://github.com/klarna/circuit_breaker>`_: Generic circuit breaker that can be used to break any service that isn't fully functional
* `elarm: <https://github.com/esl/elarm>`_: an Alarm Manager for Erlang

File System
...........

* `fuserl <https://github.com/tonyrog/fuserl>`_: Erlang bindings for FUSE

Generative Testing
..................

* `Triq <http://krestenkrab.github.io/triq/>`_
* `QuickCheck <http://www.quviq.com/products/erlang-quickcheck/>`_
* `PropEr <http://proper.softlab.ntua.gr/>`_
* `eqc_lib <https://github.com/jlouis/eqc_lib>`_: Erlang QuickCheck common library functions

HTTP Clients
............

* `Shotgun <https://github.com/inaka/shotgun>`_
* `Gun <https://github.com/extend/gun/>`_
* `Hackney <https://github.com/benoitc/hackney>`_

Interop
.......

* `jinterface <http://www.erlang.org/doc/apps/jinterface/index.html>`_
* `NIFs <http://www.erlang.org/doc/tutorial/nif.html>`_
* `Ports <http://www.erlang.org/doc/reference_manual/ports.html>`_

Internet of Things
..................

* `gen_coap <https://github.com/gotthardp/gen_coap>`_: Generic Erlang CoAP Client/Server
* `vernemq <https://verne.mq/>`_: The most scalable MQTT Message Broker. Powering IoT, M2M, Mobile, and Web Applications.
* `emqtt <http://emqtt.io/>`_: The Massively Scalable MQTT Broker written in Erlang/OTP
* `emqttc <https://github.com/emqtt/emqttc>`_: Asynchronous Erlang MQTT Client
* `rabbitmq-mqtt <https://github.com/rabbitmq/rabbitmq-mqtt>`_: RabbitMQ MQTT gateway

Javascript
..........

* `erlang_js <https://github.com/basho/erlang_js>`_

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

Load Generators
...............

* `Ponos <https://github.com/klarna/ponos>`_
* `Tsung <http://tsung.erlang-projects.org/>`_

Logging
.......

* `Lager <https://github.com/basho/lager>`_
* `erlang-syslog <https://github.com/Vagabond/erlang-syslog>`_: Erlang port driver for interacting with syslog via syslog(3)
* `chronica <https://github.com/eltex-ecss/chronica>`_: Logger framework for Erlang applications

Metrics
.......

* `Exometer <https://github.com/Feuerlabs/exometer>`_: Basic measurement objects and probe behavior

  + `exometer_json <https://github.com/helium/exometer_json>`_: exometer reporter to push JSON to a sink over HTTP

* `Folsom <https://github.com/basho/folsom>`_: Expose Erlang Events and Metrics
* `MzMetrics <https://github.com/machinezone/mzmetrics>`_:  High performance Erlang metrics library

Mocking
.......

* `Meck <https://github.com/eproxus/meck>`_

Networking
...........

* `Damocles <https://github.com/lostcolony/damocles>`_

Package Manager
...............

* `Hex <https://hex.pm/>`_
* `Rebar3 Hex Plugin <https://github.com/hexpm/rebar3_hex>`_: plugin to use hex from rebar3

Patterns
........

* `Erlang Patterns <http://www.erlangpatterns.org/>`_: An experimental project to apply Christopher Alexander’s pattern language method, as outlined in The Timeless Way of Building, to Erlang programming.

Parsing
.......

* `Leex <http://www.erlang.org/doc/man/leex.html>`_: lexer
* `Yeec <http://www.erlang.org/doc/man/yecc.html>`_: LLR(1) parser generator
* `Spell1 <https://github.com/rvirding/spell1>`_: LL(1) parser generator
* `Neotoma <https://github.com/seancribbs/neotoma>`_: packrat parser-generator for parsing expression grammars

* `Aleppo <https://github.com/ErlyORM/aleppo>`_: Alternative Erlang Pre-Processor

Performance and Debugging
.........................

* `Eper <https://github.com/massemanet/eper>`_
* `Recon <https://github.com/ferd/recon>`_
* `eflame <https://github.com/proger/eflame>`_
* `eep <https://github.com/virtan/eep>`_: Erlang Easy Profiling (eep) application provides a way to analyze application performance and call hierarchy

Plugins
.......

* `hooks <https://github.com/barrel-db/hooks>`_: generic plugin & hook system for Erlang applications

Protocols
.........

* `erlirc <https://github.com/archaelus/erlirc>`_: Erlang IRC client/server framework
* `mdns <https://github.com/arcusfelis/mdns>`_: More generic (yet another) mDNS, Zeroconf, Avahi client/server for Erlang
* `esmtp <https://github.com/archaelus/esmtp>`_: Erlang SMTP library

Products
........

* `CouchDB <http://couchdb.org/>`_: Database that uses JSON for documents, JavaScrip tfoi MapReduce indexes, anod regular HTTP for its API
* `RabbitMQ <http://www.rabbitmq.com/>`_: Robust messaging for applications
* `Riak <http://basho.com/products/#riak>`_: Distributed NoSQL database with a key/value design and advanced local and multi-cluster replication
* `LeoFS <http://leo-project.net/>`_: Unstructured Object Storage for the Web and a highly available, distributed, eventually consistent storage system.
* `OpenFlow <https://www.erlang-solutions.com/products/openflow>`_: Software Defined Networking (SDN)
* `Zotonic <http://zotonic.com/>`_: The Erlang Web Framework & CMS
* `logplex <https://github.com/heroku/logplex>`_:  Heroku log router
* `Chef <https://www.chef.io/>`_: Automation for Web-Scale IT

XMPP Servers
............

* `Ejabberd <https://www.process-one.net/en/ejabberd/>`_: World's Most Popular XMPP Server
* `MongooseIM <https://www.erlang-solutions.com/products/mongooseim-massively-scalable-ejabberd-platform>`_:  Base platform for building high performance messaging systems leveraging XMPP

XMPP Clients
............

* `escalus <https://github.com/esl/escalus>`_: XMPP client library for conveniently testing XMPP servers

Pub/Sub
.......

* `ErlBus <http://cabol.github.io/erlbus-erlang-message-bus/>`_
* `gen_event <http://www.erlang.org/doc/man/gen_event.html>`_
* `West <https://github.com/cabol/west>`_
* `TinyMQ <https://github.com/ChicagoBoss/tinymq>`_
* `Syn <https://github.com/ostinelli/syn>`_:  A global Process Registry and Process Group manager for Erlang
* `leo_mq <https://github.com/leo-project/leo_mq>`_: leo_mq is a local message-queueing library

Rate Limiting
.............

* `Pobox <https://github.com/ferd/pobox>`_
* `Backoff <https://github.com/ferd/backoff>`_

Release Management
..................

* `Relx <https://github.com/erlware/relx>`_

Routing
.......

* `Router <https://github.com/zotonic/router>`_
* `Cowboy Trails <https://github.com/inaka/cowboy-trails>`_: A couple of improvements over Cowboy Routes

Scheduling
..........

* `ErlCron <https://github.com/erlware/erlcron>`_

Server Sent Events Clients
..........................

* `Shotgun <https://github.com/inaka/shotgun>`_
* `Gun <https://github.com/extend/gun/>`_

Sockets
.......

* `Ranch <https://github.com/ninenines/ranch>`_
* `gen_tcp <http://www.erlang.org/doc/man/gen_tcp.html>`_
* `Shackle <https://github.com/lpgauth/shackle>`_:  High Performance Erlang Network Client Framework

SOAP
....

* `soap <https://github.com/bet365/soap>`_: Make it easy to use SOAP from Erlang

Static Checkers
...............

* `Xref <http://www.erlang.org/doc/apps/tools/xref_chapter.html>`_
* `Dialyzer <http://www.erlang.org/doc/man/dialyzer.html>`_
* `Elvis <https://github.com/inaka/elvis>`_

Statistics
..........

* `basho_stats <https://github.com/basho/basho_stats>`_
* `bear <https://github.com/boundary/bear>`_: a set of statistics functions for erlang

Security
........

* `erlang-certifi <https://github.com/certifi/erlang-certifi>`_: SSL Certificates for Erlang

Templates
.........

* `Mustache <https://github.com/soranoba/bbmustache>`_
* `ErlyDtl <https://github.com/erlydtl/erlydtl>`_

Testing
.......

* `Commom Test <http://www.erlang.org/doc/apps/common_test/basics_chapter.html>`_
* `EUnit <http://www.erlang.org/doc/apps/eunit/chapter.html>`_

Tools
.....

* `observer_cli <https://github.com/zhongwencool/observer_cli>`_:  A sharp shell tool see erlang node.
* `erlyberly <https://github.com/andytill/erlyberly>`_: debugger for erlang and elixir using erlang tracing. It is probably the easiest and quickest way to start debugging your erlang nodes.
* `visualixir <https://github.com/koudelka/visualixir>`_: toy process visualizer for remote BEAM nodes, written in Phoenix/Elixir/d3.
* `edump <https://github.com/archaelus/edump>`_: Erlang Crashdump Analysis Suite

Utils
.....

* `Katana <https://github.com/inaka/erlang-katana>`_
* `uuid <https://github.com/okeuday/uuid>`_
* `erlware_commons <https://github.com/erlware/erlware_commons>`_
* `hope <https://github.com/ibnfirnas/hope>`_

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
* `sumo_rest <https://github.com/inaka/sumo_rest>`_: Generic cowboy handlers to work with Sumo
* `vegur <https://github.com/heroku/vegur>`_: HTTP Proxy Library

Web Frameworks
..............

* `Axiom <https://github.com/tsujigiri/axiom>`_
* `ChicagoBoss <https://github.com/ChicagoBoss/ChicagoBoss>`_
* `Tuah <http://mhishami.github.io/tuah/>`_: A Simple Cowboy Frontend, inspired by BeepBeep

Web Sockets Servers
...................

* `Bullet <https://github.com/extend/bullet/>`_
* `N2O <https://github.com/synrc/n2o>`_

Web Sockets Clients
...................

* `Gun <https://github.com/extend/gun/>`_

Worker/Resource Pools
.....................

* `Sidejob <https://github.com/basho/sidejob>`_
* `Poolboy <https://github.com/devinus/poolboy>`_
* `worker_pool <https://github.com/inaka/worker_pool>`_
* `episcina <https://github.com/erlware/episcina>`_
* `gascheduler <https://github.com/GameAnalytics/gascheduler>`_
* `dispcount <https://github.com/ferd/dispcount>`_: Erlang task dispatcher based on ETS counters
* `leo_pod <https://github.com/leo-project/leo_pod>_`: A Fast Erlang worker pool manager

XML
...

* `Xmerl <http://www.erlang.org/doc/man/xmerl.html>`_
* `exml <https://github.com/paulgray/exml>`_

