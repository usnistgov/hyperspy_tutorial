2019 NIST HyperSpy Tutorial
===========================

About the session
+++++++++++++++++

Thank you for registering for the NIST ODI-MMSD tutorial session on HyperSpy!
This informal tutorial session will introduce you to the capabilities of
HyperSpy in a casual and interactive environment, with plenty of time allocated
for questions and individual help. The goal for the session is that by the end
each attendee feels comfortable using HyperSpy for basic hyperspectral data
analysis, and knows where to look for further help, if necessary.

Event details
-------------

.. cssclass:: table-bordered

    +--------------------+-------------------------------------------------+
    | **Date:**          | Friday May 10, 2019                             |
    +--------------------+-------------------------------------------------+
    | **Time:**          | 8:30 AM - 12:30 PM ET                           |
    +--------------------+-------------------------------------------------+
    | **Location:**      | | *Gaithersburg*: Building 101 - Lecture Room C |
    |                    | | *Boulder*: Building 2 - Room 0113 (VTC)       |
    +--------------------+-------------------------------------------------+

About the instructors
---------------------

.. table::

    +---------+-----------------------------------------------------------------+
    | |josh|  | | |josh_link| is a research engineer within the Office          |
    |         |   of Data and Informatics (MML), and has an extensive           |
    |         |   background in materials science, microscopy, and data analysis|
    |         |   utilizing machine learning, artificial intelligence, and      |
    |         |   state-of-the art signal processing techniques to facilitate   |
    |         |   greater understanding of material systems. He is a (fairly)   |
    |         |   regular |contributor| to the upstream HyperSpy project and has|
    |         |   been a user of the software for over 5 years.                 |
    +---------+-----------------------------------------------------------------+
    | |andy|  | | |andy_link| is a staff scientist in the Materials             |
    |         |   Structure and Data Group of the Materials Measurement Science |
    |         |   Division (MML) and is an expert in the quantitative structural|
    |         |   and chemical characterization of small volumes of material    |
    |         |   using electron microscopy techniques. He has used (and        |
    |         |   extended) HyperSpy to enable reproducible and well-documented |
    |         |   data  analysis for objectively processing chemical tomography |
    |         |   data based on hyperspectral images in the TEM.                |
    +---------+-----------------------------------------------------------------+

.. |contributor| replace:: `contributor <https://github.com/hyperspy/hyperspy/commits?author=jat255>`__
.. |josh_link| replace:: `Josh Taillon <https://www.nist.gov/people/joshua-taillon>`__
.. |andy_link| replace:: `Andy Herzing <https://www.nist.gov/people/andrew-herzing>`__
.. |josh| image:: _static/josh_taillon.jpg
   :width: 100%
.. |andy| image:: _static/andy_herzing.jpg
   :width: 100%

(Rough) Agenda
--------------

..  rst-class:: left-align-last-col
.. cssclass:: table-hover
..  table:: *Times are tentative and subject to adjustment during the day to meet the needs of the audience*
    :widths: 20 80

    ==================  ============
    Time                Topic
    ==================  ============
    8:00 - 8:30 AM      (*Optional*) Pre-tutorial time; instructors will be in the room to answer any specific setup questions, debugging, etc.
    8:30 - 8:45 AM      Welcome and introductions
    8:45 - 9:15 AM      *Getting Started with HyperSpy* - Basics of using a Jupyter notebook and operating on HyperSpy Signals
    9:15 - 10:00 AM     *Curve Fitting* - Introduction to Signal modeling and fitting in HyperSpy
    10:00 - 10:15 AM    *Using HyperSpyUI* - For simpler point-and-click analyses
    *10:15 - 10:30 AM*  *Short break / time for questions*
    10:30 - 11:00 AM    *Unsupervised learning & EDS Analysis* - Example analysis of TEM data from core-shell nanoparticles
    11:00 - 11:30 AM    *EELS Analysis in HyperSpy* - or... "What the commercial EELS vendors don't want you to see"
    11:30 - 12:00 PM    *Extending HyperSpy* - How HyperSpy can be extended for almost any use-case (``tomotools`` example)
    12:00 - 12:30 PM    Buffer time, Q&A, and Wrap-up
    12:30 - 1:00 PM     (*Optional*) Post-tutorial time; instructors will be on hand to answer any follow-up questions
    ==================  ============


Pre-tutorial instructions
+++++++++++++++++++++++++

Please review this section in advance of Friday's tutorial session, as it
includes instructions for installing HyperSpy and the Jupyter interactive
computing environment.

.. admonition:: Installation alternatives

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

.. _JupyterHub: https://jupyterhub.readthedocs.io/en/stable/


Installation
------------

At its core, HyperSpy is a third-party library that exists as part of the
scientific Python ecosystem (as opposed to a stand-alone application). Because
of this, installation is slightly more tricky than a normal program, but is not
too difficult once you understand the steps required. The two pieces required
are a Python distribution (pre-installed on Mac and Linux; not included on
Windows), and then the HyperSpy libraries that operate within that Python
environment.

For all operating systems, the recommended Python distribution is
`Anaconda Python <https://www.anaconda.com/distribution/>`_, due to its
prevalence in the scientific community and the ease of managing multiple Python
"environments" on one system. It also provides a uniform way of installing
packages and managing the system regardless of operating system.

.. warning::
    There is also a "standalone" bundle installation package available (for Windows
    only) available from the HyperSpy Github repository (`here <https://github.com/hyperspy/hyperspy-bundle>`_).
    If you have never used Python before, it is the "simplest" way to get
    HyperSpy installed (together with its own Python installation),
    but can lead to multiple redundant Python installations
    and is difficult to upgrade between versions. If you might use Python for
    any other sort of data analysis, plotting, or software development, we
    recommend installing via `Anaconda`_ instead.

Anaconda
~~~~~~~~

Another section's text

HyperSpy
~~~~~~~~
