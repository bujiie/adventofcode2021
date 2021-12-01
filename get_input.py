#!/usr/bin/env python3

from sys import argv
from urllib.request import Request, urlopen

day=argv[1]

config_lookup={}
# Read the 'config' file and load them into a dict for quick
# lookups throughout the code.
with open("config") as fp:
	for line in fp:
		entry=[x.strip() for x in line.split("=")]
		config_lookup[entry[0]]=entry[1]

# Header matches what gets sent to the endpoint when viewing
# input the browser. The session token can be found in the 
# adventofcode.com session cookie.
headers={"Cookie": f"session={config_lookup['session']}"}
aoc_url=f"https://adventofcode.com/{config_lookup['year']}/day/{day}/input"
response=urlopen(Request(aoc_url, headers=headers))

with open("in", "wb") as fp:
	fp.write(response.read())
