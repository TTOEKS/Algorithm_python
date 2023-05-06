#!/bin/bash

LAST_MODI_FILE=`ls -lt |grep "\.c"| tr -s ' ' | head -n1| cut -d " " -f9`
DST_FILE=`echo ${LAST_MODI_FILE} | cut -d "." -f1`


echo "Copmile ${LAST_MODI_FILE} to ${DST_FILE}..."
gcc ${LAST_MODI_FILE} -o ${DST_FILE}

