#!/usr/bin/env bash

day=$1

./open_browser.py $day

challenge_dir="day${1}"

mkdir $challenge_dir
./get_input.py $day
mv "in" "${challenge_dir}/in"

cp __template.py "${challenge_dir}/a.py"
cd $challenge_dir
chmod 755 a.py

