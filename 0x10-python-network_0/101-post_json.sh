#!/bin/bash
# Send JSON format request to spacific URI in the first arrg
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
