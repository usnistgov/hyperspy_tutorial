# How to get nice PDF versions of the RISE slides

## Installation:

* Clone the [decktape](https://github.com/astefanutti/decktape) repository somewhere locally
* Make sure you have nodejs installed (`conda install nodejs`)
* Make the following changes to `plugins/rise.js` in the decktape repo because of [two](https://github.com/astefanutti/decktape/issues/131) [issues](https://github.com/astefanutti/decktape/issues/74):
  * Replace all instances of `#start_livereveal` with `#RISE` (the button to start the slideshow has changed `id` values)
  * Change `fragments: false` to `fragments: true` (line ~41),

## Configuring the presentation

* Add the following to the beginning of `rise.css` in order to prevent the Jupyter cell selection highlighting in pdf output:
    ```css
    /* Disable selected cell indicator (for decktape) */
    div.cell.selected, div.cell.selected.jupyter-soft-selected {
        border: 0;
    }

    div.cell.selected:before, div.cell.selected.jupyter-soft-selected:before {
        position: absolute;
        display: block;
        top: -1px;
        left: -1px;
        width: 0px;
        height: calc(100% + 2px);
        content: '';
        background:white;
    }
    ```
* Remove any `autolaunch: true` from the notebook's metadata (this will mess up the `decktape` parser)
* Make sure you have a currently running notebook server with access to the presentation (the notebook does not have to be open)

## Running `decktape` and tweaking output

* From the path to which you cloned the repository, run a command structured like the following: 
  * `node decktape.js rise -s 1920x1200 http://localhost:8888/notebooks/notebook_file.ipynb?token=baa04fbbe02331a4fc02aa93b3af764e000854e10e54a399 output_file.pdf`
  * Sometimes this command arbitrarily fails, so try it again if it does
* The `token` is necessary to authenticate to Jupyter (find it in the console output)
* The resulting output will have one slide for every fragment, so you'll have to manually go through and delete the extra slides (or just leave them in) using a pdf editor