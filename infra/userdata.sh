#!/bin/sh

yum install docker -y

# makes a directory
mkdir /appdata
mount -t efs fs-d48c7f8c:/ /appdata


# enable and start docker
systemctl enable docker
systemctl start docker

# bootstraps "docker compose"
curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
usermod -aG docker ec2-user

docker pull docker pull yohanhl/flask-dynamodb-app

# Heredoc for a docker-compose.yaml file
cat << 'EOF' > /app/docker-compose.yaml
version: '3'
services:
  app:
    image: yohanhl/flask-dynamodb-app
    ports:
      - 8080:5000
    restart: always
    env_file: .env
EOF

cd /app
docker-compose up