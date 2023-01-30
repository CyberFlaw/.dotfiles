#!/usr/bin/env bash

tmux neww lf
tmux split-window lazygit
tmux select-pane -t 0
tmux select-window -t 0
hx .