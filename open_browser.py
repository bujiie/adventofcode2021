#!/usr/bin/env python3

from sys import argv
import webbrowser

day=argv[1]

config_lookup={}
# Read the 'config' file and load them into a dict for quick
# lookups throughout the code.
with open("config") as fp:
	for line in fp:
		entry=[x.strip() for x in line.split("=")]
		config_lookup[entry[0]]=entry[1]

webbrowser.open(f"https://adventofcode.com/{config_lookup['year']}/day/{day}")
