#!/bin/env python

import argparse
import logging
import boto3
import urllib.request
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
import tarfile
import io
import datetime as dt
import sys


maxmind_url = "https://download.maxmind.com/app/geoip_download?edition_id=GeoIP2-City&date={}&suffix=tar.gz&license_key={}"
maxmind_db = "GeoIP2-City.mmdb"

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--maxmind_license_key", required=True)
    parser.add_argument("--s3_bucket", required=True)
    parser.add_argument("--aws_access_key_id", required=True)
    parser.add_argument("--aws_secret_access_key", required=True)
    args = parser.parse_args()

    log.info("Using S3 bucket {}".format(args.s3_bucket))


    # grab the latest from Maxmind
    # City db updates every Tues (at least the non-free one does)
    today = dt.date.today()
    lasttues = today - dt.timedelta(days=today.weekday() + 6)
    lasttues = "%4d%02d%02d" % (lasttues.year, lasttues.month, lasttues.day)

    url = maxmind_url.format(lasttues, args.maxmind_license_key)

    log.info("Fetching from %s" % url)
    with urllib.request.urlopen(url) as response:
        tarball_bytes = response.read()

    file_like_wrapper = io.BytesIO(tarball_bytes)
    tar = tarfile.open(fileobj=file_like_wrapper)
    tar.getnames()
    for name in tar.getnames():
        if name.endswith(maxmind_db):
            maxmind_db_bytes = tar.extractfile(name).read()


    # Copy to S3
    log.info("Copying to S3 bucket %s" % args.s3_bucket)
    session = boto3.Session(
        aws_access_key_id=args.aws_access_key_id,
        aws_secret_access_key=args.aws_secret_access_key
    )
    s3 = session.resource('s3')
    s3.Object(args.s3_bucket, maxmind_db).put(Body=maxmind_db_bytes)
