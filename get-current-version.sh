#!/bin/bash

# This returns the last tag. $1 is the value to return if there are no tags.

IF_MISSING=$1
NUMBER_OF_TAGS=$(git tag | wc -l)
if [ $NUMBER_OF_TAGS -gt 0 ]; then
  echo $(git tag | tail -n1)
else
  echo "$IF_MISSING"
fi
