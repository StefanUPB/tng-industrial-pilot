#!/bin/bash
#
# We need the 5GTANGO SDK tools to package the projects.
sudo pip3 remove tng-sdk-package
sudo pip3 remove tng-sdk-validate
sudo pip3 remove tng-sdk-proejct
set -e
sudo pip3 install --upgrade git+https://github.com/sonata-nfv/tng-sdk-project.git
sudo pip3 install --upgrade git+https://github.com/sonata-nfv/tng-sdk-validation.git
sudo pip3 install --upgrade git+https://github.com/sonata-nfv/tng-sdk-package

tng-project -h
tng-validate -h
tng-package -h