# Udacity Server Project Configuration
This is the last project for the "Full Stack Web Developer Nanodegree" program on Udacity, the project consist in the deploying a ubuntu vsp (virtual private server) and do the following tasks:
* use a linux server instance, its recommended to use Amazon lightsail, Digital Ocean, Lonide
* Change the ssh port from 22 to 2200
* Configure the Uncomplicated Firewall (UFW) to only allow incoming connection for SSH (port 2200), HTTP (port 80) and NTP (port 123)
* Create a user (__grader__)
* Give __grader__ the permission to sudo
* Create an SSH key pair for __grader__ using the ssh-keygen tool
* Install apache2 and deploy the Item Catalog Project done early in the course 
   

## VPS service provider
For the project I used [digital ocean](https://www.digitalocean.com/pricing/) which has a $5/mo $0.007/hr plan. The process is very easy: 
* Create a new droplet, use Ubuntu 16.04.6 X64
* You will receive an email with the root password

## Server Details
* ip address: 192.241.149.216
* SSH port: 2200
* project url: http://192.241.149.216.xip.io/

## Software installed
* Apache2
* libapache2-mod-wsgi
* postgresql
* python-pip
* python-Flask
* Git
* python-httplib2
* python-requests
* python-bleach
* python-sqlachemy
* python-oauth2client
* python-psycopg2
* python-passlib
* python-virtualenv


## Connect to Server
To connect to the server and open its files for editing i used [putty](https://www.putty.org/) and [WinSCP](https://winscp.net/eng/download.php), to test grader and create public and private keys i used Git Bash which is a emulated linux console application that can interact with the windows file system that comes with [Git](https://git-scm.com/downloads).

---
Note: Is possible also to use a linux subsystem to do all the tasks, just open windows store type linux and install the linux you want to work with, but keep in mind that is not advised to open linux files from Windows metadata may corrupt your work 

---

## Server initial Configuration
### Update all currently installed packages
```console
$ sudo apt-get update
$ sudo apt-get upgrade
```

### Create the user grader

```console
$ sudo adduser grader
```

### Give grader permission to sudo
For this you need to create the file called __grader__ inside the directory /etc/__sudoers.d__
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/etc/sudoers.d# sudo nano grader
```
Add the following line inside grader
```nanorc
grader ALL=(ALL) NOPASSWD:ALL
```
## Setup SSH Authentication
This step has two parts: first generate a SSH key pair on your local machine second copy the public key to the server.

__LOCAL MACHINE:__ If you are using gitbash on windows the keys will located in "*C:\Users\YOUR_username\\.ssh*", also by default name of your keys are __id_rsa__ and __id_rsa.pub__ I named mine graderKEY and graderKEY.pub
```console
Sertech@SertechLaptop MINGW64 ~
$ ssh-keygen -t rsa -b 2048 -C "Udacity GRADER"
```
__SERVER__:In the server change user to grader, create a directory called .ssh in grader's home directory, inside that folder create a file named authorized_keys and finally copy and paste the contents of id_rsa.pub into authorized_keys
#### switch to grader user
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/home# su grader
```
#### as grader create .ssh folder
```console
grader@ubuntu-s-1vcpu-1gb-nyc1-01:~$ mkdir ~/.ssh
```
#### create the file for the public key
Here paste the contents of graderKEY.pub(in this case) ctrl+o to save ctrl+x to exit
```console
grader@ubuntu-s-1vcpu-1gb-nyc1-01:~$ sudo nano ~/.ssh/authorized_keys
```
#### Set correct permissions
```console
grader@ubuntu-s-1vcpu-1gb-nyc1-01:~$ chmod 700 ~/.ssh
grader@ubuntu-s-1vcpu-1gb-nyc1-01:~$ sudo chmod 644 ~/.ssh/authorized_keys
```
### Change the SSH port from 22 to 2200
Edit the file called sshd_config located in _/etc/ssh/sshd_config_, look for a commented line or just a line that says Port 22 and change it to Port 2200
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:~# sudo nano /etc/ssh/sshd_config
```
### Restart the SSH service
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:~# sudo service ssh restart
```
## Configure UFW to allow given connections
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:~# sudo ufw allow 2200
root@ubuntu-s-1vcpu-1gb-nyc1-01:~# sudo ufw allow 80
root@ubuntu-s-1vcpu-1gb-nyc1-01:~# sudo ufw allow 123
```
### Enable UFW
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:~# sudo ufw enable
```
## Configure the time zone to UTC
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:~# sudo dpkg-reconfigure tzdata
```
It will open a different menu, inside it select none of the above, then select UTC and finish
```console
Current default time zone: 'Etc/UTC'
Local time is now:      Mon May 27 02:54:36 UTC 2019.
Universal Time is now:  Mon May 27 02:54:36 UTC 2019.
```
## Install and configure Apache to serve a Python mod_wsgi application

### Install Apache2 and libapache2-mod-wsgi
```console
$ sudo apt-get install apache2
$ sudo apt-get install libapache2-mod-wsgi
$ sudo a2enmod wsgi
```
### Install and configure PostgreSQL
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/# sudo apt-get install postgresql
```
Change to the postgres user
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/# sudo su - postgres
postgres@ubuntu-s-1vcpu-1gb-nyc1-01:~$
```
Create a new user:catalog password:password with limited access to the catalog application database
```console
postgres@ubuntu-s-1vcpu-1gb-nyc1-01:~$ createuser --interactive -P
Enter name of role to add: catalog
Enter password for new role:
Enter it again:
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) n
Shall the new role be allowed to create more new roles? (y/n) n
```
Create the catalog database
```console
postgres@ubuntu-s-1vcpu-1gb-nyc1-01:~$ psql
postgres=# CREATE DATABASE catalog;
postgres=# \q
```
### Install Git
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/# sudo apt-get install git
```

## Clone the Catalog project
Inside /var/www/ create a directory called catalog and there clone the Catalog repository
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog# sudo git clone https://github.com/sertech/projectProtafolio3.git catalog
```
## Install pip for phyton
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo apt-get install python-pip
```
## Install virtual environment with pip
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# pip install virtualenv
```
## Create a virtual environment called venv
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo virtualenv venv
```
## Activate venv and install python dependencies
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# source venv/bin/activate
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo pip install Flask
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo pip install psycopg2
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo pip install requests
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo pip install oauth2client
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo pip install itsdangerous
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo pip install google-api-python-client
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo pip install SQLAlchemy
```
## Exit venv
```console
(venv) root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# deactivate
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog#
```
## Setup the catalog project configuration file
Create a configuration file for the catalog project called catalog.conf 
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog/catalog# sudo nano /etc/apache2/sites-available/catalog.conf
```
catalog.conf
```apacheconf
<VirtualHost *:80>
		ServerName 192.241.149.216
		ServerAlias 192.241.149.216.xip.io
		ServerAdmin ihatelinux@whyissohard.com
		WSGIScriptAlias / /var/www/catalog/catalog.wsgi
		<Directory /var/www/catalog/catalog/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/catalog/catalog/static
		<Directory /var/www/catalog/catalog/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
## Enable the virtual host
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/# sudo a2ensite catalog
```
note: to disable other sites use ```$sudo a2dissite```
## Create the wsgi file for the catalog project
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog# sudo nano catalog.wsgi
```
catalog.wsgi
```python
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalog/")

from catalog import app as application
application.secret_key = 'do not share this baby2'
```
## Prepare the catalog application from development to production
It is necessary to make small changes in the application files for it to run in the server, the main application file needs to be renamed to \__init__.py   

BEFORE:
```python
engine = create_engine('sqlite:///catalogApp.db')

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')

if __name__ == '__main__':
    app.secret_key = 'do not share this baby'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
```
AFTER:
```python
engine = create_engine('postgresql://catalog:password@localhost/catalog')

CLIENT_ID = json.loads(open('/var/www/catalog/catalog/client_secrets.json', 'r').read())['web']['client_id']

oauth_flow = flow_from_clientsecrets('/var/www/catalog/catalog/client_secrets.json', scope='')

if __name__ == '__main__':
    app.secret_key = 'do not share this baby2'
    app.run()
```

The directory structure should be like this inside /var/www/

```console
+-- catalog
|   +-- catalog
|   |   +-- __init__.py
|   |   +-- db_setup.py
|   |   +-- static
|   |   +-- templates
|   |   +-- venv (the virtual environment)
|   |   +-- other files and folders necessary
|   +-- catalog.wsgi
```
## finally restart the apache2 service
A restart is necessary every time a file is change inside app directory
```console
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog# sudo service apache2 reload
root@ubuntu-s-1vcpu-1gb-nyc1-01:/var/www/catalog# sudo service apache2 restart
```