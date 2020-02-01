.. _bundle_mac-label:

Installing on macOS
-------------------

On macOS, the easiest way to install HyperSpy is to use the HyperSpy bundle
installer. This simple to install program provides a customized Anaconda 
installation, which contains the HyperSpy libraries but also other libraries 
used in the field of electron microsocpy. A detailed walk through of the 
process is provided below.

Download
^^^^^^^^

First, download the installer using the following link
(https://github.com/ericpre/hyperspy-bundle/releases):

.. figure:: _static/github_download_labels.png
   :width: 100 %
   :target: https://github.com/ericpre/hyperspy-bundle/releases
   :alt: Links HyperSpy bundle downloads
   :figwidth: 70%

   Download the installer corresponding to your system.

Installing
^^^^^^^^^^

Run the downloaded file to proceed with the installation. This installer is
currently not identified as trusted party by macOS, meaning that macOS will
not allow to run the installer simply by double-clicking on it. However, 
control-clicking the app icon, then choosing ``Open`` from the shortcut menu 
will allow to run the installer, as explained in the 
`macOS documentation <https://support.apple.com/en-gb/guide/mac-help/mh40616/mac>`_.

.. figure:: _static/macOS_control_click_open.png
   :width: 100 %
   :alt: Links HyperSpy bundle downloads
   :figwidth: 70%

   To open the installer, control-click the installer icon and choose Open from
   the shortcut menu.

This rest of the process is fairly straightforward. For the installation 
location, we *highly* recommend to select ``Install for me only``, as set 
by default:

.. figure:: _static/macOS_install_destination.png
   :width: 100 %
   :alt: Bundle installation progress
   :figwidth: 50%

   Single user installation is recommended.


And that's it! All the installed programs should now be installed and they
distribution should be available from the terminal or from the context menu
(:ref:`start_jupyter`). You can either continue following the next section to
test the installation, or continue to the :ref:`getting-data` section on the
main page.

.. include:: testing_install.rst
