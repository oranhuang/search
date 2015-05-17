#!/usr/bin/python
#print "hello world"
#f = open("/var/log/boot.log")
#lines = f.readlines();
#f.close()
#for line in lines:
#	print line
###########################
#print "I am a fish".split()
###########################
#f = open("test.txt", "w")
#f.write("you are damm good!!\n")
#f.close();
##########################
#import sys
#print sys.argv
#print "now where are we?"
#########################
#t = [1,2,3]
#print 1 in t
#########################
#import urllib
#print dir(urllib)
#yahoo = urllib.urlopen("http://www.yahoo.com.tw")
#print yahoo.read()
########################
#num = [3, 5, 7]
#num.reverse();
#for i in num:
#	print(i)
########################
import os
os.chdir(r'/home/oran/')
print os.getcwd();
f = open('file.html', 'r');
for i in f:
	print i
