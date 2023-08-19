.. _python_setup:

============
Python Setup
============

**Python** will run on virtually any device with a processor. It supports all operating systems: Windows, Mac and Linux.

Python Installation
===================

ChromeOS
--------

1. Update your Chrome0S, if applicable,

(INSERT SCREENSHOT)

2. Enable and install Linux subsystem,

(INSERT SCREENSHOT)

3. Open Linux terminal and verify installation with the command,
   
.. code:: shell

    python --version

(INSERT SCREENSHOT)

.. note:: 

    Pin the Linux terminal to your dock for quick access.

    (INSERT SCREENSHOT)

1. Install **Python** graphics library,
 
The following command is required to install PNG and JPEG rendering engines on your ChromeBook,

.. code:: shell 

    sudo apt-get install python3-tk

(INSERT SCREENSHOT)

5. Install the **Python** package manager,

The following command is required to install the **Python** package manager,

.. code:: shell

    sudo apt-get install python3-pip

6. Install the **Python** editor,

The following command is required to the **Python** editor, **IDLE**,

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

Once **Python** is installed, you will have access to the `python` command on the command prompt. Open a command prompt and verify your installation with the following command, 

.. code:: shell
    
    python --version

You can start an *interpretter* session with,

.. code:: shell

    python

This will bring up the **Python** *shell*, which allows you to enter commands and expression line by line. **Python** *interprets* your commands after you type ``ENTER``.
For example, type the following arithmetical expression and then type ``ENTER`` to execute it. 

.. code:: python

    5 + 7

You can also print text to screen with the `print()` function,

.. code:: python

    print("Hello world")

We won't use the *interpretter* much in this class, but it is a handy tool to quickly check if a expression you had in mind is syntactical. For example, you might want to square a number and try,

.. code:: 

    2 ^ 2

However, this is not how you raise a number to a power in **Python**. Instead you use the "\*\*" operator,

.. code:: 

    2 ** 2

The *interpretter* allows to experiment with **Python** and get a feel for it. However, for this class, we will almost always be writing :ref:`python_scripts`.

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

Save the file and open a Linux terminal (or command prompt if you are using your personal computer). Pass the name of the file to the **Python** interpretter and something magical will happen,

.. code:: shell 
 
    python test.py 

Congratulations, you have just written your first Python script. In the labs, when you are asked to create and run a **Python** script, this is essentially what you will be doing: 

    - create a ``.py`` file
    - tell the **Python** interpretter your file name. 
    
However, *IDLE* will make this whole process much less painful, so continue onto the next section, dear reader. 

.. _python_idle:

IDLE
====

**Python** (usually) ships with a program named *IDLE*. `IDLE <https://docs.python.org/3/library/idle.html>`_ stands for *Integrated Development and Learning Environment*. *IDLE* is a text editor integrated with a **Python** interpretter. It provides `syntax highlighting <https://en.wikipedia.org/wiki/Syntax_highlighting#Support_in_text_editors>`_, the ability to save and execute scripts, and a debugger for stepping through the programs. Open up an *IDLE* session,

.. image:: ../../assets/imgs/python/idle_shell.png

This is another version of the **Python** interpretter we encountered a few sections ago, sometimes referred to as a `shell <https://en.wikipedia.org/wiki/Shell_(computing)>`_. You can execute the exact same commands in this *shell* as in the previous section, e.g.,

.. image:: ../../assets/imgs/python/idle_shell_command.png

If you navigate to the ``File > New File`` menu option in the top left corner to the *IDLE* shell (you may also hit the ``CTRL + N`` keys at the same time), it will open a text editor,

.. image:: ../../assets/imgs/python/idle_editor.png

You can type commands into this editor, as pictured. You can run these commands by navigating to the ``Run > Run Module`` menu option in the top left corner (you may also hit ``F5``). It will then prompt you to save the script, if you haven't already. After saving it, the *IDLE* shell will reappear with the results of your script,

.. image:: ../../assets/imgs/python/idle_editor_results.png

While you can complete all the labs in this class in Notepad if you so choose, all examples in class will us the *IDLE* shell and text editor. 

.. _python_packages:

Packages
========

By default, Python comes installed with the `Standard Library <https://docs.python.org/3/library/index.html>`_. The **Standard Library** is a collection of common functions and utilities. For instance, the `math` library is part of the **Standard Library**. `math` contains functions for computing trigonemtric ratios, generating random numbers, calculating powers and roots, etc. You can use `math` functions by first `import`-ing the library and accessing its content with *dot notation*. Start an interpretter session and type,

.. code:: python

    import math

    answer = math.factorial(20)
    print(answer)

This sequence of commands imports the `math` library, calls the factorial function with *dot notation* to compute :math:`n!`, stores the answer in the variable `answer`, and then prints it to screen.

`math` has plenty of functions that will be useful in this class, but it doesn't have *everything* we need. Luckily, **Python** ships with a *package manager* that allows you to install third-party libraries.

We will need to install two additional packages for this class. `matplotlib <https://matplotlib.org/>`_ will be used to generate graphical representations of data. `tkinter <https://docs.python.org/3/library/tkinter.html>`_ will be used to render the output of `matplotlib <https://matplotlib.org/>`_ into JPEG and PNG images. These packages can be installed through the command line (*not* the **Python** interpretter). Open the Linux terminal on your ChromeBook (or the command prompt on your personal computer),

.. code:: shell

    pip install matplotlib tk

See the :ref:`matplotlib` section to learn more about using *matplotlib* to generate plots of data.