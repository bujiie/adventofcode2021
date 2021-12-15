#!/usr/bin/env python3

from sys import argv, exit
import webbrowser

if len(argv) < 2:
    print("A day number is required.")
    exit(1)

day=argv[1]

config_lookup={}
# Read the 'config' file and load them into a dict for quick lookups 
# throughout the code.
with open("config") as fp:
	for line in fp:
		key, value=[x.strip() for x in line.split("=")]
		config_lookup[key]=value

YEAR_KEY = 'year'
if YEAR_KEY not in config_lookup:
    print("A year must be defined in the config file.")
    exit(1)

year = config_lookup['year']
webbrowser.open(f"https://adventofcode.com/{year}/day/{day}")
