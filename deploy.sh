#!/bin/bash
cd ~/HackathonVIScon22/api
tmux new-session -d -s my_session 'sudo python3 -m uvicorn main:app --host 0 --port 80'
