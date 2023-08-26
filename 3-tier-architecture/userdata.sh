#!/bin/bash

# Update the system
sudo yum update -y

# Install Apache HTTP Server (httpd)
sudo yum install httpd -y

# Start and enable the HTTP server
sudo systemctl start httpd
sudo systemctl enable httpd