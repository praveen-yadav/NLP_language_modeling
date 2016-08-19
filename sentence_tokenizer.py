#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import codecs
from nltk.tokenize import sent_tokenize

if len(sys.argv) < 2:
    print('Usage: python tokenizer.py file_name')
    sys.exit()
file_name = sys.argv[1]
content = codecs.open(file_name,"r","utf-8").read()
mystring = content.replace('\n', ' ').replace('\r', '')
listofsentences = sent_tokenize(mystring)
outfile = codecs.open("input", "w", "utf-8")
for sentence in listofsentences:
	sentence = re.sub(r'\W+', ' ', sentence)
	outfile.write("<s> ")
	listofwords = sentence.split(" ")
	for word in listofwords:
		outfile.write(word.lower())
		outfile.write(" ")
	outfile.write("</s> ")

outfile.close()    