import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)

    # test if it works with this command and if it prints any log on stdout
    #pip.main(['install', '--upgrade', package])
