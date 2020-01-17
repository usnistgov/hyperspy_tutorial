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

   install_bundle
   install_anaconda
   coming_soon

===========================
ACMM 2020 HyperSpy workshop
===========================

..
    .. raw:: html
    
        <div class="text-center">
            <a  class="downloadbutton"
                href="https://github.com/usnistgov/hyperspy_tutorial/releases/download/2019_MandM_X15/hyperspy_tutorial.zip">
                    Click here to download<br/>the tutorial data (1.9 GB)
            </a>
        </div>
    
    |
    |

.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            >
                Download tutorial data (1.9 GB)<br/> <b>coming soon</b>
        </a>
    </div>

|
|

Thank you for registering for the 2020 ACMM HyperSpy workshop on data analysis 
in materials science.
This interactive tutorial session will introduce you to modern techniques of
data analysis for materials science and microscopy data within the scientific
Python environment, with time for questions and individual help.
The ultimate goal for the session is that by its end, each attendee feels
comfortable using HyperSpy for basic imaging and hyperspectral data analysis,
and knows where to look for further help, if necessary.

There are a few useful links in the top header of this page. The first
(`Tutorial Repository <https://github.com/ericpre/hyperspy_tutorial>`_)
will take you to the git repository containing the notebooks and data we will
use during the tutorial. The next two point to the HyperSpy
`Homepage <http://hyperspy.org>`_ and
`User Guide <http://hyperspy.org/hyperspy-doc/current/index.html>`__,
respectively. The homepage contains general information about the project as
a whole, while the User Guide is an extensive piece of documentation that explains
how to use HyperSpy for all sorts of analyses. Feel free to refer
to these links before and during the tutorial session for additional help.

Session Logistics
-----------------

.. cssclass:: table-bordered

    +--------------------+-------------------------------------------------+
    | **Date:**          | | Sunday 16th February                          |
    +--------------------+-------------------------------------------------+
    | **Time:**          | 9:00 AM - 5:00 PM PT                            |
    +--------------------+-------------------------------------------------+
    | **Location:**      | | Information coming soon                       |
    |                    | |                                               |
    +--------------------+-------------------------------------------------+

About the instructors
---------------------

.. table::

    +----------+---------------------------------------------------------------------+
    | |eric|   | | |eric_link| (EP) is a Lecturer in Materials Characterisation at   |
    |          |   the University of Manchester and the SuperSTEM Laboratory. His    |
    |          |   main areas of research focus on the development, implementation   |
    |          |   and application of new TEM methodologies - from specimen          |
    |          |   preparation, experimental workflow to advanced data processing    |
    |          |   and analysis - with the aim to uncover the                        |
    |          |   structure-property relationships of materials. He is an open      |
    |          |   source enthusiast, and started to use the HyperSpy                |
    |          |   library as a user during his PhD and made his first code          |
    |          |   contribution during his Post-Doc. He has since increased his      |
    |          |   contribution and commitment to the development of HyperSpy        |
    |          |   and is now a core developer.                                      |
    |          |   (Contact: eric.prestat@manchester.ac.uk)                          |
    +----------+---------------------------------------------------------------------+


.. |eric_link| replace:: `Eric Prestat <https://www.research.manchester.ac.uk/portal/en/researchers/eric-prestat(d6091419-ddb8-4164-9048-21fae9bb9074).html>`__
.. |eric| image:: _static/eric_prestat.jpg
   :width: 100%

Agenda
------

