#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo 'usage : '
    echo '       ./mkfile.sh dir_name [file_name]'
    echo '       ./mkfile.sh dir_name [url]'
    exit -1
fi

if [[ ! -d "$1" ]]; then
    mkdir -p "$1"
fi

f_url="$2"
f_name="$f_url"
if [[ "$f_name" =~ ^http ]]; then
    my_array=($(echo $f_name | tr "/" "\n"))
    f_name="${my_array[@]: -1:1}"
    f_name=$(echo "$f_name" | sed 's/-/_/g')
fi

if [[ -f "$1/$f_name.py" ]]; then
    rm "$1/$f_name.py"
fi

cat >> "$1/$f_name.py" <<EOF
#!/usr/local/bin/python3

def $f_name():
    """
    $f_url

    Time :
    Space:
    Note :
    """
    pass


def run():
    pass


if __name__ == '__main__':
    run()

EOF

chmod +x "$1/$f_name.py"
