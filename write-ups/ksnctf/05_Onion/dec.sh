#!/bin/bash
set -eu

readonly FILENAME="onion.txt"

main() {
    local a=$(cat ${FILENAME})
    while :
    do
        # 改行と空白を削除してからデコード
        a=$(echo ${a} | sed -z 's/\n//g' | sed -z 's/ \+//g' | base64 -d)
        echo ${a}
    done
}

main
