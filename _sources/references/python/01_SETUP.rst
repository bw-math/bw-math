.. _python_setup:

============
Python Setup
============

**Python** will run on virtually any device with a processor. It supports all operating systems: Windows, Mac and Linux.

Python Installation
===================

.. note:: 
    
    Ensure you are connected to the internet before attempting any of the commands on this page, especially :ref:`python_packages` section. When you install third-party libraries into **Python**, your computer needs to reach out to the `Python Package Index (PyPi) <https://pypi.org/>`_, where all of the extra libraries are stored. 

ChromeOS
--------

This video will illustrate each of the steps below.

(TODO INSERT YOUTUBE VIDEO HERE)


Step 1: Update ChromeOS 
***********************

Ensure you are on the latest version of the ChromeOS operating system.

(INSERT SCREENSHOT)

Step 2: Enable Linux Subsystem
******************************

Enable and install Linux subsystem in the Settings menu,

(INSERT SCREENSHOT)

This will give you access to something called the *command line* (sometimes called a *terminal* or a *shell*). The *command line* is a direct interface to the operating system of your laptop. Let's take a look.

Step 3: Explore A Little
************************

A new world has now opened up to you, the world of *Linux*. Let's take a little while to familiarize ourselves with it before moving on to **Python**. Open Linux command line (*terminal*),

(INSERT PICTURE)


.. note:: 

    Pin the Linux terminal to your dock for quick access.

    (INSERT SCREENSHOT)
    
This is your *operating system*. Let's try a few commands here and see what we can see. You can type (or copy and paste) the next command directly into the *cursor* of the terminal,

.. code:: shell

    echo "Hello World"

Press ``ENTER`` and you shoud see the words "*Hello World*" print to screen. The ``echo`` command, as you might have guessed, simply prints the words (a *string* of text) you give it back to screen,

(INSERT PICTURE)

Not very useful. Let's try something a little more interesting,

.. code:: shell

    df 

Press ``ENTER`` and you will see something along the lines of (the actual output will vary from computer to computer), 

(INSERT PICTURE)

These are your computer filesystems. This is where all of the data on your computer lives. Let's not mess around with it. While you can't physically break your computer by entering commands, it is possible to break your *operating system* to the point where it will need re-installed. That is not something you want to happen. For that reason, let's move on to other, safer areas.

The *Linux* world is a hierarchy of files. Everything in *Linux* is a file, even folders. 

.. note:: 

    Folders are called *directories* in Linux.

You can imagine a tree like the following picture exists somewhere inside your computer,

(INSERT PICTURE)

When you open your *terminal*, you open it *in* one of the folders in this tree. The *terminal* allows you traverse the different nodes and branches of this tree. To see where you currently located in the tree, type the following command and press ``ENTER``,

.. code:: shell

    pwd 

This stands for "*present working directory*". When you type ``ENTER``, you will see a file path print to screen. This is the directory where you terminal is currently idling. You can see the contents of the *present working directory* with the command,

.. code:: shell

    ls 

This will list the contents of the directory to screen,

(INSERT PICTURE)

You can *change directories* with the next command, 

.. code:: shell

    cd <path>

Where ``<path>`` is the location of the directory into which you would like to go. 

You can move *up* the file hierarchy by typing,

.. code:: shell
    
    cd .. 

If you then print the *present working directory*, you will see the directory you were just in.

.. code:: shell

    pwd
 
Alright, that was fun. However, this class isn't about learning the ins and outs of *Linux*. This section was merely to show you for what the terminal is used: issuing commands.

Step 3: Install Python 
**********************

**Python** *should* come pre-installed in most *Linux* distributions. Open a terminal and verify your installation with the following command, 

.. code:: shell

    python --version

(INSERT SCREENSHOT)

If you get an error along the lines of "*bash: python command not found*", you will need to install **Python**. You can do this through the *Linux* package repository, an online library of software that you can install from the command line,

.. code:: shell

    sudo apt-get install python3

.. warning:: 

    Make sure you install **Python3**. **Python2**, an older version, is still available to be installed. If you encounter any unknown errors through the course of this class, the first thing you check if what *version* of **Python** you are running.

