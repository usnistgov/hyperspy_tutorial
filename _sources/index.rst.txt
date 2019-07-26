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

.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            href="https://github.com/usnistgov/hyperspy_tutorial/archive/2019-MandM.zip">
                Click here to download<br/>the tutorial data
        </a>
    </div>


==================================
2019 M&M Sunday Short Course X-15:
==================================

----------------------------------
Data Analysis in Materials Science
----------------------------------

Thank you for registering for the 2019 Microscopy and Microanalysis short course
on data analysis in materials science, presented by the developers of HyperSpy.
This interactive tutorial session will introduce you to modern techniques of
data analysis for materials science and microscopy data within the scientific
Python environment, with plenty of time for questions and individual help.
The ultimate goal for the session is that by its end, each attendee feels
comfortable using HyperSpy for basic imaging and hyperspectral data analysis,
and knows where to look for further help, if necessary.

There are a few useful links in the top header of this page. The first
(`Tutorial Repository <https://github.com/usnistgov/hyperspy_tutorial>`_)
will take you to the git repository containing the notebooks and data we will
use during the tutorial. The next two point to the HyperSpy
`Homepage <http://hyperspy.org>`_ and
`User Guide <http://hyperspy.org/hyperspy-doc/current/user_guide/index.html>`_,
respectively. The homepage contains general information about the project as
a whole, while the User Guide is an extensive piece of documentation that explains
how to use HyperSpy for all sorts of analyses. Feel free to refer
to these links before and during the tutorial session for additional help.

Session Logistics
-----------------

.. cssclass:: table-bordered

    +--------------------+-------------------------------------------------+
    | **Date:**          | | Sunday August 4, 2019                         |
    +--------------------+-------------------------------------------------+
    | **Time:**          | 8:30 AM - 5:30 PM PT                            |
    +--------------------+-------------------------------------------------+
    | **Location:**      | | Oregon Convention Center - Portland, OR       |
    |                    | | (Room B118-119)                               |
    +--------------------+-------------------------------------------------+

About the instructors
---------------------

.. table::

    +----------+---------------------------------------------------------------------+
    | |duncan| | | |duncan_link| (DJ) is a Research Associate in the Electron        |
    |          |   Microscopy Group of the Department of Materials Science &         |
    |          |   Metallurgy, University of Cambridge, UK. His work focuses on      |
    |          |   developing materials characterization approaches based on         |
    |          |   electron diffraction and is currently particularly interested     |
    |          |   in determining structure on the nanoscale in soft materials.      |
    |          |   He leads the development of the ``pyxem`` python package for      |
    |          |   the analysis of scanning diffraction data in which                |
    |          |   diffraction patterns are acquired at every probe position         |
    |          |   across a specimen. The ``pyxem`` package builds on HyperSpy       |
    |          |   and he has made contributions to HyperSpy to enable that          |
    |          |   dependence. (Contact: dnj23@cam.ac.uk)                            |
    +----------+---------------------------------------------------------------------+
    | |kate|   | | |kate_link| (KM) is a postdoctoral researcher at the Ernst        |
    |          |   Ruska Centre for Microscopy and Spectroscopy in the Helmholtz     |
    |          |   funded Research Centre Jülich, Germany. She completed her PhD     |
    |          |   at Oxford University in 2015 on quantitative EDX and HAADF        |
    |          |   STEM. She has interests in Materials Science, spectroscopy and    |
    |          |   microscopy analysis in a quantitative manner. Katherine got       |
    |          |   involved with HyperSpy development three years ago with the       |
    |          |   aim of automating her quantitative EDX analysis method.           |
    |          |   She has since expanded her contributions to more general          |
    |          |   data analysis functions and methods, with the interest of         |
    |          |   working towards automated analysis of in-situ spectroscopic       |
    |          |   data. (Contact: k.macarthur@fz-juelich.de)                        |
    +----------+---------------------------------------------------------------------+
    | |magnus| | | |magnus_link| (MN) is a Marie Curie fellow at Electron Microscopy |
    |          |   for Materials research (EMAT) at University of Antwerp,           |
    |          |   Belgium. He obtained his PhD at the Norwegian University of       |
    |          |   Science and Technology working on advanced analysis of both       |
    |          |   EELS and atomic resolution STEM data. The former resulting        |
    |          |   in many contributions to HyperSpy, and the latter in the          |
    |          |   creation of the Atomap Python library. His current research       |
    |          |   interests revolves around utilizing fast pixelated detectors      |
    |          |   in STEM with the ``pixStem`` library, to study both magnetic      |
    |          |   and structural properties at the nanoscale.                       |
    |          |   (Contact: magnus.nord@uantwerpen.be)                              |
    +----------+---------------------------------------------------------------------+
    | |eric|   | | |eric_link| (EP) is a person that does microscopy.                |
    +----------+---------------------------------------------------------------------+
    | |josh|   | | |josh_link| (JT) is a research engineer within the Office         |
    |          |   of Data and Informatics in the Material Measurement               |
    |          |   Laboratory at NIST, and has an extensive                          |
    |          |   background in materials science, microscopy, and data analysis    |
    |          |   utilizing machine learning, artificial intelligence, and          |
    |          |   state-of-the art signal processing techniques to facilitate       |
    |          |   greater understanding of material systems. He is a (fairly)       |
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

