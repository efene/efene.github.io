Efene Shell
===========

Efene provides a shell (or REPL) similar to the one provided by Erlang.

To get it you need to download and build efene::

    git clone https://github.com/efene/efene
    cd efene
    make

And then run::

    ./fnshell

You will see something like::

   $ ./fnshell

   Erlang/OTP 18 [erts-7.0] [source] [64-bit] [smp:4:4] [async-threads:10] [kernel-poll:false]

   efene shell (call q() to quit, help() for help, Ctrl+g for Job Control Mode)

   >>>

As the banner says, write `q()` and press enter to quit, write `help()` and
press enter to see other builtin functions, if you press Ctrl+g you enter
erlang's Job Control Mode, see "JCL Mode" section in the `shell manual page from the erlang documentation <http://www.erlang.org/doc/man/shell.html>`_ for more details of what you can do there.

You can symlink fnshell from a place in your $PATH to be able to run it from
any folder, for example::

    mkdir -p ~/bin
    cd ~/bin
    ln -s path/to/efene/fnshell

.. note::

    Change path/to/fnshell to the actual path where you have the fnshell file

Add ~/bin to your $PATH if you don't have it already::

    export PATH=$PATH:$HOME/bin

Add it to your shell rc file to have it permanently set (.zshrc for zsh, .bashrc for bash)
