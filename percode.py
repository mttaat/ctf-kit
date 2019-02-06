#!/usr/bin/python3
#
# Copyright (c) 2019 mttaat <mttaat@protonmail.com>. All Rights Reserved.
# This file licensed under the GPLv3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# percode v0.1
# percent encode/decode arbitrary strings
#
# encode usage: $ python percode.py -e '<STRING>'
# decode usage: $ python percode.py -d %3c%53%54%52%49%4e%47%3e
#
# # # # # # # # 
#
# @mttaat
# https://mttaat.net
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import sys

if sys.argv[1] == "-e":
 # encode
 un = sys.argv[2]
 un = str(un)
 en = ""
 for ch in un:
  ch = str(ch)
  en += "%" + str(ch.encode("hex"))
 print(en)
elif sys.argv[1] == "-d":
 # decode
 en = sys.argv[2]
 en = en.replace("%", "")
 un = str(en.decode("hex"))
 print(un)
else:
 print("invalid input")
