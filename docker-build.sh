#!/bin/bash

# create the condarc
echo "channels:\n  - defaults" > /root/.condarc#

echo "Exposing conda..."
source /opt/anaconda/etc/profile.d/conda.sh
conda update --all -y
conda install jinja2 conda-build -y

echo "Creating and activating py36 conda env..."
conda create -n py36 python=3.6 -y
conda activate py36
conda install boto3
