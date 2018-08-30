FROM phusion/baseimage

# Need wget and ca-certificates to grab miniconda
# Conda itself needs bzip2
RUN apt-get update && apt-get -y install wget bzip2 ca-certificates

# grab miniconda, setup root env in /opt/anaconda, and call out to docker-build.sh to build the rest
RUN wget -O miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    /bin/sh miniconda.sh -b -p /opt/anaconda && \
    rm miniconda.sh

COPY docker-build.sh /
RUN /bin/bash /docker-build.sh && \
    rm /docker-build.sh

# copy to /opt
COPY src /opt/staging
RUN chown -R root:root /opt/staging
WORKDIR /opt/staging

# run 
CMD ["/bin/bash", "start_from_docker.sh"]
