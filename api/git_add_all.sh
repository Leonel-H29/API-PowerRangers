#!/bin/bash

git add .

echo -n "- Ingrese un mensaje para el nuevo commit: "
read message

git commit -m "$message"

git push origin $(git branch --show-current)

git log
