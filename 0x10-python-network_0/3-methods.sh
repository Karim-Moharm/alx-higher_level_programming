#!/bin/bash
# displays all HTTP methods the server will accept for URL
curl -sI -X OPTIONS "$1" | grep -i "Allow" | awk '{$1=""; sub(/^ /, ""); print $0}' 
