.. _python_plotting:

=====
Plots
=====

We will be using **Python** to generate graphs. Lots and lots of graphs. So many graphs, you might say it's *graphic*. 

This section serves as a gallery for all the different sorts of graphs you can create with **Python**. However, before we get to that point, we need to make sure our computers are setup with graphing capabilities. If you followed along with the :ref:`python_setup` and completed all the steps on that page, you should be good to go. You may skip the next section in that case, or read through as a refresher (re-installing the graphics library won't break anything). 

By default, **Python** does not have statistical graphing capabilities. You must install two addition packages to supplement this deficiency, ``matplotlib`` and ``tk``. 

.. _python_plotting_prerequisites:

Prerequisites
=============

matplotlib
----------

``matplotlib`` is a versatile library for generating just about any sort of mathematical graph you can imagine. To install it, open up the Linux Terminal on your ChromeBook and type,

.. code:: shell

    pip3 install matplotlib

tkinter
-------

``tkinter``, or just ``tk``, is a library for processing the results of ``matplotlib`` into pretty JPEGs and PNGs. You can also install it through the Linux terminal, 

.. code:: shell 

    pip3 install tk

Now that we have everything we need, let's take a look at the various plots we can create. 

.. _python_plotting_imports:

Importing
=========

When you import ``matplotlib`` into your scripts, the very first thing you should do is *tell it to use the* ``tk`` *library* to create graphs.

.. code:: python

    import matplotlib

    matplotlib.use('tkagg')

This step is not, strictly speaking, necessary as most systems will default to using this library, but if you plots aren't showing up or you experience other weird errors, this is the likely culprit. In the event something goes wrong and you can't figure why, try adjusting this setting.

Creating the Axes
=================

To create a plot, we use the ``pyplot`` library. The ``subplots()`` function within the ``pyplot`` library will generate an *x-y* plane canvas, called the *axes*.

The following code will create a *figure* and a set of *axes* on which we can graph.

.. code:: python

    # note: the `as` gives the library a short-cut name we can use.
    import matplotlib.pyplot as plot 

    fig, axes = plot.subplots()

.. note:: 

    ``fig``, which stands for *figure*, is for drawing directly onto a 2D image using pixels. We will not use *figures* in this class to generate images. We are only interested in the ``axes``, which allow us to graph things in the *x-y* plane.

Labelling
---------

Titles
******

The following code adds a title to a plot,

.. code:: python 

    import matplotlib.pyplot as plot 

    fig, axes = plot.subplots()
    
    plot.suptitle("This is the Main Title") 

Subtitles
*********

The following code adds a subtitle to a plot, 

.. code:: python 

    import matplotlib.pyplot as plot

    fig, axes = plot.subplots()

    plot.title("This is the Sub Title")

Axes
****

The following code labels both the *x* and *y* axes in a plot,

.. code:: python 

    import matplotlib.pyplot as plot 

    fig, axes = plot.subplots()

    axes.set_xlabel("x units")
    axes.set_ylabel("y units")

Multiple Graphs
---------------

You can add multiple graphs to the same image by creating additional axes. You can create more axes by passing an argument into the ``subplots()`` function. 

When you pass in arguments to ``subplots``, it will return a *list* of axes. You can then access the individual axes by using their *index*,

.. code:: python

    import matplotlib.pyplot as plot

    # create two sets of axes 
    fig, axes = plot.subplots(1, 2)

    # plot the ordered pairs (4, 10) and (5, 11) on the first set of axes
    axes[0].scatter([4, 5], [10, 11])
    # plot the ordered pairs (-1, 5) and (2, -2) on the second set of axes
    axes[1].scatter([-1, 2], [5, -2])

.. note:: 

    The number of *axes* is the *second* argument of the ``subplots()`` function. We have to pass in a ``1`` first because **matplotlib.pyplot** always interprets the first argument as the number of *figures*.

Showing The Plot
================

Once you have plotted something on the ``axes``, you can display the plot with the ``show()`` function. 

This example will plot the ordered pairs :math:`(1, 8), (2, 9), (3, 7)`

.. code:: python

    import matplotlib.pyplot as plot

    fig, axes = plot.subplots()

    plot.title("Ordered Pairs")

    axes.scatter([1, 2, 3], [8, 9, 7])
    axes.set_xlabel("X units")
    axes.set_ylabel("Y units")

    plot.show()

Gallery
=======

You can download the scripts used to generate any of these examples by clicking on the "*source*" link in the top right corner of the image. 

Boxplot
-------

.. plot:: assets/plots/boxplots/boxplot_normal.py

Bar Chart
---------

.. plot:: assets/plots/other/bar_chart.py

Dot Plot
--------

.. plot:: assets/plots/other/dot_plot.py
    
Histogram
---------

.. plot:: assets/plots/histograms/histogram_normal.py

Ogives
------

.. plot:: assets/plots/ogives/ogive_normal.py

Scatterplot
-----------

.. plot:: assets/plots/scatterplots/scatterplot_no_correlation.py

Time Series
-----------

.. plot:: assets/plots/timeseries/timeseries_no_trend.py


References
==========

- `matplotlib documentation <https://matplotlib.org/>`_
- `matplotlib examples <https://matplotlib.org/stable/gallery/index>`_
- `matplotlib statistics examples <https://matplotlib.org/stable/gallery/statistics/index.html>`_
- `matplotlib histogram examples <https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py>`_
- `matplotlib ogive (cumulative distribution) examples <https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html#sphx-glr-gallery-statistics-histogram-cumulative-py>`_
- `matplotlib error bar examples <https://matplotlib.org/stable/gallery/statistics/errorbar.html#sphx-glr-gallery-statistics-errorbar-py>`_
- `matplotlib boxplot examples <https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-gallery-statistics-boxplot-demo-py>`_