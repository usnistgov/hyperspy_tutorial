# How to get nice PDF versions of the RISE slides

## Installation:

* Install [decktape](https://github.com/astefanutti/decktape) via `npm install -g decktape`
* Make sure you have a currently running notebook server with access to the presentation (the notebook does not have to be open)

## Running `decktape` and tweaking output

* From the path to which you cloned the repository, run a command structured like the following:
  * `decktape rise -s 1920x1080 http://localhost:8888/notebooks/notebook_file.ipynb?token=access_token output_file.pdf`
  * Sometimes this command arbitrarily fails, so try it again if it does
* The `token` is necessary to authenticate to Jupyter (find it in the console output of `jupyter notebook list`)
* The resulting output will have one slide for every fragment, so you'll have to manually go through and delete the extra slides (or just leave them in) using a pdf editor