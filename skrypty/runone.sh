#!/bin/bash
read -p "Które: " number
filename="zadanie-$number.py"
if [ -f "./zadania/$filename" ]; then
    python "./zadania/$filename"
else
    echo "Niema takiego :("
fi