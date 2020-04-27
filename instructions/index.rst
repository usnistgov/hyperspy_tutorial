..
    Build this document with the command:

    ```
    python -m sphinx.cmd.build ./ ../ -n -E -a -j auto -b html
    ```

    from the ./instructions directory and commit the build files to the
    ``nist-pages`` branch to build the public site at
    https://pages.nist.gov/hyperspy_tutorial

    Make sure to use sphinx-bootstrap-theme 0.6.5 (0.7.1 has a problem with
    sidebar styling)

:tocdepth: 4

.. toctree::
   :hidden:

   install_bundle_windows
   install_bundle_mac
   install_bundle_linux


2020 CCEM Workshop - HyperSpy
-----------------------------


.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            href="https://github.com/usnistgov/hyperspy_tutorial/releases/download/2020-04_CCEM_IP_Workshop/hyperspy_tutorial.zip">
                Click here to download<br/>the workshop data (22.4 MB)
        </a>
    </div>

|
|
 

Thank you for attending  the 2020 CCEM Image Processing workshop on using
HyperSpy for open source EELS data analysis.
This interactive workshop session will introduce you to modern techniques of
data analysis for materials science and microscopy data within the scientific
Python environment, with time for questions and individual help.
The ultimate goal for the session is that by its end, each attendee feels
comfortable using HyperSpy for basic imaging and hyperspectral data analysis,
and knows where to look for further help, if necessary.

There are a few useful links in the top header of this page. The first
(`Workshop Repository <https://github.com/usnistgov/hyperspy_tutorial>`_)
will take you to the git repository containing the notebooks and data we will
use during the tutorial. The next two point to the HyperSpy
`Homepage <http://hyperspy.org>`_ and
`User Guide <http://hyperspy.org/hyperspy-doc/current/index.html>`__,
respectively. The homepage contains general information about the project as
a whole, while the User Guide is an extensive piece of documentation that explains
how to use HyperSpy for all sorts of analyses. Feel free to refer
to these links before and during the workshop session for additional help.

Session Logistics
-----------------

.. table::
    :widths: auto

    +--------------------+-------------------------------------------------+
    | **Date:**          | | Friday May 1st, 2020                          |
    +--------------------+-------------------------------------------------+
    | **Time:**          | | 11:10 AM - 12:40 PM EDT (UTC-4h)              |
    +--------------------+-------------------------------------------------+
    | **Location:**      | | Online webinar                                |
    +--------------------+-------------------------------------------------+

About the instructor
--------------------

.. table::

    +----------+---------------------------------------------------------------------+
    | |josh|   | | |josh_link|  is a research engineer within the Office             |
    |          |   of Data and Informatics in the Material Measurement               |
    |          |   Laboratory at NIST, and has an extensive                          |
    |          |   background in materials science, microscopy, and data analysis    |
    |          |   utilizing machine learning, artificial intelligence, and          |
    |          |   state-of-the art signal processing techniques to facilitate       |
    |          |   greater understanding of material systems. He is a                |
    |          |   regular |contributor| to the upstream HyperSpy project and has    |
    |          |   been a user of the software for over 5 years.                     |
    |          |   (Contact: joshua.taillon@nist.gov)                                |
    +----------+---------------------------------------------------------------------+


.. |contributor| replace:: `contributor <https://github.com/hyperspy/hyperspy/commits?author=jat255>`__
.. |josh_link| replace:: `Josh Taillon <https://www.nist.gov/people/joshua-taillon>`__
.. |duncan_link| replace:: `Duncan Johnstone <https://www.emg.msm.cam.ac.uk/People/dnj23>`__
.. |kate_link| replace:: `Katherine MacArthur <http://www.er-c.org/metals/staff/macarthur.htm>`__
.. |magnus_link| replace:: `Magnus Nord <https://www.uantwerpen.be/en/staff/magnus-nord/>`__
.. |eric_link| replace:: `Eric Prestat <https://www.research.manchester.ac.uk/portal/en/researchers/eric-prestat(d6091419-ddb8-4164-9048-21fae9bb9074).html>`__
.. |josh| image:: _static/josh_taillon.jpg
   :width: 100%
.. |kate| image:: _static/kate_macarthur.jpg
   :width: 100%
.. |magnus| image:: _static/magnus_nord.png
   :width: 100%
.. |duncan| image:: _static/duncan_johnstone.jpg
   :width: 100%
.. |eric| image:: _static/eric_prestat.jpg
   :width: 100%

Agenda
------

