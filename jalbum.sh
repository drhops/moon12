#!/bin/bash

# Runner script for jAlbum.
# @author drhops@gmail.com (Dan Hopkins)

# Args: author

if [ $# -ne 1 ]
then
  echo "Usage: `basename $0` <author>"
  echo "(e.g. ./jalbum.sh artists/paco-uong)"
  exit 1
fi

echo $1

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IMG_DIR="$DIR/moon12/artful/static/images/$1"

# use lowercase file extension
find $IMG_DIR -name "*.JPG" -print0 | xargs -0 rename 's/\.JPG/\.jpg/'
find $IMG_DIR -name "*.JPEG" -print0 | xargs -0 rename 's/\.JPEG/\.jpg/'
find $IMG_DIR -name "*.jpeg" -print0 | xargs -0 rename 's/\.jpeg/\.jpeg/'
find $IMG_DIR -name "*.jpg" -print0 | xargs -0 rename 's/ /_/g'
find $IMG_DIR -name "*.jpg" -print0 | xargs -0 rename 's/__/_/g'
find $IMG_DIR -name "*.jpg" -print0 | xargs -0 rename 's/#/N/g'

# transform images into additional formats
java -jar /usr/share/jalbum/JAlbum.jar -directory $IMG_DIR -outputDirectory $IMG_DIR/album -skin galleriffic
