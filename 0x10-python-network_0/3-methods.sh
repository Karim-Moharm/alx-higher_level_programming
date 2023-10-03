#!/bin/bash
# displays all HTTP methods the server will accept for URL
curl -s -X OPTIONS "$1"
