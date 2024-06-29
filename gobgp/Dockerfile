FROM ubuntu:24.04
RUN apt-get update && \
    apt-get remove -y binutils && \
    apt-get install -y \
        python3 \
        python3-pip \
        gobgp \
        wget && \
    rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY ./gobgpd.conf /root/gobgp/gobgpd.conf
COPY ./entrypoint.sh /root/gobgp/entrypoint.sh
COPY ./startup.sh /root/gobgp/startup.sh
RUN chmod +x /root/gobgp/entrypoint.sh && \
    chmod +x /root/gobgp/startup.sh
ENTRYPOINT ["/root/gobgp/entrypoint.sh"]
