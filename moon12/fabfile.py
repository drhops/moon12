from fabric.api import lcd
from fabric.api import local

def deploy():
    with lcd('/Users/drhop/dev/moon12deploy/moon12'):
        local('git pull /Users/drhop/dev/moon12dev')
        local('python manage.py migrate artful')
        local('python manage.py test artful')
        #local('/my/command/to/restart/webserver')

def prepare_deploy(branch):
    local('python manage.py test artful')
    local('git add -p && git commit || :')
    local('git checkout master && git merge ' + branch)
