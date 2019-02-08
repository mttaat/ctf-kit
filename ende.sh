#!/bin/bash
#
# Copyright (c) 2019 mttaat <mttaat@protonmail.com>. All Rights Reserved.
# This file licensed under the GPLv3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ende 
# general purpose encoder/decoer
#
# usage: $ ./endecoder.sh [--hex, --base64, --percent] [-e (encode), -d (decode)] 'string'"
#
# # # # # # # # 
#
# @mttaat
# https://mttaat.net
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


function usage() {
 echo "endecoder.sh [--hex, --base64, --percent] [-e (encode), -d (decode)] 'string'"
 exit
}

if [ $# -lt 3 ]; then
 usage
fi

if [ "$2" != "-e" ] && [ "$2" != "-d" ]; then
 usage
fi

# TODO: Refactor branching logic
# TODO: Add support for multiple iterations (with one command)
# TODO: Add more encoding methods (UTF-8, HTML, UUEncoding, Morse, etc)
# TODO: Move entirely to platform independent python (ie: no reliance on xxd, base64, etc)

if [ $1 == "--base64" ]; then
 if [ "$2" == "-e" ]; then
  action=""
 elif [ "$2" == "-d" ]; then
  action="--decode"
 else
  usage
 fi
 result=`echo $3 | base64 $action`
 echo $result
elif [ $1 == "--hex" ]; then
 if [ "$2" == "-e" ]; then
  result=`echo $3 | tr -d '\n' | xxd -p`
 elif [ "$2" == "-d" ]; then
  result=`echo $3 | xxd -r -p` 
 fi
 echo $result
elif [ $1 == "--percent" ]; then
 result=`python py/percode.py $2 $3`
 echo $result
fi
