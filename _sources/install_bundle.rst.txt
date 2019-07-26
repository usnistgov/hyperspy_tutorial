.. _bundle-label:

Installing via the "Bundle"
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are running on Windows, the easiest way to install HyperSpy is using
the "standalone" bundle package. This simple to install program provides a
customized Python installation that has the HyperSpy libraries pre-installed.
Instructions can be found at from the HyperSpy Bundle Github repository
(`here <https://github.com/hyperspy/hyperspy-bundle>`_), and a detailed walk
through of the process is provided below.

Download
^^^^^^^^

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

Installing
^^^^^^^^^^

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
Start Menu under the "HyperSpy Bundle" folder. You can either continue following
the next section to test the installation, or continue to the
:ref:`getting-data` section on the main page.

Testing the installation
^^^^^^^^^^^^^^^^^^^^^^^^

If you would like to test that your installation is working properly, you can
run a small test example by opening the "Qt Console". This is an interactive
Python interpreter that allows you to type in Python statements directly. Launch
the Qt Console from within the "HyperSpy Bundle" folder in the Start Menu:

.. figure:: _static/bundle_test_qtconsole.png
   :width: 100 %
   :alt: Launching the interactive Python console
   :figwidth: 50%

   Launching the interactive Python console from the Start Menu

.. include:: testing_install.rst