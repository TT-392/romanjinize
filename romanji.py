#!/bin/python3.7
from pykakasi import kakasi
import sys 


mode = 'H' 
offset = 0 

text = ""

if (len(sys.argv) > 1): 
    if (str(sys.argv[1]) == "-r"): # set mode to romanji if -r is present
        mode = 'a' 
        offset = 1 

kakasi = kakasi()
kakasi.setMode("H",mode) # Hiragana to ascii, default: no conversion
kakasi.setMode("K",mode) # Katakana to ascii, default: no conversion
kakasi.setMode("J",mode) # Japanese to ascii, default: no conversion
kakasi.setMode("s", True) # add space, default: no separator
conv = kakasi.getConverter()

if (len(sys.argv) > offset + 1): # check if there are command line arguments
    text = sys.argv[offset + 1]
    print(conv.do(text))
else: # else switch to pipe mode
    while 1:
        try: 
            text = input()
            print(conv.do(text))
        except:
            break
