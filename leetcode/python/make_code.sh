#!/bin/zsh

MODULE_FILES=(
"collections"
"heapq"
"functools"
"itertools"
"re"
"sys"
"math"
"bisect"
"pprint"
)

HEADER_DATAS=(
"from typing import *"
)


function make_header() {
  for MODULE_FILE in ${MODULE_FILES[@]}; do
    echo "import ${MODULE_FILE}"
  done

  for HEADER_DATA in ${HEADER_DATAS[@]}; do
    echo "${HEADER_DATA}"
  done

}

function make_body() {
  echo 'if __name__=="__main__":'
  echo '\ttestcase = []'
  echo '\tprint("hello world")'
  echo
  echo '\tsol = Solution()'
  echo '\tprint(sol)'
}

#### MAIN

if [ ${#} -ne 1 ]; then
  echo "You should input python file name!"
  exit -1
fi

if [ "${1#*.}" != "py" ]; then
  echo "This script only support python files"
  echo "You should input file type .py"
  echo "ex) helloworld.py"
fi

FILE_NAME="${1}"
cat /dev/null > ${FILE_NAME}
make_header >> ${FILE_NAME}
echo >> ${FILE_NAME}
echo >> ${FILE_NAME}
make_body >> ${FILE_NAME}

nvim "${FILE_NAME}"
