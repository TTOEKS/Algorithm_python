#!/bin/bash

DEBUG_MODE=""
WARN_FLAG="-Wall -Wextra -Wuninitialized"

if [ ${#} -eq 1 ] && [ "${1}" == "-D" ]; then
  DEBUG_MODE="-DDEBUG"
  echo "DEBUG MODE ON"
fi

LAST_MODI_FILE=`ls -lt ../ |grep "\.c"| tr -s ' ' | head -n1| cut -d " " -f9`
DST_FILE=`echo ${LAST_MODI_FILE} | cut -d "." -f1`
EXTENSION=`echo ${LAST_MODI_FILE} | cut -d "." -f2`

DELETE_LIST=`find . ! -path . -type d -o -type f -maxdepth 1| grep -vE "\.c|\.sh|\.swp|test"`

for LIST in ${DELETE_LIST}
do
  rm -rf ${LIST}
done


echo "Copmile ${LAST_MODI_FILE} to ${DST_FILE}..."
echo "Extension: ${EXTENSION}"


if [[ "c" == ${EXTENSION} ]]; then
  echo "Detect language: C lang"
  gcc ../${LAST_MODI_FILE} ${DEBUG_MODE} ${WARN_FLAG} -std=c99  -g -o ./${DST_FILE} 
  ./${DST_FILE}
elif [[ "cpp" == ${EXTENSION} ]]; then
  echo "Detect language: C++"
  g++ ../${LAST_MODI_FILE} ${DEBUG_MODE} ${WARN_FLAG} -std=c++17 -g -o ./${DST_FILE} 
  ./${DST_FILE}
else
  echo "Unsupported extension: ${LAST_MODI_FILE}"
  exit 0
fi

