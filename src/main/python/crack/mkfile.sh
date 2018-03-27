#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo 'Usage : ./mkfile.sh dir_name file_name'
    exit -1
fi

if [[ ! -d "$1" ]]; then
    mkdir "$1"
fi

if [[ -f "$1/$2.py" ]]; then
    rm "$1/$2.py"
fi

cat >> "$1/$2.py" <<EOF

def $2():
    '''

    '''
    pass

def run():
    pass

if __name__ == '__main__':
    run()

EOF