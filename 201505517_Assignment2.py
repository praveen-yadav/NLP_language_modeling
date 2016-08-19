#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import codecs

if len(sys.argv) < 2:
    print('Usage: python tokenizer.py file_name')
    sys.exit()
file_name = sys.argv[1]
content = codecs.open(file_name,"r").read()
content = content.split('\n')
unigram_dict = {}
unigramlist = []
for line in content:
	#print line	
	line = line.strip(" ")
	words = line.split(" ")
	for word in words:		
		if not word:
			continue
		unigramlist.append(word)
		if word in unigram_dict:
			unigram_dict[word]+=1
		else: 
			unigram_dict[word]=1

#Print top 40 unigrams
f1 = open('unigram_list.csv', 'w')
f1.write("\"word\";\"frequency\"\n")
i=0
for w in sorted(unigram_dict, key=unigram_dict.get, reverse=True):
  	  i+=1
	  if i==40:
	  	break
	  #print str(unigram_dict[w])+' '+w
	  # print w+' , '+str(unigram_dict[w])
	  f1.write(w+';'+str(unigram_dict[w])+'\n')

f1.close()

	
bigramlist = []
i=0
j=1
lenofuniqunigrams = len(unigramlist)
while(j<lenofuniqunigrams):
	bigramlist.append(unigramlist[i]+' '+unigramlist[j])
	i+=1
	j+=1

bigram_dict = {}
for bigram in bigramlist:
	if bigram in bigram_dict:
		bigram_dict[bigram]+=1
	else:
		bigram_dict[bigram]=1

# i=0
# for w in sorted(bigram_dict, key=bigram_dict.get, reverse=True):
#   if w.split(' ')[1]=="</s>":
# 	  i+=1
# 	  if i==40:
# 	  	break
# 	  print w, bigram_dict[w]
f1 = open('bigram_list.csv', 'w')
f1.write("\"word\";\"frequency\"\n")
i=0
for w in sorted(bigram_dict, key=bigram_dict.get, reverse=True):
  	  
  	  if w.split(' ')[1]=="</s>":
  	  	i+=1
	  	if i==40:
	  		break
	  	f1.write(w.split(' ')[0]+';'+str(bigram_dict[w])+'\n')
f1.close()

trigramlist = []
i=0
j=1
k=2
lenofuniqunigrams = len(unigramlist)
while(k<lenofuniqunigrams):
	trigramlist.append(unigramlist[i]+' '+unigramlist[j]+' '+unigramlist[k])
	i+=1
	j+=1
	k+=1	

trigram_dict = {}
for trigram in trigramlist:
	if trigram in trigram_dict:
		trigram_dict[trigram]+=1
	else:
		trigram_dict[trigram]=1
	

# i=0
# for w in sorted(trigram_dict, key=trigram_dict.get, reverse=True):
# 	if w.split(' ')[2]=="</s>":
# 	  i+=1
# 	  if i==40:
# 	  	break
# 	  print w, trigram_dict[w]

f1 = open('trigram_list.csv', 'w')
f1.write("\"word\";\"frequency\"\n")
i=0
for w in sorted(trigram_dict, key=trigram_dict.get, reverse=True):
  	  splitted = w.split(' ')
  	  if splitted[2]=="</s>":
  	  	i+=1
	  	if i==40:
	  		break
	  	f1.write(splitted[0]+' '+splitted[1]+';'+str(trigram_dict[w])+'\n')
f1.close()

quadgramlist = []
i=0
j=1
k=2
l=3
lenofuniqunigrams = len(unigramlist)
while(l<lenofuniqunigrams):
	quadgramlist.append(unigramlist[i]+' '+unigramlist[j]+' '+unigramlist[k]+' '+unigramlist[l])
	i+=1
	j+=1
	k+=1
	l+=1	

quadgram_dict = {}
for quadgram in quadgramlist:
	if quadgram in quadgram_dict:
		quadgram_dict[quadgram]+=1
	else:
		quadgram_dict[quadgram]=1
	

