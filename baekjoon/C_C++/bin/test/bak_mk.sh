#!/bin/bash

DEBUG_MODE=""

if [ ${#} -eq 1 ] && [ "${1}" == "-D" ]; then
  DEBUG_MODE="-DDEBUG"
  echo "DEBUG MODE ON"
fi

LAST_MODI_FILE=`ls -lt ./ |grep "\.c"| tr -s ' ' | head -n1| cut -d " " -f9`
DST_FILE=`echo ${LAST_MODI_FILE} | cut -d "." -f1`

DELETE_LIST=`find . ! -path . -type d -o -type f -maxdepth 1| grep -vE "\.c|\.sh|\.swp|test"`


echo "Copmile ${LAST_MODI_FILE} to ${DST_FILE}..."

gcc ./${LAST_MODI_FILE} ${DEBUG_MODE}  -g -o ./${DST_FILE} 
./${DST_FILE}
