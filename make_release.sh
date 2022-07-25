#!/usr/bin/env bash

# zip everything into one archive, ignoreing hidden files and directories, this 
# file, and any zip files in the root of the directory tree
find . -not -path '*/\.*' -not -path './make_release.sh' -not -path './*.zip' -not -path './_build/*' \
       -not -path './environment.yml' -type f | zip -9 hyperspy_tutorial.zip --names-stdin

# same as above, ignoring files larger than 100M:
# find . -not -path '*/\.*' -not -path './make_release.sh' -not -path './*.zip' \
#        -not -path './environment.yml' -type f -not -size +100M | zip hyperspy_tutorial_no_big_data.zip --names-stdin
