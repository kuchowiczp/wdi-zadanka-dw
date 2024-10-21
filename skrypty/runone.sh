#!/bin/bash
read -p "Które (2~10 / d1): " number
filename="zadanie-$number.py"
if [ -f "./zadania/$filename" ]; then
    python "./zadania/$filename"
else
    echo "Niema takiego :("
fi