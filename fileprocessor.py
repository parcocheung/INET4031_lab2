#!/usr/bin/env python3

with open('fileprocessor.input', 'r') as file:
    lines = file.readlines()
list_line = []

print("Printing out User Data:\n")

for line in lines:
   if line.startswith("#"):
       print(f"{line[1:].split(':')[0].strip()} is skipped because it starts with a hashtag (is commented out)")
       continue
   split_line = line.split(":")
   list_line.append(split_line) 
 
  
    
      
for user in list_line:
    username, password, userid, groupid = user
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("\nEnd of User Data")
