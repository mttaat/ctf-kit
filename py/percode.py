#!/usr/bin/python3
#
# Copyright (c) 2019 mttaat <mttaat@protonmail.com>. All Rights Reserved.
# This file licensed under the GPLv3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# percode v0.1
# percent encode/decode arbitrary strings
#
# usage: $ python percode.py -e '<STRING>'
# usage: $ python percode.py -d %3c%53%54%52%49%4e%47%3e
#
# # # # # # # # 
#
# @mttaat
# https://mttaat.net
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


import sys
import re

usage="python percode.py (-e,-d) '<STRING>'"

if len(sys.argv) < 3:
 print(usage)
 sys.exit()

if sys.argv[1] == "-e":
 un = sys.argv[2]
 un = str(un)
 en = ""
 for ch in un:
  ch = str(ch)
  en += "%" + str(ch.encode("hex"))
 print(en)
elif sys.argv[1] == "-d":
 en = sys.argv[2]
 en = en.replace("%", "")
 un = str(en.decode("hex"))
 print(un)
else:
 print(usage)
 exit
