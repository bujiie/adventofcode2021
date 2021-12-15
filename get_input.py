#!/usr/bin/env python3

from sys import argv, exit
from urllib.request import Request, urlopen

if len(argv) < 2:
    print("A day number is required.")
    exit(1)

day = argv[1]

config_lookup={}
# Read the 'config' file and load them into a dict for quick lookups 
# throughout the code.
with open("config") as fp:
	for line in fp:
		key, value=[x.strip() for x in line.split("=")]
		config_lookup[key]=value

SESSION_KEY = 'session'
YEAR_KEY = 'year'
# Header matches what gets sent to the endpoint when viewing input the browser. 
# The session token can be found in the adventofcode.com session cookie.
if SESSION_KEY not in config_lookup:
    print("A session token must be specified in the config file.")
    exit(1)

if YEAR_KEY not in config_lookup:
    print("A year must be specified in the config file.")
    exit(1)

session, year = config_lookup['session'], config_lookup['year']

headers={"Cookie": f"session={session}"}
aoc_url=f"https://adventofcode.com/{year}/day/{day}/input"
response=urlopen(Request(aoc_url, headers=headers))

with open("in", "wb") as fp:
    fp.write(response.read())
