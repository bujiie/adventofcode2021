#!/usr/bin/env bash

day=$1

challenge_dir="day${1}"

mkdir $challenge_dir
cp __template.py "${challenge_dir}/${day}.py"
cd $challenge_dir
chmod 755 "${day}.py"

touch "in" 
