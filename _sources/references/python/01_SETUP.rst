.. _python_setup:

============
Python Setup
============

**Python** will run on virtually any device with a processor. It supports all operating systems: Windows, Mac and Linux.

Python Installation
===================

ChromeOS
--------

1. Update 0S, if applicable,

(INSERT SCREENSHOT)

2. Enable and install Linux subsystem,

(INSERT SCREENSHOT)

3. Open command line terminal and verify installation,

(INSERT SCREENSHOT)

.. note:: 
    Pin the Linux terminal to your dock for quick access.

    (INSERT SCREENSHOT)

4. Install **Python** graphics library,
 
The following command is required to install PNG and JPEG rendering engines on your ChromeBook,

    sudo apt-get install python3-tk

(INSERT SCREENSHOT)

5. Install the **Python** package manager,

The following command is required to install the **Python** package manager,

    sudo apt-get install python3-pip

6. Install the **Python** editor,

The following command is required to the **Python** editor, **IDLE**,

    sudo apt-get install idle3

Congratulation, you are now setup to run **Python** scripts on your ChromeBook.

Interpretter
============

Once **Python** is installed, you will have access to the `python` command on the command prompt. Open a command prompt and verify your installation with the following command, 

    python --version

You can start an *interpretter* session with,

    python

This will bring up the **Python** *shell*, which allows you to enter commands and expression line by line. 

    > 5 + 7 # addition

You can also print text to screen with the `print()` function,

    > print("Hello world")

To exit the *interpretter*, use,

    > exit()

Packages
========

By default, Python comes installed with the `Standard Library <https://docs.python.org/3/library/index.html>`_. The **Standard Library** is a collection of common functions and utilities. For instance, the `math` library is part of the **Standard Library**. `math` contains functions for computing trigonemtric ratios, generating random numbers, calculating powers and roots, etc. You can use `math` functions by first `import`-ing the library and accessing its content with *dot notation*. Start an interpretter session and type,

    > import math
    > answer = math.factorial(20)
    > print(answer)

This sequence of commands imports the `math` library, calls the factorial function with *dot notation* to compute :math:`n!`, stores the answer in the variable `answer`, and then prints it to screen.

`math` has plenty of functions that will be useful in this class, but it doesn't have *everything* we need. Luckily, **Python** ships with a *package manager* that allows you to install third-party libraries.

We will need to install two additional packages for this class. `matplotlib <https://matplotlib.org/>`_ will be used to generate graphical representations of data. `tkinter <https://docs.python.org/3/library/tkinter.html>`_ will be used to render the output of `matplotlib <https://matplotlib.org/>`_ into JPEG and PNG images. These packages can be installed through the command line (*not* the **Python** interpretter),

    pip install matplotlib tk

See the :ref:`matplotlib` section to learn more about using *matplotlib* to generate plots of data.

IDLE
====

**Python** ships with a program named *IDLE*. `IDLE <https://docs.python.org/3/library/idle.html>`_ stands for *Integrated Development and Learning Environment*. 