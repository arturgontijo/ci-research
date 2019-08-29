#! /bin/bash

TARGET_FILE=$1

if [ ! "$TARGET_FILE" ]
    then
    # "Invalid path to dir|file!"
    echo 0
fi

# Last Git Commit.
LATEST_COMMIT=$(git rev-parse HEAD)

# Last Git Commit where dir|file was changed.
TARGET_FILE_COMMIT=$(git log -1 --format=format:%H --full-diff ${TARGET_FILE})

if [ "$TARGET_FILE_COMMIT" = "$LATEST_COMMIT" ]
    then
    # "${TARGET_FILE} has changed!"
    echo 1
elif [ "$TARGET_FILE_COMMIT" = "" ]
    then
    # "${TARGET_FILE} not commited yet!"
    echo 0
else
    # "${TARGET_FILE} has not changed."
    echo 0
fi