..  cssclass:: table-hover
..  table::
    :widths: 30 80

    +-------------------+------------------------------------------------------+
    | Time              | Topic                                                |
    +===================+======================================================+
    | 11:10 - 11:40     | HyperSpy Basics                                      |
    +-------------------+------------------------------------------------------+
    | 11:40 - 12:40     | EELS Analysis                                        |
    +-------------------+------------------------------------------------------+


Pre-workshop instructions
-------------------------

Please review this section in advance of Friday's workshop session if you would
like to follow along interactively during the demonstration, as it includes
instructions for installing HyperSpy and the Jupyter interactive computing
environment.

..
    ..  admonition:: Installation alternatives

        While we encourage everyone to follow the instruction below to install
        HyperSpy locally on their personal system, we will also provide a web-based
        `JupyterHub`_ instance that can be used through a normal web browser,
        without installing anything to your system. If you choose to use this
        option, all you will need is a computer with a modern web browser (even a
        tablet with external keyboard should work). If you wish to use this option
        you will need a Google Account of some kind (either a NIST-administered one,
        which can be obtained
        `here <https://docs.google.com/forms/d/18vhcaRwq7MloEtz7-K75ZKKsGpgquhuVAteNkl5HTvg/viewform?edit_requested=true>`_
        or a personal account) for authentication purposes.

    ..  _JupyterHub: https://jupyterhub.readthedocs.io/en/stable/

Prerequisites
^^^^^^^^^^^^^

No prior knowledge of Python is required for this workshop but a basic familiarity
with Python will be helpful. You will need to follow
the instructions below to install HyperSpy using either the Anaconda Python
distribution (Windows, Mac, or Linux), or the pre-compiled "bundle" installer
(only available on Windows).

Installation
^^^^^^^^^^^^

At its core, HyperSpy is a third-party library that exists as part of the
greater scientific Python ecosystem (as opposed to a stand-alone application).
Because of this, installation is slightly more tricky than a normal program,
but is not too difficult once you understand the steps required. The two pieces
required are a Python distribution (typically pre-installed on Mac and Linux;
but not included on by default on Windows), and then the HyperSpy libraries
that operate within that Python environment. Even for systems (like macOS and Linux)
that have Python pre-installed, we recommend to use a separate Python
distribution for scientific data analysis installed through Anaconda, so that
there are no conflicts with the system version.

Select one of following instructions, depending on:

* If you are *not* already using an Anaconda Python distribution on your system:

.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            href="install_bundle_windows.html">
                Windows
        </a>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <a  class="downloadbutton"
            href="install_bundle_mac.html">
                Mac
        </a>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <a  class="downloadbutton"
            href="install_bundle_linux.html">
                Linux
        </a>
    </div>

|
|

* If you are already using a Miniconda or Anaconda distribution:

.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            href="http://hyperspy.org/hyperspy-doc/current/user_guide/install.html#quick-instructions-to-install-hyperspy-using-anaconda-linux-macos-windows">
                Installation in an existing <br/> Anaconda distribution
        </a>
    </div>

|
|

..  caution::
    It is important that you install HyperSpy using either the "Bundle" installer,
    or in an existing Python distribution (*not both!*). Installing
    both can work, but will leave you with multiple Python installations on your
    system, and it will be very confusing to try to solve any issues that arise
    if you are not experienced with Python.

.. _getting-data:

Obtaining the tutorial data
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            href="https://github.com/usnistgov/hyperspy_tutorial/releases/download/2020-04_CCEM_IP_Workshop/hyperspy_tutorial.zip">
                Click here to download<br/>the workshop data (22.4 MB)
        </a>
    </div>

|
|

Click the button above to download the files that will be used in the interactive
workshop. Once downloaded, extract the files into their own folder that is
easily accessible. We recommend a folder in your user's home directory named
``hyperspy_tutorial`` (i.e. ``C:\Users\<username>\hyperspy_tutorial`` on 
Windows).

.. note::

   If you have limited disk space and/or internet availability, you can download
   a smaller version of the same data
   `here <https://github.com/ericpre/hyperspy_tutorial/releases/download/2020_ACMM/hyperspy_tutorial_no_big_data.zip>`_.
   This archive is missing three large datasets, and so you will not be able to
   interactively participate in the *Big Data* and *pyXem* sessions. The
   remaining files are all the same.

Getting started
---------------

.. _start_jupyter:

Starting HyperSpy
^^^^^^^^^^^^^^^^^

HyperSpy is a Python library which can be used in different environments.
Typically, we use  `Jupyter <https://jupyter.org/>`_, which has three
different interfaces available:

* `Notebook <https://jupyter-notebook.readthedocs.io/en/stable/>`_
* `Qt Console <https://qtconsole.readthedocs.io/en/stable/>`_
* `JupyterLab <https://jupyterlab.readthedocs.io/en/stable/>`_

