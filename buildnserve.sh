#!/bin/fish
pelican content -s pelicanconf.py -o docs
pelican --listen -o docs/
