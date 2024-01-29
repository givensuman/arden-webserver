#!/bin/bash

# Kill any process running on port 8080
fuser -k 28804/tcp

# Start server and DNS tunnel
nohup python3 server.py & cloudflared/cloudflared tunnel --url localhost:28804 &


