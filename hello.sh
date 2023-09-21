#!/bin/bash


# Declare an array of strings
listOfUsers=("User1" "User2" "User3")

a=2
b=2
c=$((a + b))

for user in "${listOfUsers[@]}"; do
       	echo "$user"
done

echo "Bash says: Hello, World!"
echo "$a + $b = $c"
