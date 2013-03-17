# Setup the system to run Moon12.
# @author drhops@gmail.com (Dan Hopkins)

# Install virtualenv
sudo apt-get install -y python-virtualenv
# Setup python env
virtualenv env
# Initialize python env
source ./env/bin/activate
# Install gcc & python headers
sudo apt-get install -y build-essential python-dev
# Install mysql server
sudo apt-get install -y mysql-server
# Update distribute (needed by MySQL-python)
easy_install -U distribute
# Install mysql_config
sudo apt-get install -y libmysqlclient-dev
# Install python dependencies
pip install -r requirements.txt

# Load DB
#mysql -u root -p
#CREATE DATABASE moon12;
#ALTER DATABASE moon12 charset=utf8;

# Intall Django
sudo apt-get install -y python-django

# Intall South
sudo apt-get install -y python-django-south

# Intall MySQL-python
sudo apt-get install -y python-mysqldb

# Migrate Moon12 DB
cd moon12
python manage.py syncdb
python manage.py migrate artful
./load_db.sh
cd ..
