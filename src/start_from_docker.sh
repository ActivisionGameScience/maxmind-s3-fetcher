#!/bin/bash

# bail on error
set -e 

echo "Activating conda env..."
source /opt/anaconda/etc/profile.d/conda.sh
conda activate py36

# copy everything from staging
mkdir /opt/prod
cp -ax /opt/staging/* /opt/prod
cd /opt/prod

if [ -n "$MAXMIND_LICENSE_KEY" ]; then
    ARGS="--maxmind_license_key $MAXMIND_LICENSE_KEY"
fi

if [ -n "$MAXMIND_S3_BUCKET" ]; then
    ARGS="$ARGS"" --s3_bucket $MAXMIND_S3_BUCKET"
fi

if [ -n "$MAXMIND_AWS_ACCESS_KEY_ID" ]; then
    ARGS="$ARGS"" --aws_access_key_id $MAXMIND_AWS_ACCESS_KEY_ID"
fi

if [ -n "$MAXMIND_AWS_SECRET_ACCESS_KEY" ]; then
    ARGS="$ARGS"" --aws_secret_access_key $MAXMIND_AWS_SECRET_ACCESS_KEY"
fi

echo "Syncing..."
python run.py $ARGS
