#!/bin/bash

LAST_MODI_FILE=`ls -lt ../ |grep "\.c"| tr -s ' ' | head -n1| cut -d " " -f9`
DST_FILE=`echo ${LAST_MODI_FILE} | cut -d "." -f1`

DELETE_LIST=`find . -type f | grep -vE "\.c|\.sh|\.swp"`

rm -r ${DELETE_LIST}

echo "Copmile ${LAST_MODI_FILE} to ${DST_FILE}..."
gcc ../${LAST_MODI_FILE} -g -o ./${DST_FILE}

