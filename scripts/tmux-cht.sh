#!/usr/bin/env bash
lanuages=`echo "rust cpp c nodejs typescript golang lua" | tr ' ' '\n'`
core_utils=`echo "find sed awk tr git" | tr ' ' '\n'`

selected=`printf "$lanuages\n$core_utils" | fzf`
read -p "Enter Query: " query

if printf $lanuages | grep -qs $selected; then
    tmux neww bash -c "echo \"curl cht.sh/$selected/$query/\" & curl cht.sh/$selected/$query & while [ : ]; do sleep 1; done"
else
    tmux neww bash -c "curl -s cht.sh/$selected~$query | less"
fi
