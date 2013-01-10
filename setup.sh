# Setup python env
#virtualenv env
# Initialize python env
source ./env/bin/activate
# Install gcc & python headers
sudo aptitude install build-essential python-dev
# Install mysql server
sudo aptitude install mysql-server
# Update distribute (needed by MySQL-python)
easy_install -U distribute
# Install mysql_config
sudo apt-get install libmysqlclient-dev
# Install python dependencies
pip install -r requirements.txt

# Load DB
#mysql -u root -p
#CREATE DATABASE moon12;
#ALTER DATABASE moon12 charset=utf8;

# Intall MySQL-python
sudo apt-get install python-mysqldb

cd moon12
python manage.py migrate syncdb
python manage.py migrate artful
./load_db.sh
cd ..
