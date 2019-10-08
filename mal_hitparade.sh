#!/bin/sh

#Gets the location of the .bz2 file to be parsed
FILE_LOCATION=$1

bzcat $FILE_LOCATION |
grep '^[അ - ഃ]' |
sed 's/[0-9]//g' |
tr -d "[:alnum:]<>[]{}/|.:\"&_();#!',*=\-" |
tr ' ' '\012' |
sort -f |
uniq -c |
sort -nr > hitparadetest.txt
