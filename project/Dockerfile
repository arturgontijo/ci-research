FROM ubuntu:18.04

ARG git_owner="arturgontijo"
ARG git_repo="ci-research"
ARG git_branch="master"

ARG test_host
ARG test_port
ARG test_user
ARG test_pass
ARG test_storage
ARG test_cert
ARG test_certkey

ENV TEST_HOST=${test_host:-"0.0.0.0"}
ENV TEST_PORT=${test_port:-"7777"}
ENV TEST_USER=${test_user:-"admin"}
ENV TEST_PASS=${test_pass:-"admin#PASS"}
ENV TEST_STORAGE=${test_storage:-"storage"}
ENV TEST_CERT=${test_cert:-"cert.pem"}
ENV TEST_CERTKEY=${test_certkey:-"privkey.pem"}

ENV PROJECT_FOLDER=/opt/${git_owner}/${git_repo}

RUN mkdir -p ${PROJECT_FOLDER}

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    git \
    wget \
    nano \
    curl

ADD . ${PROJECT_FOLDER}

RUN cd ${PROJECT_FOLDER} && \
    pip3 install -r requirements.txt

WORKDIR ${PROJECT_FOLDER}
