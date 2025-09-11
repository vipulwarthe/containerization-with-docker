# Containerization With Docker

    https://medium.com/@kadimasam/containerization-with-docker-a6bf9f5786a0

## Overview

Docker containerization is revolutionizing software development and deployment. This introduction highlights Docker’s role in creating efficient, portable application containers.

## Resources

1. [Containerization With Docker](https://medium.com/@kadimasam/containerization-with-docker-a6bf9f5786a0)

2. Create one ubuntu 22.04 server /t2.medium/15gb/all-traffic for demo purpose
   
4. Install Docker

sudo vi docker.sh

       # Add Docker's official GPG key:
       sudo apt-get update
       sudo apt-get install ca-certificates curl
       sudo install -m 0755 -d /etc/apt/keyrings
       sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
       sudo chmod a+r /etc/apt/keyrings/docker.asc

       # Add the repository to Apt sources:
       echo \
       "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
       $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
       sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       sudo apt-get update
       sudo apt install docker.io -y
       docker --version
       sudo usermod -aG docker $USER    # Next cmd is "newgrp docker" or you can use below command
       sudo chown $USER /var/run/docker.sock
       sudo systemctl start docker
       sudo systemctl enable docker
       sudo systemctl status docker

 sudo chmod +x docker.sh
 
 ./docker.sh 



4. create folder docker_demo and change the directory docker_demo

   15  mkdir docker_demo && cd docker_demo

5. clone github repo and change the directory to containerization-with-docker/
   
   16  git clone https://github.com/vipulwarthe/containerization-with-docker.git
   
   17  ls
   
   18  cd containerization-with-docker/
   
   19  ls
   
   21  sudo apt install python3-pip -y
   
   22  pip install -r requirements.txt

7. Build and run the docker image:
   
   23  docker build -t djangoapp-image:v1.0.0 .
   
   24  docker image ls  or  docker images
   
   25  docker run -p 8000:8000 djangoapp-image:v1.0.0
   
   31  docker ps
   
   32  docker stop <container name>

8. access the application  http://<public ip>:8000

