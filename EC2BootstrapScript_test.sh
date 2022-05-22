#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
echo “Hello World, Jason C connecting from $(hostname -f)” > /var/www/html/index.html
sudo yum install firewalld
sudo systemctl start firewalld
sudo systemctl reload firewalld
sudo systemctl enable firewalld
sudo ss -lntp > /var/log/firewalld.txt