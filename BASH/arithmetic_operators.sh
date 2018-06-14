#!/bin/sh
# Perform arithmetic operations
# Read inputs
read input1
read input2
# -eq = equal to operator
# -lt = less than operator
# -gt = greater than operator
if [ $input1 -eq $input2 ]
then
echo "X is equal to Y"
elif [ $input1 -gt $input2 ]
then
echo "X is greater than Y"
else
echo "X is less than Y"
fi