Once this command completes, verify you installation by printing the version to screen,

.. code:: shell

    python --version

Step 4: Install Libraries 
*************************

**Python** alone is not enough. We need to plugin some additional functionality to the bare bones installation of **Python**. 

In order to create graphics, we need a graphics library. 
 
The following command installs a PNG/JPEG rendering engines on your ChromeBook,

.. code:: shell 

    sudo apt-get install python3-tk

We are currently installing from the *Linux* package repository. We will need a way to install **Python** packages as well.

The following command installs the **Python** package manager,

.. code:: shell

    sudo apt-get install python3-pip

Lastly, while the command line is fun tool, it would be nice to have an text editor to develop **Python** programs. *IDLE* is the solution to this problem. We will talk more about this editor in the next section. For now, you can install it with the following command,

.. code:: shell

    sudo apt-get install idle3

Congratulation, you are now setup to run **Python** scripts on your ChromeBook.

Other Operating Systems
-----------------------

If you want to install **Python** on your home PC or laptop, you can download the official installer on found the `Python website <https://www.python.org/downloads/>`_ and follow the steps in this section,

1. Go to *https://www.python.org/downloads** and click the **Download** button,

.. image:: ../../assets/imgs/python/install_step_1.png

2. Download the appriopriate operating system distribution,

.. image:: ../../assets/imgs/python/install_step_2.png

3. Ensure the option "*Add Python to the PATH*" is checked,

.. image:: ../../assets/imgs/python/install_step_3.png

4. Ensure all of the following options are checked,

.. image:: ../../assets/imgs/python/install_step_4.png

