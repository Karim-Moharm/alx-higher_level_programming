#!/bin/bash
# a Bash script that takes in a URL as an argument, sends a GET request to the URL,
## and displays the body of the response

header="X-School-User-Id: 98"
curl -H "$header" $1
