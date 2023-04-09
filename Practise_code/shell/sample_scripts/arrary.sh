#!/bin/sh

arr=("apple" "orange" "banana" "guava") # Define an arrary. in shell you use space unlike in python where you use "," in between array
echo ${arr} # Prints first element

echo ${arr[0]}
echo
echo ${arr[1]}

echo ${arr[@]}