..  rst-class:: left-align-last-col
..  cssclass:: table-hover
..  table::
    :widths: 20 20 20 80

    +-------------------+------------+-----------+------------------------------------------------------+
    | Time              | Format     | Leader(s) | Topic                                                |
    +===================+============+===========+======================================================+
    | 09:00 - 09:15     | Talk       | EP        | Introduction to Python and HyperSpy                  |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 09:15 - 10:30     | Practical  | EP        | HyperSpy Basics                                      |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 10:30 - 11:00     |                        | *Coffee Break*                                       |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 11:00 - 11:45     | Practical  | EP        | Model Fitting                                        |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 11:45 - 12:30     | Practical  | EP        | EELS Analysis                                        |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 12:30 - 13:30     |            |           | *Lunch Break*                                        |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 13:30 - 13:45     | Talk       | EP        | Intro to Machine Learning in EM                      |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 13:45 - 14:15     | Practical  | EP        | Machine Learning                                     |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 14:15 - 15:00     | Practical  | EP        | EDS Analysis                                         |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 15:00 - 15:30     |                        | *Coffee Break*                                       |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 15:30 - 16:15     | Practical  | EP        | Big Data Analysis                                    |
    +-------------------+------------+-----------+------------------------------------------------------+
    | |                 | |          |  |        | | *Running in parallel, self-learning with provided* |
    | |                 | |          |  |        | | *notebooks and support from instructors:*          |
    | | 16:15 - 17:00   | | Practical|  | EP     | |   - Atomic resolution image analysis               |
    | |                 | |          |  |        | |   - Scanning electron diffraction analysis         |
    | |                 | |          |  |        | |   - Pixelated STEM / 4D STEM                       |
    +-------------------+------------+-----------+------------------------------------------------------+

-------------------------
Pre-tutorial instructions
-------------------------

Please review this section in advance of Sunday's tutorial session, as it
includes instructions for installing HyperSpy and the Jupyter interactive
computing environment.

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
-------------

No prior knowledge of Python is required for this workshop but a basic familiarity
with Python will be helpful. You will need to follow
the instructions below to install HyperSpy using either the Anaconda Python
distribution (Windows, Mac, or Linux), or the pre-compiled "bundle" installer
(only available on Windows).

Installation
------------

At its core, HyperSpy is a third-party library that exists as part of the
scientific greater Python ecosystem (as opposed to a stand-alone application).
Because of this, installation is slightly more tricky than a normal program,
but is not too difficult once you understand the steps required. The two pieces
required are a Python distribution (typically pre-installed on Mac and Linux;
but not included on by default on Windows), and then the HyperSpy libraries
that operate within that Python environment.

There are two possible approaches to getting a working HyperSpy environment. If
you are brand-new to Python and the command line in general (and you are running
Windows), we recommend using the pre-packaged
:doc:`"Bundle" Installer <../install_bundle>`.

For all other operating systems (and Windows, if you're a bit more comfortable
with Python and the command line), the recommended way to install HyperSpy is
using :doc:`Anaconda <../install_anaconda>`, due to its prevalence in the
scientific community and the ease of managing multiple Python "environments" on
one system. It also provides a uniform way of installing packages and managing
the system regardless of operating system, as well as up-to-date versions of
Python and library packages (often the "system" installation on Linux or Mac is
out of date). Anaconda can also be installed and run without administrative
privileges, meaning it can be used on remote systems easily regardless of
ownership.

Click one of the following buttons to view the specific installation
instructions for each method:

.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            href="install_bundle.html">
                "Bundle" installation <br/>instructions
        </a>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <a  class="downloadbutton"
            href="install_anaconda.html">
                Anaconda installation <br/>instructions
        </a>
    </div>

|
|

..  caution::
    It is important that you install HyperSpy using either the
    :doc:`"Bundle" Installer <../install_bundle>`, or through
    :doc:`Anaconda <../install_anaconda>` (*not both*!). Installing
    both can work, but will leave you with multiple Python installations on your
    system, and it will be very confusing to try to solve any issues that arise
    if you are not experienced with Python.

.. _getting-data:

Obtaining the tutorial data
---------------------------

The data will be available shortly before the workshop (most likely a couple of
days).

