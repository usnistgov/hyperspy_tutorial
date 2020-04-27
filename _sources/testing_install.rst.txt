Testing the installation
^^^^^^^^^^^^^^^^^^^^^^^^

Start the Jupyter Qt Console using the context menu (right click) shortcut (see
the :ref:`start_jupyter` section for details).

The Qt Console is an interactive Python interpreter that allows you to enter
Python statements directly and immediately see their output. Once the console
has opened and you see a prompt that says ``In [1]:``, copy the following code
snippet at the location of the blinking cursor:

..  code-block:: python

    %matplotlib qt
    import hyperspy.api as hs
    s = hs.datasets.artificial_data.get_core_loss_eels_signal(add_powerlaw=True)
    s.remove_background()

Very briefly, this code is loading the interactive plotting libraries, loading
HyperSpy, creating an example EELS signal from some artificial data, and then
telling the interpreter you want to interactively remove the Power Law
background. Press ``Shift-Enter`` within the console to run the lines of code
you pasted in (it may take a few moments to run if this is the first time
you've used HyperSpy on your machine):

.. figure:: _static/bundle_test_qtconsole_code.png
   :width: 100 %
   :alt: Entering the example code into the Qt Console
   :figwidth: 70%

   Entering the example code into the Qt Console

Eventually, you should see a spectrum window and a small tool window for
removing the background open (they may be stacked on top of each other;
drag them out of the way, if so). If you click and drag on part of the spectrum
display, HyperSpy will fit a Power Law to the signal within that region,
and also show you a preview of the background-subtracted signal:

.. figure:: _static/bundle_test_bgremoval.gif
   :width: 100 %
   :alt: Removing the background from a test signal
   :figwidth: 90%

   By clicking and dragging on the spectrum display, a region is created (shown
   in red). The fitted background is shown in blue, and a preview of the
   background-subtracted signal is displayed in green.

Clicking "OK" in the *Background removal tool* window will perform the
background subtraction, and replace the window with one showing the resulting
signal:

.. figure:: _static/bundle_test_bgremoval_sig.png
   :width: 100 %
   :alt: Removing the background from a test signal
   :figwidth: 50%

Assuming all of this worked, congratulations! You have a working HyperSpy
installation and you have run your first bit of open-source HyperSpy-based
materials science data analysis! Click the button below to return to the main
tutorial homepage:

.. raw:: html

    <div class="text-center">
        <a  class="downloadbutton"
            href="index.html">
                Click here to return<br/>to the main page
        </a>
    </div>

|
|
|
