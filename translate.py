#!/usr/bin/env python3

import os, sys
untranslated = ""
mapping = {"A":"4",
           "B":"|3",
           "C":"(",
           "D":"|)",
           "E":"3",
           "F":"|=",
           "G":"9",
           "H":"|-|",
           "I":"!",
           "J":"_|",
           "K":"|<",
           "L":"|_",
           "M":"/\\/\\",
           "N":"|\\|",
           "O":"0",
           "R":"|2",
           "S":"5",
           "T":"7",
           "U":"|_|",
           "V":"\\/",
           "W":"\\/\\/",
           "X":"><",
           "Y":"`/",
           "Z":"2"}

try:
  f = open(sys.argv[len(sys.argv) - 1], "r")
  untranslated_lst = f.read().split("\n")
  for line in untranslated_lst:
    line_split = list(line.upper())
    for x in range(0, len(line_split)):
      try:
        line_split[x] = mapping[line_split[x]]
      except:
        pass 
    line = ''.join(line_split)
    print(line)
except:
  print("youre not 1337 to use this software. try harder n00b")
  sys.exit(1)





