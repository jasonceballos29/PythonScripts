#!/bin/bash
sudo yum install -y git
sudo git clone https://github.com/ACloudGuru-Resources/course-aws-certified-developer-associate/
#ls into the directory, then select Cognito Demo folder
#Move the two web files into the HTTPD folder so we can use VIM to modify them and add info
sudo mv fact.jpg /var/www/html
sudo mv index.html /var/www/html
cd /var/www/html
