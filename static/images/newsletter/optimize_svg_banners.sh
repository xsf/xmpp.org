#!/bin/bash

# Script to clean and minimize svg files, it uses
# - Scour https://github.com/scour-project/scour
# - Xmlstarlett https://xmlstar.sourceforge.net/

for fin in *_source.svg;
do
  fout="${fin/_source/}"
  echo "${fout}"
  scour -i "${fin}" -o "${fout}"
  xmlstarlet edit --inplace  --omit-decl -N x=http://www.w3.org/2000/svg   --delete  '//x:text'  ${fout}
done 