..  rst-class:: left-align-last-col
..  cssclass:: table-hover
..  table::
    :widths: 20 20 20 80

    +-------------------+------------+-----------+------------------------------------------------------+
    | Time              | Format     | Leader(s) | Topic                                                |
    +===================+============+===========+======================================================+
    | 08:30 - 09:00     | Talk       | JT        | Introduction to Python and HyperSpy                  |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 09:00 - 10:30     | Practical  | EP        | HyperSpy Basics                                      |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 10:30 - 10:45     |                        | *Coffee Break*                                       |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 10:45 - 11:30     | Practical  | DJ        | Model Fitting                                        |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 11:30 - 12:15     | Practical  | MN        | EELS Analysis                                        |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 12:15 - 13:15     |            |           | *Lunch Break*                                        |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 13:15 - 13:30     | Talk       | JT        | Intro to Machine Learning in EM                      |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 13:30 - 14:00     | Practical  | JT        | Machine Learning                                     |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 14:00 - 15:00     | Practical  | KM        | EDS Analysis                                         |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 15:00 - 15:15     |                        | *Coffee Break*                                       |
    +-------------------+------------+-----------+------------------------------------------------------+
    | 15:15 - 16:00     | Practical  | EP        | Big Data Analysis                                    |
    +-------------------+------------+-----------+------------------------------------------------------+
    | |                 | |          |  |        | | *Running in parallel, self-learning with provided* |
    | |                 | |          |  |        | | *notebooks and support from instructors:*          |
    | | 16:00 - 17:30   | | Practical|  | MN/KM  | |   - Atomic resolution image analysis               |
    | |                 | |          |  | DJ     | |   - Scanning electron diffraction analysis         |
    | |                 | |          |  | MN     | |   - Pixelated STEM / 4D STEM                       |
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

For participation in the session, a basic familiarity with Python and command
line tools will be helpful, but not strictly required. You will need to follow
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
Windows), we recommend using the pre-packaged `"Bundle" Installer`_.

For all other operating systems (and Windows, if you're a bit more comfortable
with Python and the command line), the recommended way to install HyperSpy is using
`Anaconda`_, due to its prevalence in the scientific community and the
ease of managing multiple Python "environments" on one system. It also provides
a uniform way of installing packages and managing the system regardless of
operating system, as well as up-to-date versions of Python and library
packages (often the "system" installation on Linux or Mac is out of date).
Anaconda can also be installed and run without administrative privileges,
meaning it can be used on remote systems easily regardless of ownership.

..  _Anaconda Python: https://www.anaconda.com/distribution

..  warning::
    It is important that you install HyperSpy using either the
    `"Bundle" Installer`_, or through `Anaconda`_ (and *not both*!). Installing
    both will leave you with multiple Python installations on your system, and
    it will be very confusing to try to solve any issues that arise.


"Bundle" Installer
~~~~~~~~~~~~~~~~~~

If you are running on Windows, the easiest way to install HyperSpy is using
the "standalone" bundle package. This simple to install program provides a
customized Python installation that has the HyperSpy libraries pre-installed.
Instructions can be found at from the HyperSpy Bundle Github repository
(`here <https://github.com/hyperspy/hyperspy-bundle>`_), and a detailed walk
through of the process is provided below.

