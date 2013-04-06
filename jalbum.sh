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
#java -jar /usr/share/jalbum/JAlbum.jar -help
java -jar /usr/share/jalbum/JAlbum.jar -directory $IMG_DIR -outputDirectory $IMG_DIR/album -skin galleriffic
