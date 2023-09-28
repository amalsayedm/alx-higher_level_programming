#!/bin/bash
# Make request and display response size
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
