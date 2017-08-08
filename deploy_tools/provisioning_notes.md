Provising a new site
====================

## Required Packages:
* nginx
* Python 3.6
* virtualenv + pip
* Git

e.g. on Ubuntu

	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get install nginx git python36 python3.6-venv
	
## Nginx Virtual Host config
* see nginx.template.conf
* replace SITENAME with e.g. staging.my-domain.com

## Systemd service
* see gunicorn-system.template.service
* replace SITENAME with e.g. staging.my-domain.com

## Folder Structure

/home/username
|__sites
	|__SITENAME
		|__database
		|__source
		|__static
		|__virtualenv