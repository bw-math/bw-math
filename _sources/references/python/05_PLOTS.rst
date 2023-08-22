.. _python_plotting:

=====
Plots
=====

We will be using **Python** to generate graphs. Lots and lots of graphs. So many graphs, you might say it's *graphic*. 

This section serves as a gallery for all the different sorts of graphs you can create with **Python**. However, before we get to that point, we need to make sure our computers are setup with graphing capabilities. If you followed along with the :ref:`python_setup` and completed all the steps on that page, you should be good to go. You may skip the next section in that case, or read through as a refresher (re-installing the graphics library won't break anything). 

By default, **Python** does not have statistical graphing capabilities. You must install two addition packages to supplement this deficiency, ``matplotlib`` and ``tk``. 

Prerequisites
=============

matplotlib
----------

``matplotlib`` is a versatile library for generating just about any sort of mathematical graph you can imagine. To install it, open up the Linux Terminal on your ChromeBook and type,

.. code:: shell

    pip install matplotlib

tkinter
-------

``tkinter``, or just ``tk``, is a library for processing the results of ``matplotlib`` into pretty JPEGs and PNGs. You can also install it through the Linux terminal, 

.. code:: shell 

    pip install tk

Now that we have everything we need, let's take a look at the various plots we can create. 

Importing
=========

When you import ``matplotlib`` into your scripts, the very first thing you should always do is *tell it to use the* ``tk`` *library* to create graphs.

.. code:: python

    import matplotlib

    matplotlib.use('tkagg')

*Always, always, always* do this. If it's not clear by now, let's re-iterate: anytime you are using ``matplotlib`` you should *always* tell it to use ``tk``. Otherwise, you may encounter strange errors that make no sense. 

Gallery
=======

You can download the scripts used to generate any of these examples by clicking on the "*source*" link in the top right corner of the image. 

Boxplot
-------

.. plot:: assets/plots/boxplots/boxplot_normal.py

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

Error Bars
----------

TODO 

References
==========

- `matplotlib documentation <https://matplotlib.org/>`_
- `matplotlib examples <https://matplotlib.org/stable/gallery/index>`_
- `matplotlib statistics examples <https://matplotlib.org/stable/gallery/statistics/index.html>`_
- `matplotlib histogram examples <https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py>`_
- `matplotlib ogive (cumulative distribution) examples <https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html#sphx-glr-gallery-statistics-histogram-cumulative-py>`_
- `matplotlib error bar examples <https://matplotlib.org/stable/gallery/statistics/errorbar.html#sphx-glr-gallery-statistics-errorbar-py>`_
- `matplotlib boxplot examples <https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-gallery-statistics-boxplot-demo-py>`_