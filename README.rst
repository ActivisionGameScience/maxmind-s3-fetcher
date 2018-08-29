==============================
 Maxmind to S3 Fetcher
==============================

Fetches Maxmind's geoip2 City database and caches it in S3 with filename (key) `GeoIP2-City.mmdb`.
This is meant to be run periodically (e.g. every week) so that your services don't pound
Maxmind.

This requires ``boto3`` to run.

After cloning, you can run it like this::

    cd src
    python run.py --maxmind_license_key <YOUR_MAXMIND_LICENSE> --s3_bucket <YOURBUCKET> --aws_access_key_id <YOURID> --aws_secret_access_key <YOURSECRET>

Docker instructions
===================

First edit the ``Dockerfile`` to specify the following env vars::

    MAXMIND_LICENSE_KEY=<YOUR_MAXMIND_LICENSE>
    S3_BUCKET=<YOURBUCKET>
    AWS_ACCESS_KEY_ID=<YOURID>
    AWS_SECRET_ACCESS_KEY=<YOURSECRET>

Then create a docker image for ``maxmind-s3-fetcher``::

    sudo docker build -t maxmind-s3-fetcher .

and launch it::

    sudo docker run -d --name maxmind-s3-fetcher


License
=======

All files are licensed under the BSD 3-Clause License as follows:
 
| Copyright (c) 2015, Activision Publishing, Inc.  
| All rights reserved.
| 
| Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
| 
| 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
|  
| 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
|  
| 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
|  
| THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

