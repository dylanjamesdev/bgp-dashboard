FROM ubuntu:24.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get remove -y binutils && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        wget && \
    rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /tmp/requirements.txt
RUN python3 -m venv venv && chmod +x venv
RUN . venv/bin/activate && pip3 install -r /tmp/requirements.txt
RUN wget https://github.com/osrg/gobgp/releases/download/v3.27.0/gobgp_3.27.0_linux_amd64.tar.gz && \
    tar -xzvf gobgp_3.27.0_linux_amd64.tar.gz && \
    mv gobgp /usr/local/bin/gobgp && \
    mv gobgpd /usr/local/bin/gobgpd && \
    rm gobgp_3.27.0_linux_amd64.tar.gz
COPY ./gobgpd.conf /root/gobgp/gobgpd.conf
COPY ./entrypoint.sh /root/gobgp/entrypoint.sh
COPY ./startup.sh /root/gobgp/startup.sh
RUN chmod +x /root/gobgp/entrypoint.sh && \
    chmod +x /root/gobgp/startup.sh
ENTRYPOINT ["/root/gobgp/entrypoint.sh"]
