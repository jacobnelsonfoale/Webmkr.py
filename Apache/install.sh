#!/usr/bin/bash

echo "Make sure Apache2 is installed Before Running"
echo "sudo apt update"
echo "sudo apt install apache2"
sleep .5

sudo cp ../index.html /var/www/html
sudo cp ../Contact.html /var/www/html
sudo cp ../home-theme.css /var/www/html
sudo cp -R ../posts/ /var/www/html
sudo cp ../favicon.ico /var/www/html
