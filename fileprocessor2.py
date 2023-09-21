#!/usr/bin/env python3
import sys

line_data= []
print("Printing out User Data:\n")

for line in sys.stdin:
    line = line.strip() 
    if line.startswith("#"):
        print(f"{line[1:].split(':')[0].strip()} is skipped because it starts with a hashtag (is commented out)")
        continue
    split_line = line.split(":")
    line_data.append(split_line)

for lines in line_data:
    username, password, userid, groupid = lines
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("\nEnd of User Data")