5. All of the other defaults are fine. Proceed with the installation. When it is done, you will now have icons for the **Python** interpreter and :ref:`IDLE <python_idle>` in your start menu (or your app launcher, if you're one of the weird *Mac* people.)

.. _python_interpretter:

Interpretter
============

Once **Python** is installed, you will have access to the `python` command on the terminal. Open a *Linux* and verify your installation with the following command, 

.. code:: shell
    
    python --version

If you see a version print out, you are good to go. If you get an error that says "*bash: python command not found*", head back to the previous section and make sure you completed all of the steps. 

You can start an *interpretter* session with,

.. code:: shell

    python

This will bring up the **Python** *shell*, which allows you to enter commands and expressions line by line. Up to this point we have been allow *Linux* to intrepret our commands. We are now handing off that responsiblity to **Python**. Like *Linux*, **Python** *interprets* your commands after you type ``ENTER``.

For example, type the following arithmetical expression and then type ``ENTER`` to execute it,

.. code:: python

    5 + 7

You can also print text to screen with the `print()` function, similar to (but not exactly like) *Linux*'s ``echo`` function,

.. code:: python

    print("Hello world")

We won't use the *interpretter* much in this class, but it is a handy tool to quickly check if a expression you had in mind is syntactical. For example, you might want to square a number and try,

.. code:: 

    2 ^ 2

However, this is not how you raise a number to a power in **Python**. Instead you use the "\*\*" operator,

.. code:: 

    2 ** 2

The *interpretter* allows to experiment with **Python** and get a feel for it. However, as previously mentioned, for this class, we will almost always be writing :ref:`python_scripts`.

To exit the *interpretter*, type and execute,

.. code:: python

    exit()

.. _python_scripts:

Scripts
=======

**Python** scripts are files that have a ``.py`` extension. ``.py`` files are just files containing plain text, but anything that ends in ``.py`` will be understood by the **Python** :ref:`python_interpretter` as a set of executable instrutions, so you can't write just any text in this file. You have to write words that exist in the `Python language <https://docs.python.org/3/reference/index.html>`_. Anytime we do a lab in this class, you will be writing a *script*. 

As an example, create a new file named ``test.py`` and open it in a text editor (actually, you will want to use :ref:`IDLE <python_idle>`, but we haven't gotten to that part yet, so any old text editor will do for now)

.. code:: python
 
    the_meaning_of_life = 42 
    print("The meaning of life is: ", the_meaning_of_life)

Save the file and open a *Linux* terminal (or command prompt if you are using your personal computer). Pass the name of the file to the **Python** interpretter and something magical will happen,

.. code:: shell 
 
    python test.py 

(INSERT SCREENSHOT)

Congratulations, you have just written your first Python script. In the labs for this class, when you are asked to create and run a **Python** script, this is essentially what you will be doing: 

    - creating a ``.py`` file
    - telling the **Python** interpretter your file name. 
    
However, *IDLE* will make this whole process much less painful, so continue onto the next section, dear reader. 

.. _python_idle:

IDLE
====

**Python** (usually) ships with a program named *IDLE*. `IDLE <https://docs.python.org/3/library/idle.html>`_ stands for *Integrated Development and Learning Environment*. *IDLE* is a text editor integrated with a **Python** interpretter. It provides `syntax highlighting <https://en.wikipedia.org/wiki/Syntax_highlighting#Support_in_text_editors>`_, the ability to save and execute scripts, and a debugger for stepping through the programs. In the immortal words of the poet laureate, Biz Markie, it's got what we need. 

Open up an *IDLE* session,

.. image:: ../../assets/imgs/python/idle_shell.png

This is another version of the **Python** interpretter we encountered a few sections ago, sometimes referred to as a `shell <https://en.wikipedia.org/wiki/Shell_(computing)>`_. You can execute the exact same commands in this *shell* as in the previous section, e.g.,

.. image:: ../../assets/imgs/python/idle_shell_command.png

If you navigate to the ``File > New File`` menu option in the top left corner to the *IDLE* shell (you may also hit the ``CTRL + N`` keys at the same time), it will open a text editor,

.. image:: ../../assets/imgs/python/idle_editor.png

You can type commands into this editor, as pictured. You can run these commands by navigating to the ``Run > Run Module`` menu option in the top left corner (you may also hit ``F5``). It will then prompt you to save the script, if you haven't already. After saving it, the *IDLE* shell will reappear with the results of your script,

.. image:: ../../assets/imgs/python/idle_editor_results.png

We will sometimes call the *IDLE* text editor a *notebook*. 

.. _python_packages:

Packages
========

By default, Python comes installed with the `Standard Library <https://docs.python.org/3/library/index.html>`_. The **Standard Library** is a collection of common functions and utilities. For instance, the `math` library is part of the **Standard Library**. `math` contains functions for computing trigonemtric ratios, generating random numbers, calculating powers and roots, etc. You can use `math` functions by first `import`-ing the library and accessing its content with *dot notation*. Start an interpretter session and type,

.. code:: python

    import math

    answer = math.factorial(20)
    print(answer)

This sequence of commands imports the `math` library, calls the factorial function with *dot notation* to compute :math:`n!`, stores the answer in the variable `answer`, and then prints it to screen.

.. _python_third_party:

Third-Party Packages
--------------------

`math` has plenty of functions that will be useful in this class, but it doesn't have *everything* we need. Luckily, **Python** ships with a *package manager* that allows you to install third-party libraries. You use the ``pip`` command anytime you need to install any additional libraries or pacakges into **Python**. Open up a Linux Terminal and type,

.. code:: shell
 
    pip --version 

You should see the version number print to screen. If you happen to see an error message that says something along the lines of "bash: pip command not found", then you will need to install ``pip`` from the *Linux* package repository with the following command,

.. code:: shell

    sudo apt-get install python3-pip

After this installation is complete, try verifying the ``pip`` version again, 

.. code:: shell 

    pip --version 

Now that you have ``pip``, we will need to install two additional packages for this class. `matplotlib <https://matplotlib.org/>`_ will be used to generate graphical representations of data. `tkinter <https://docs.python.org/3/library/tkinter.html>`_ will be used to render the output of `matplotlib <https://matplotlib.org/>`_ into JPEG and PNG images. These packages can be installed through the command line. Open the Linux terminal on your ChromeBook (or the command prompt on your personal computer),

.. code:: shell

    pip install matplotlib tk

See the :ref:`matplotlib` section to learn more about using *matplotlib* to generate plots of data.