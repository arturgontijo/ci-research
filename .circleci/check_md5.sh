#! /bin/bash

TARGET_FILE=$1
RET_VAL=0

CURRENT_MD5=$(md5sum "${TARGET_FILE}")
REMOTE_MD5=$(ssh -o "StrictHostKeyChecking no" "${SSH_USER}"@"${SSH_HOST}" docker exec "${PROD_TAG}""${DOCKER_CONTAINER_NAME}" md5sum "${TARGET_FILE}")

if [ "$CURRENT_MD5" != "$REMOTE_MD5" ]
    then
    # "${TARGET_FILE} has changed!"
    RET_VAL=1
fi

echo ${RET_VAL}
