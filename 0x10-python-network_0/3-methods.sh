#!/bin/bash
# displays all HTTP methods the server will accept for URL
curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d ":" -f 2- | tr -d '\r\n'
