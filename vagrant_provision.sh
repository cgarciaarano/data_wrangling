#!/bin/bash
sudo apt-get update
sudo apt-get -qy install python-dev python-pip
sudo pip install -r /vagrant/requirements.txt
# MongoDB install
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB1
echo 'deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.0 multiverse' > /etc/apt/sources.list.d/mongodb.list
sudo apt-get update
sudo apt-get install -qy --force-yes mongodb-org
exit 0