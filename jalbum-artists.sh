#!/bin/bash

for i in `ls -1 ./moon12/static/images/artists/`; do ./jalbum.sh artists/$i; done
