#!/bin/bash

# Check if the URL and filename arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

url="$1"
filename="$2"
if [ ! -f "$filename" ]; then
    echo "File '$filename' not found."
    exit 1
fi
response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$filename" "$url")
echo "$response"
