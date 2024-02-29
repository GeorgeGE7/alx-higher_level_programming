#!/bin/bash
# Get only statuis code as output
curl -s -w "%{http_code}" -o /dev/null "$1"
