# HyperSpy tutorial website builder

This repository contains the files required to build a website for a
HyperSpy tutorial using [Sphinx](https://www.sphinx-doc.org/en/master/).

To build the website, make sure [`poetry`](https://python-poetry.org/docs/)
is installed, and then run `poetry install` from this directory. That
will install Sphinx and the website theme. Once that's done, run
`poetry run build`, which will use the `build_helper.build` file to run
sphinx and the website output will be in the `_build/` folder.

Once you're happy with the output, you can copy these static html files
into the `nist-pages` branch on this repo to have it published to 
https://pages.nist.gov/hyperspy_tutorial
