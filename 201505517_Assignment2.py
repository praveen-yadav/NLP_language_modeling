#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import codecs
from random import randint
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

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
	



#sentece generataion using bigram
print "1. for any given word/token can you estimate, whether that is the sentence-ending token. ?"
print "2. sentece generataion"
print "3. plot curve"
print "4. exit"
print "5. Print top 40 n-gram"
choice = int(raw_input("Enter choice:"))
if choice==5:
	gram = int(raw_input("Enter n of n-gram to plot:"))
	i=0
	if gram==1: 
			for w in sorted(unigram_dict, key=unigram_dict.get, reverse=True):
			  if w.split(' ')[0]=="</s>":
				  i+=1
				  if i==40:
				  	break
					print w, unigram_dict[w]
	elif gram==2:
		for w in sorted(bigram_dict, key=bigram_dict.get, reverse=True):
		  if w.split(' ')[1]=="</s>":
			  i+=1
			  if i==40:
			  	break
			  print w, bigram_dict[w]
	elif gram==3:
		i=0
		for w in sorted(trigram_dict, key=trigram_dict.get, reverse=True):
			if w.split(' ')[2]=="</s>":
			  i+=1
			  if i==40:
			  	break
			  print w, trigram_dict[w]			
	elif gram==4:
		i=0
		for w in sorted(quadgram_dict, key=quadgram_dict.get, reverse=True):
			if w.split(' ')[3]=="</s>":
			  i+=1
			  if i==40:
			  	break
			  print w, quadgram_dict[w]			
	elif gram==5:
		i=0
		for w in sorted(pentagram_dict, key=pentagram_dict.get, reverse=True):
			if w.split(' ')[4]=="</s>":
			  i+=1
			  if i==40:
			  	break
			  print w, pentagram_dict[w]
	elif gram==6:
		i=0
		for w in sorted(hexagram_dict, key=hexagram_dict.get, reverse=True):
			if w.split(' ')[5]=="</s>":
			  i+=1
			  if i==40:
			  	break
			  print w, hexagram_dict[w]


if choice==3:
	gram = int(raw_input("Enter n of n-gram to plot:"))
	f1 = open('rankvsfrequency.csv', 'w')
	f1.write("\"rank\";\"frequency\"\n")
	i=0
	if gram==1: 
		dictionary=unigram_dict
	elif gram==2:
		dictionary=bigram_dict
	elif gram==3:
		dictionary=trigram_dict
	elif gram==4:
		dictionary=quadgram_dict
	elif gram==5:
		dictionary=pentagram_dict
	elif gram==6:
		dictionary=hexagram_dict
	for w in sorted(dictionary, key=dictionary.get, reverse=True):
		i+=1
		if i==40:
			break
		f1.write(str(i)+';')
		if gram==1: 
			f1.write(str(unigram_dict[w]))
		elif gram==2:
			f1.write(str(bigram_dict[w]))
		elif gram==3:
			f1.write(str(trigram_dict[w]))
		elif gram==4:
			f1.write(str(quadgram_dict[w]))
		elif gram==5:
			f1.write(str(pentagram_dict[w]))
		elif gram==6:
			f1.write(str(hexagram_dict[w]))
		f1.write('\n')

	f1.close()
	data = np.genfromtxt('./rankvsfrequency.csv', delimiter=';', skip_header=1,
                     names=['rank', 'frequency'])
	# print data
	fig = plt.figure()

	for i in range(len(data)):
		plt.scatter(data[i][0],data[i][1])
	plt.show()
	fig.savefig(str(gram)+"-gram")
	print "File generated."
if choice==4:
	sys.exit()
if choice==2:
	while 1:
			
		gram = int(raw_input("Enter n(2<=n<=6) using which to generte sentece:"))
		times = int(raw_input("How many senteces:"))
		print "Random generated sentece:"
		for x in range(0,times):
			finalsentence = []
			intermediatelist = []
			prevword="<s>"
			if gram==2:
					for listitem in bigramlist:
						if listitem.split(' ')[0]==prevword:
							intermediatelist.append(listitem)						
			if gram==3:
				for listitem in trigramlist:
					if listitem.split(' ')[0]==prevword:
						intermediatelist.append(listitem)						

			if gram==4:
				for listitem in quadgramlist:
					if listitem.split(' ')[0]==prevword:
						intermediatelist.append(listitem)						

			if gram==5:
				for listitem in pentagramlist:
					print listitem
					if listitem.split(' ')[0]==prevword:
						intermediatelist.append(listitem)						
			if gram==6:
				for listitem in hexagramlist:
					if listitem.split(' ')[0]==prevword:
						intermediatelist.append(listitem)	
			randomnumber =randint(0,len(intermediatelist)-1)

			for j in intermediatelist[randomnumber].split(' '):
				finalsentence.append(j)	

			prevword = []
			for j in range(0,gram-1):
				prevword.append(finalsentence[ len(finalsentence)-gram+j+1])


			while 1:
				if gram==2:
					for listitem in bigramlist:
						if listitem.split(' ')[0:gram-1]==prevword[0:gram-1]:
							intermediatelist.append(listitem)						
				if gram==3:
					for listitem in trigramlist:
						if listitem.split(' ')[0:gram-1]==prevword[0:gram-1]:
							#print listitem
							intermediatelist.append(listitem)						

				if gram==4:
					for listitem in quadgramlist:
						if listitem.split(' ')[0:gram-1]==prevword[0:gram-1]:
							intermediatelist.append(listitem)						
				if gram==5:
					for listitem in pentagramlist:
						if listitem.split(' ')[0:gram-1]==prevword[0:gram-1]:
							intermediatelist.append(listitem)	
				if gram==6:
					for listitem in hexagramlist:
						if listitem.split(' ')[0:gram-1]==prevword[0:gram-1]:
							intermediatelist.append(listitem)									
						
				
				try:
					randomnumber =randint(0,len(intermediatelist)-1)
				except Exception , e:
					#print str(randomnumber)+">="+str(len(intermediatelist))
					finalsentence.append("</s>")
					break
				if "<s>" in intermediatelist[randomnumber].split(' ')[0:len(intermediatelist)-1]:
					continue
				finalsentence.append(intermediatelist[randomnumber].split()[-1])	
				prevword.pop(0)
				prevword.append(intermediatelist[randomnumber].split()[-1])
					
				
				del intermediatelist[:]
				
				if finalsentence[-1]=="</s>":
					break
			
			print ' '.join(finalsentence)	
			pass
			

if choice==1:
	print "\nFor any given word/token can you estimate, whether that is the sentence-ending token ?"
	n = int(raw_input("\nEnter Number of Queries:"))
	for i in xrange(n):
		token =  raw_input("\nEnter String:").lower()
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
			print "No sentence ends with this token so by smoothing"
			print float(float(1)/float(len(unigram_dict)))


	#1/dictionary size for normalize everything