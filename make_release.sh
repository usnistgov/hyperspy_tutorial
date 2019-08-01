#!/usr/bin/env bash

zip -r hyperspy_tutorial.zip . -x "*/.*" -x ".*" -x "make_release.sh" -x "./*.zip"

zip -r hyperspy_tutorial_no_big_data.zip . -x "*/.*" -x ".*" -x "make_release.sh" -x "./*.zip"