First, navigate to the repository home page
(https://github.com/hyperspy/hyperspy-bundle), and click on the large green
button slightly down the page:

.. figure:: _static/bundle_install_button.png
   :width: 100 %
   :alt: Link to Windows download for standalone HyperSpy bundle
   :figwidth: 70%

   Clicking the big green button on the main repository page will bring you to
   the "Releases" page that contains a link to the ``.exe`` installation file

On the releases page, click on the appropriate installer for your system (most
likely you will want the 64-bit version):

.. figure:: _static/bundle_release_download.png
   :width: 100 %
   :alt: Links HyperSpy bundle downloads
   :figwidth: 70%

   Most modern systems will need the "64-bit" version, but some older machines
   may still use the 32-bit option

After the download finishes, run the ``.exe`` file, accepting the default options.
Doing so will install HyperSpy into your user folder under a subfolder named
``"HyperSpy Bundle"``. The installation may take some time, but you should get
a progress window that looks like:

.. figure:: _static/bundle_during_installation.png
   :width: 100 %
   :alt: Bundle installation progress
   :figwidth: 50%

   A screenshot during the bundle installation process

Once the installation finishes, click the *Next* button, and then *Finish* to
exit the installer. A command prompt window might open to pre-compile the included
libraries. This will only happen once, and speeds up the code when it comes time
to run any Python scripts. Wait for the process to finish, and the window should
close on its own:

.. figure:: _static/bundle_compiling.png
   :width: 100 %
   :alt: Pre-compiling the included Python libraries
   :figwidth: 70%

   The last step of the installation is pre-compilation of the included Python
   libraries. This only happens one time, so please wait for it to finish. The
   command window should close itself when it is done.

And that's it! All the installed programs should now be available within the
Start Menu under the "HyperSpy Bundle" folder. You should now continue to the
`Obtaining the tutorial data`_ section (skipping the `Anaconda`_ section).

Anaconda
~~~~~~~~

Installing HyperSpy with Anaconda is slightly more involved, but provides more
flexibility if you plan to do more development with Python, or need to run many
different Python programs on your machine alongside each other.

While it is mostly unattended, the download and installation of Anaconda can
take a fair amount of time (approximately 10 to 15 minutes, depending on the
speed of your system), so it is highly recommended to do this before you
arrive at the tutorial session (and when you have access to a decent internet
connection).

Download
^^^^^^^^

The installation process for Anaconda varies a bit depending on your operating
system. Instructions for Windows are detailed here. MacOS will be somewhat similar,
while if you run Linux, you will need to use the command line installer (an
exercise left to the reader). From the `Anaconda Python`_ link, click the
selector for your operating system, and then click the big green download button
for the "Python 3.7 version":

.. figure:: _static/anaconda_download_link.png
   :width: 100 %
   :alt: Link to Windows download for Anaconda
   :figwidth: 70%

   Make sure to select the 64-bit 3.7 graphical installer (the green button
   should get you the right version) - It's a rather large download, so a decent
   connection is recommended

Installing Anaconda
^^^^^^^^^^^^^^^^^^^

Detailed instructions for
`Windows <https://docs.anaconda.com/anaconda/install/windows/>`_,
`macOS <https://docs.anaconda.com/anaconda/install/mac-os/>`_, and
`Linux <https://docs.anaconda.com/anaconda/install/linux/>`_ are available on
the Anaconda website. Specific instructions for Windows are reproduced below.

Run the downloaded file to proceed with the installation. This process is fairly
straightforward. For the installation location, we recommend an easily accessed
path that does not require administrative rights, such as the folder
``anaconda3`` within your user directory:

.. figure:: _static/anaconda_installation_path.png
   :width: 100 %
   :alt: Anaconda installation path
   :figwidth: 50%

   This path can be whatever you want (where you have write access), but
   a subfolder in the user directory is usually a convenient location - the
   default option is also fine

The next screen will present you with options about adding Anaconda to the
system ``PATH`` variable, and whether or not you want this installation to
be registered as the "default" Python installation on your system (via a
key saved to the registry on Windows). We recommend the default options (as
shown below), but if you have other Python installations on your system, you may
want to uncheck the "Register as default" option:

..  figure:: _static/anaconda_PATH_options.png
    :width: 100 %
    :alt: Installation options
    :figwidth: 50%

    Specifying configuration settings for the Anaconda installation on Windows

Click the "Install" button at this point, and go to get a coffee or tea (or go
for a walk), as the installation process takes some time depending on your disk
speed.

..  figure:: _static/anaconda_install_complete.png
    :width: 100 %
    :alt: Installation complete
    :figwidth: 50%

    The "Installation complete" screen after installing Anaconda on Windows

Once the installation completes, click the "Next" button to continue and then
"Finish" to exit the installer.

Usage
^^^^^

After Anaconda is installed, we suggest taking a look at the
"`Getting Started`_" guide from its documentation to familiarize yourself with
how Anaconda is used. There are a few ways to interact with Anaconda, primarily
through either the "navigator" application, or on the command line. One of the
most powerful features of Anaconda is the ``conda`` environment and package
manager, which allows you to create multiple different "installations" (known as
`environments`) of Python, enabling you to select which version of Python is
used for each environment and what packages are installed inside that
environment. A common setup is to have one environment for each project or
application you are working with. For this tutorial however, we will install
HyperSpy into the ``base`` (the default) environment (for ease of use) using
the command line.

..  _Getting Started: https://docs.anaconda.com/anaconda/user-guide/getting-started/


Installing HyperSpy with Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Like for Anaconda, detailed installation instructions for HyperSpy are
available directly from its `documentation <http://hyperspy.org/hyperspy-doc/current/user_guide/install.html#quick-instructions-to-install-hyperspy-using-anaconda-linux-macos-windows>`_.
The process will also be summarized here with a bit more instruction.

..  admonition:: Info about code blocks

    In the following section, lines in code blocks will be prefaced with ``$``
    or ``>>>``. ``$`` is used to indicate regular terminal input, while ``>>>``
    represents inputs to the Python interpreter (accessed by running ``python``
    from the regular command line. Any lines without these symbols
    indicate the expected output of the given command. To run the
    commands provided, copy everything after the ``$`` or ``>>>`` character into
    your terminal. Where necessary, commands will be given for both the Windows
    Anaconda prompt and the macOS/Linux terminal, so only use the commands
    specific to your operating system.

From the Start Menu (on Windows), open the `Anaconda Prompt`:

..  figure:: _static/anaconda_post_install.png
    :width: 100 %
    :alt: Windows programs installed by Anaconda
    :figwidth: 30%

    Windows programs installed by Anaconda

On Mac or Linux, open a terminal as normal. If during installation you told
the installer to "initialize" Anaconda3, all the ``conda`` commands should
be immediately available. If not, you will have to run the following, replacing
the bracketed term with the actual path in which you installed Anaconda:

..  code-block:: bash

    $ source <ANACONDA_INSTALL_PATH>/bin/activate

before any of the ``conda`` commands will work. Again, `this is only for
Mac/Linux`, the commands should be available with no problem on Windows when
you launch the `Anaconda Prompt`.

From the prompt, run the following to install HyperSpy, its UI package, and its
dependencies:

..  code-block:: bash

    $ conda install -c conda-forge hyperspy hyperspyui

After Anaconda calculates the dependencies it will need to install, it will ask
for confirmation to continue. Press ``Enter`` to accept the changes, and wait
for the requested libraries to be installed. Once the install is completed,
you can check that it was successful by starting the Python interpreter (run
the ``python`` command) and entering:

..  code-block:: python

    >>> import hyperspy.api as hs

If this returns to the Python prompt (which looks like ``>>>``) without error
(it may take a few moments the first time you run this command if your machine
is not too powerful), then the installation was successful and you should be
all set to use HyperSpy. Press ``Ctrl-D`` to exit the Python interpreter and
return back to the Anaconda Prompt.

..
    HyperSpyUI
    ^^^^^^^^^^

    While most HyperSpy users find Jupyter Notebooks and the programmatic interface
    to be the best for reproducible analyses, there is a graphical user interface
    available that can accomplish a number of tasks and allow you to quickly browse
    through multiple data files.

    To start the user interface, run the command ``hyperspyui`` from the Anaconda
    Prompt after the installation from the previous step is complete.


Obtaining the tutorial data
---------------------------

Please click `this <https://github.com/usnistgov/hyperspy_tutorial/archive/2019-MandM.zip>`_
link to download the tutorial notebooks and data as a ``.zip`` file
(or click the big green button at the top of this page). Once downloaded, extract
the files into their own folder that is easily accessible. We recommend a folder
in your user's home directory named``hyperspy_tutorial``
(i.e. ``C:\Users\username\hyperspy_tutorial`` on Windows).


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
    $ cd ~/Desktop/hyperspy_tutorial

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
displayed on the page to get to the correct folder. To create a new notebook,
you can click the `New` button, and then specify the `Python 3` kernel:

..  figure:: _static/anaconda_creating_a_notebook.png
    :width: 100 %
    :alt: Creating a notebook in the Jupyter Server on Windows
    :figwidth: 70%

    Click the highlighted locations to open a new notebook in the Jupyter Server

Otherwise, to open the notebook files you downloaded earlier, just
click on any file with the extension ``.ipynb``. The notebook will open in a new
tab, and can be interacted with as you need. The original Jupyter "homepage" will
stay open, and you can open as many notebooks as you wish at once (as long as you
leave the terminal window open in the background).

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
