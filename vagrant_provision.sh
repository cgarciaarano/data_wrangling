#!/bin/bash
sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip install -r /vagrant/requirements.txt
exit 0