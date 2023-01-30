#!/usr/bin/env bash

workspaces=`ls ~/code/user`
selected=`printf "$workspaces" | fzf`

tmux new -s $selected -c ~/code/user/$selected ~/.scripts/tmux-ide.sh