For this workshop, we'll be using the Notebook interface.
If you installed HyperSpy using the bundle, opening a Jupyter environment is very
simple: you will have a shortcut in
`the context menu <https://github.com/hyperspy/start_jupyter_cm>`_
(right click), which will open a Jupyter Notebook instance within this folder.
Make sure to right click on a folder, rather than an individual file, or the
shortcut will not appear.

.. list-table::

   * - .. figure:: _static/jupyter_cm_windows.png
          :height: 175 px

          Shortcut to start Jupyter from the current folder
          on Windows.
    
     - .. figure:: _static/jupyter_cm_macos.png
    
          Shortcut to start Jupyter from the current folder
          on macOS.

     - .. figure:: _static/jupyter_cm_gnome.png
    
          Shortcut to start Jupyter from the current folder
          on Linux with a Gnome desktop.

On Windows, you can also use the shortcut in the Start Menu to start Jupyter
in your user folder.

.. figure:: _static/windows_start_menu_notebook_labels.png
   :width: 100 %
   :alt: Starting Jupyter from the Start Menu
   :figwidth: 30%

   Starting the notebook server from the start menu shortcut.

Then you can import HyperSpy by executing in a notebook cell or in the Qt
Console:

..  code-block:: python

    %matplotlib qt
    import hyperspy.api as hs

It may worth checking that your install is running correctly by following the
instructions in the the :ref:`test_install_label` section.

Opening the workshop notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the workshop, we will use notebooks which can be run using the 
``jupyter notebook`` or the ``jupyter lab``. The simplest is to use the shortcut
in the context menu as explained above in the :ref:`start_jupyter` section.

Alternatively, you can open a terminal (on Windows, start the `Anaconda Prompt`
program from your Start Menu) and
navigate to the folder containing the workshop data by using the ``cd`` command.
For example, if you saved the data into a folder named ``hyperspy_tutorial`` 
in your user folder, you would change to that folder with a command such as:

..  code-block:: bash

    $ cd ~/hyperspy_tutorial

Once in that folder, start the Jupyter Notebook server with the following
command:

..  code-block:: bash

    $ jupyter notebook

Once you start the notebook "server", a browser window (or new tab) will 
automatically open to connect to the local server. If it does not automatically
open, the link to connect to the server will also be displayed in your terminal.

.. note::

   While we use the term "server", the Jupyter software runs only on your
   local machine, and cannot (by default) be connected to from any other location.
   Internet connectivity is not required to run the software, even though
   you access it through the web browser.

Make sure to leave the terminal window open in the background, as closing it will
shut down the notebook server. If everything has worked as expected, then you
will see a representation of the directory structure within ``hyperspy_tutorial``
on the Notebook homepage. If you do not, you can click through the file structure
displayed on the page to get to the correct folder:

..  figure:: _static/notebook_folder_labels.png
    :width: 100 %
    :alt: The notebook server home page
    :figwidth: 70%

    Click a folder name to browse into that folder, or a notebook name to open
    that file

Once inside one of the folders, simply click on any file with the extension
``.ipynb`` to open the notebook. The notebook will open in a new tab, and can
be interacted with as you need:


..  figure:: _static/notebook_open_labels.png
    :width: 100 %
    :alt: Opening a notebook
    :figwidth: 70%

    Opening the "Getting Started" notebook within the "01 HyperSpy basics"
    folder

The original Jupyter "homepage" will stay open in the first tab, and you can
open as many notebooks as you wish at once (as long as you leave the terminal
window open in the background).

Congratulations! You should now be ready for the tutorial. If you ran into any
trouble, please `contact Josh <mailto:joshua.taillon@nist.gov>`_ prior to the
workshop, and he'll help get you up and running.


Getting Help
------------

In addition to the links in the header of this page, there are a few additional
resources that can be used to get help with questions you may have about using
the software. The `support <http://hyperspy.org/support.html>`_ page for the
project highlights the best avenues for help, but briefly they are:

- The HyperSpy `User Guide <http://hyperspy.org/hyperspy-doc/current/index.html>`_
- The HyperSpy `user mailing list <https://groups.google.com/forum/#!forum/hyperspy-users>`_
- The interactive `Gitter chat room <https://gitter.im/hyperspy/hyperspy>`_
- The `issue/bug tracker <https://github.com/hyperspy/hyperspy/issues>`_ on the HyperSpy Github page
- The `HyperSpy Demos <https://github.com/hyperspy/hyperspy-demos/>`_ repository, which contains the foundations of the notebooks presented in this tutorial, together with some additional demos

|
|
