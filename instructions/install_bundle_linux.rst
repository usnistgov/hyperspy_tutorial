.. _bundle_linux-label:

Installing on Linux
-------------------

On Linux, the easiest way to install HyperSpy is to use the HyperSpy bundle
installer. This simple to install program provides a customized Anaconda 
installation, which contains the HyperSpy libraries but also other libraries 
used in the field of electron microscopy. A detailed walk through of the
process is provided below.

Download
^^^^^^^^

First, download the installer by visiting
`this link <https://github.com/ericpre/hyperspy-bundle/releases>`_ and selecting
the correct option for your operating system:

.. figure:: _static/github_download_labels.png
   :width: 100 %
   :target: https://github.com/ericpre/hyperspy-bundle/releases
   :alt: Links HyperSpy bundle downloads
   :figwidth: 70%

   Download the installer corresponding to your system.

Installing
^^^^^^^^^^

The process is exactly the same as 
`installing Miniconda <https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html>`_
or Anaconda:

1. In your terminal window, run:

   ..  code-block:: bash
    
       bash HyperSpy-bundle-2020.02.05-Linux-x86_64.sh

2. Follow the prompts on the installer screens.
   If you are unsure about any setting, accept the defaults. You can change
   them later.
3. To make the changes take effect, close and then re-open your terminal window.
4. Test your installation. In your terminal window, run the command 
   ``conda list``. A list of installed packages appears if it has been
   installed correctly.

And that's it! All the installed programs should now be installed and they
distribution should be available from the terminal or from the context menu
(:ref:`start_jupyter`). You can either continue following the next section to
test the installation, or continue to the :ref:`getting-data` section on the
main page.

.. include:: testing_install.rst
