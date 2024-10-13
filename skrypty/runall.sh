#!/bin/bash
for filename in ./zadania/*.py; do
    echo "---- $filename ----"
    python "$filename"
done