FROM ubuntu:18.04

ARG git_owner="arturgontijo"
ARG git_repo="ci-research"
ARG git_branch="master"

ARG test_host="0.0.0.0"
ARG test_port="7077"
ARG test_user="admin"
ARG test_pass="admin#PASS"
ARG test_cert="cert.pem"
ARG test_certkey="privkey.pem"

ENV PROJECT_FOLDER=/opt/arturgontijo/${git_repo}

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

WORKDIR ${PROJECT_FOLDER}

ENV TEST_HOST=${test_host}
ENV TEST_PORT=${test_port}
ENV TEST_USER=${test_user}
ENV TEST_PASS=${test_pass}
ENV TEST_CERT=${test_cert}
ENV TEST_CERTKEY=${test_certkey}

CMD python3 \
    test.py \
    --host ${TEST_HOST} \
    --port ${TEST_PORT} \
    --username ${TEST_USER} \
    --password ${TEST_PASS} \
    --cert ${TEST_CERT} \
    --certkey ${TEST_CERTKEY}