# i=0
# for w in sorted(quadgram_dict, key=quadgram_dict.get, reverse=True):
# 	if w.split(' ')[3]=="</s>":
# 	  i+=1
# 	  if i==40:
# 	  	break
# 	  print w, quadgram_dict[w]
f1 = open('quadgram_list.csv', 'w')
f1.write("\"word\";\"frequency\"\n")
i=0
for w in sorted(quadgram_dict, key=quadgram_dict.get, reverse=True):
  	  splitted = w.split(' ')
  	  if splitted[3]=="</s>":
  	  	i+=1
	  	if i==40:
	  		break
	  	f1.write(splitted[0]+' '+splitted[1]+' '+splitted[2]+';'+str(quadgram_dict[w])+'\n')
f1.close()

pentagramlist = []
i=0
j=1
k=2
l=3
m=4
lenofuniqunigrams = len(unigramlist)
while(m<lenofuniqunigrams):
	pentagramlist.append(unigramlist[i]+' '+unigramlist[j]+' '+unigramlist[k]+' '+unigramlist[l]+' '+unigramlist[m])	
	if pentagramlist[-1].find("<s>")!=-1:
		del pentagramlist[-1]
	i+=1
	j+=1
	k+=1
	l+=1
	m+=1	

pentagram_dict = {}
for pentagram in pentagramlist:
	if pentagram in pentagram_dict:
		pentagram_dict[pentagram]+=1
	else:
		pentagram_dict[pentagram]=1
	

# i=0
# for w in sorted(pentagram_dict, key=pentagram_dict.get, reverse=True):
# 	if w.split(' ')[4]=="</s>":
# 	  i+=1
# 	  if i==40:
# 	  	break
# 	  # print w, pentagram_dict[w]

hexagramlist = []
i=0
j=1
k=2
l=3
m=4
n=5
lenofuniqunigrams = len(unigramlist)
while(n<lenofuniqunigrams):		
	hexagramlist.append(unigramlist[i]+' '+unigramlist[j]+' '+unigramlist[k]+' '+unigramlist[l]+' '+unigramlist[m]+' '+unigramlist[n])
	if hexagramlist[-1].find("<s>")!=-1:
		del hexagramlist[-1]
	# if len(hexagramlist)>0 and hexagramlist[-1].find("</s>")!=-1:
	# 	del hexagramlist[-1]
	i+=1
	j+=1
	k+=1
	l+=1
	m+=1
	n+=1	

hexagram_dict = {}
for hexagram in hexagramlist:
	if hexagram in hexagram_dict:
		hexagram_dict[hexagram]+=1
	else:
		hexagram_dict[hexagram]=1
	

i=0
for w in sorted(hexagram_dict, key=hexagram_dict.get, reverse=True):
	if w.split(' ')[5]=="</s>":
	  i+=1
	  if i==40:
	  	break
	  print w, hexagram_dict[w]

print "\nFor any given word/token can you estimate, whether that is the sentence-ending token ?"
n = int(raw_input("\nEnter Number of Queries:"))
for i in xrange(n):
	token = raw_input("\nEnter String:")
	tokens = token.split(' ')
	lenoftoken = len(tokens)
	try:
		if lenoftoken==1:
			print bigram_dict[token+' '+"</s>"]
			print unigram_dict[token]
			print float(float(bigram_dict[token+' '+"</s>"])/float(unigram_dict[token]))
		if lenoftoken==2:
			print trigram_dict[token+' '+"</s>"]
			print bigram_dict[token]
			print float(float(trigram_dict[token+' '+"</s>"])/float(bigram_dict[token]))
		if lenoftoken==3:
			print quadgram_dict[token+' '+"</s>"]
			print trigram_dict[token]
			print float(float(quadgram_dict[token+' '+"</s>"])/float(trigram_dict[token]))
		if lenoftoken==4:
			print pentagram_dict[token+' '+"</s>"]
			print quadgram_dict[token]
			print float(float(pentagram_dict[token+' '+"</s>"])/float(quadgram_dict[token]))
		if lenoftoken==5:
			print hexagram_dict[token+' '+"</s>"]
			print pentagram_dict[token]
			print float(float(hexagram_dict[token+' '+"</s>"])/float(pentagram_dict[token]))
	except Exception , e: 
		print "No sentence ends with this token"
