FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
        git \
        curl \
        openssh-client \
        python \
        python-dateutil \
        python-httplib2 \
        python-jinja2 \
        python-paramiko \
        python-pip \
        python-setuptools \
        python-yaml \
        tar


RUN git clone git://github.com/ansible/ansible.git --recursive


ENV PATH /ansible/bin:$PATH 
ENV PYTHONPATH /ansible/lib

RUN mkdir /netscaler-ansible

COPY ansible-modules/ /netscaler-ansible/ansible-modules/
COPY test/ /netscaler-ansible/test/
COPY documentation_fragments/netscaler.py /netscaler-ansible/documentation_fragments/netscaler.py
COPY install.py /netscaler-ansible
COPY nitro-python-1.0.tar.gz /netscaler-ansible

RUN pip install /netscaler-ansible/nitro-python-1.0.tar.gz
RUN python /netscaler-ansible/install.py

RUN rm -rf /netscaler-ansible

ENTRYPOINT ["ansible-playbook"]
