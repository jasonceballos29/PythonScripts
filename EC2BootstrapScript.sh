#!/bin/bash
yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
yum install -y httpd mariadb-server
yum install stress -y
systemctl start httpd
systemctl enable httpd
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php
echo “Hello World, Jason C connecting from $(hostname -f)” > /var/www/html/index.html
chkconfig httpd on > /var/log/chkconfig_httpd.txt
#Specify User Data at Launch Script
#aws ec2 run-instances --image-id ami-abcd1234 --count 1 --instance-type m3.medium \ --key-name my-key-pair --subnet-id subnet-abcd1234 --security-group-ids sg-abcd1234 \ --user-data echo user data