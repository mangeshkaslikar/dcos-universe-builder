#!/bin/bash
git clone -b "3.3.0-2.73.1"  https://github.com/mesosphere/dcos-jenkins-service.git 3.3.0-2.73.1
cd 3.3.0-2.73.1
cp -f ../Dockerfile . 
docker build .