..
    Please click
    `this <https://github.com/usnistgov/hyperspy_tutorial/releases/download/2019_MandM_X15/hyperspy_tutorial.zip>`_
    link to download the tutorial notebooks and data as a ``.zip`` file
    (or click the `big green button <#>`_ at the top of this page). Due to the inclusion
    of some larger files, it is nearly 2.0 GB in size, so please ensure that you have
    enough disk space and bandwidth for the download. Once downloaded,
    extract the files into their own folder that is easily accessible. We recommend
    a folder in your user's home directory named ``hyperspy_tutorial``
    (i.e. ``C:\Users\<username>\hyperspy_tutorial`` on Windows).
    
    .. note::
       If you have limited disk space and/or internet availability, you can download
       a smaller version of the same data
       `here <https://github.com/usnistgov/hyperspy_tutorial/releases/download/2019_MandM_X15/hyperspy_tutorial_no_big_data.zip>`_.
       This archive is missing three large datasets, and so you will not be able to
       interactively participate in the *Big Data* and *pyXem* sessions. The
       remaining files are all the same.


Running the Jupyter Notebooks
-----------------------------

To actually open the Jupyter Notebooks containing the tutorials, you will need
to start a local Jupyter server and connect to it through your browser (don't
worry, everything stays local and there's no security risk to running the
notebook on ``localhost``).

If you installed using the bundle, this is very simple. Just open the Start Menu
and navigate to the "Jupyter Notebook" option within the "HyperSpy Bundle" folder:

.. figure:: _static/bundle_start_menu_notebook.png
   :width: 100 %
   :alt: Starting the notebook server from the bundle Start Menu
   :figwidth: 50%

   Starting the notebook server from the Start Menu shortcut installed in the
   bundle

If you installed with Anaconda, open the Anaconda Prompt (Windows) or a regular terminal
(macOS/Linux). From that prompt, use the ``cd`` command to change to the
directory that contains the tutorial notebooks and data that you downloaded
in the previous section. For example, if you saved the data into a folder named
``hyperspy_tutorial`` in your user folder, you would change to that folder with
one of the following commands:

..  code-block:: bash

    # For Windows:
    $ cd %USERPROFILE%\\hyperspy_tutorial

    # For macOS or Linux:
    $ cd ~/hyperspy_tutorial

Once in that folder, start the Jupyter Notebook server with the following
command:

..  code-block:: bash

    $ jupyter notebook

..  figure:: _static/anaconda_starting_jupyter.png
    :width: 100 %
    :alt: Starting the Jupyter Notebook on Windows
    :figwidth: 70%

    Starting the Jupyter Notebook from the ``hyperspy_tutorial`` folder on
    Windows

Regardless if you used the bundle or Anaconda, once you start the notebook "server",
it will automatically open a browser window (or new tab) to connect to the local server.
Make sure to leave the terminal window open in the background, as closing it will
shut down the notebook server. If everything has worked as expected, then you
will see a representation of the directory structure within ``hyperspy_tutorial``
on the Notebook homepage. If you do not, you can click through the file structure
displayed on the page to get to the correct folder:

..  figure:: _static/anaconda_creating_a_notebook.png
    :width: 100 %
    :alt: The notebook server home page
    :figwidth: 70%

    Click a folder name to browse into that folder, or a notebook name to open
    that file

..  figure:: _static/opening_getting_started_folder.png
    :width: 100 %
    :alt: Navigating to a folder
    :figwidth: 70%

    (For example) click the "02 HyperSpy basics" link to browse into that folder

Once inside one of the folders, simply click on any file with the extension
``.ipynb`` to open the notebook. The notebook will open in a new tab, and can
be interacted with as you need:


..  figure:: _static/opening_getting_started.png
    :width: 100 %
    :alt: Opening a notebook
    :figwidth: 70%

    Opening the "Getting Started" notebook within the "02 HyperSpy basics"
    folder

The original Jupyter "homepage" will stay open in the first tab, and you can
open as many notebooks as you wish at once (as long as you leave the terminal
window open in the background).

Congratulations! You should now be ready for the tutorial. If you ran into any
trouble, please try to arrive on Sunday morning a bit early, and one of the
instructors will be happy to help get you up and running.

------------
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
