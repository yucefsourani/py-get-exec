#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  get_exec.py
#  
#  Copyright 2015 youcef <youcef.m.sourani@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from __future__ import print_function
import os
import sys
import re
import six
import subprocess
from optparse import OptionParser

parser = OptionParser()
home=os.getenv("HOME")
application=["/usr/share/applications/","%s/.local/share/applications/"%home,"/usr/local/share/applications/"]


#get line after Exec=
def __get_exec(filee):
	with open(filee,"r") as myfile:
		for line in myfile.readlines():
			if line.startswith("Exec"):
				lineee=re.split("=",line)
				if len(lineee)>0:
					if len(lineee)>2:
						result=""
						for i in lineee[1:]:
							result+=i
						return result.replace("\n","")
					else:
						return lineee[1].replace("\n","")
				else:
					return None


#get all programes in categories and get Exec command 
def get_exec_by_categories(text=None):
	
	if isinstance(text, list)==False:
		sys.exit("Enter List argv")
	else:
		if not len(text)>=1:
			sys.exit("Enter one argv in list")
			
	text1=[]
	for word in text:
		if not isinstance(word, six.string_types):
			sys.exit("Enter String argv")
		elif word=="":
			sys.exit("Error Empty argv")
		else:
			if word not in text1:
				text1.append(word)
			
	result=[]
	
	for folder in application:
		if os.path.isdir(folder):
			for filee in os.listdir(folder):
				if os.path.isfile(os.path.join(folder,filee)):
					with open(os.path.join(folder,filee),"r") as myfile:
						for line in myfile.readlines():
							if line.startswith("Categories"):
								lineee=re.split("[= ;]",line)
								for word in text1:
									if word in lineee[1:-1]:
										if[os.path.join(folder,filee), __get_exec(os.path.join(folder,filee))] not in result:
											result.append([os.path.join(folder,filee), __get_exec(os.path.join(folder,filee))])

	return result



#get Exec command by name 
def get_exec_by_name(programe_name=None):
	
	if  isinstance(programe_name, list)==False:
		sys.exit("Enter List argv")
	else:
		if len(programe_name)!=1:
			sys.exit("Enter one argv in list")
		elif isinstance(programe_name[0], six.string_types)==False:
				sys.exit("Enter String argv")
		elif programe_name[0]=="":
			sys.exit("Enter one argv")
			
	result=[]
	for folder in application:
		if os.path.isdir(folder):
			check=subprocess.Popen("ls %s |grep -i %s"%(folder,programe_name[0]),stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
			stdout, stderr = check.communicate()
			stdout=stdout.split()
			for i in stdout:
				if  i!="" and i!=None:
					if[os.path.join(folder,i), __get_exec(os.path.join(folder,i))] not in result:
						result.append([os.path.join(folder,i), __get_exec(os.path.join(folder,i))])
						
	return result

#to print result get_exec_by_categories(text=None) line b line 
def print_bycategories(text):
	for line in get_exec_by_categories(text):
		print ("%s  :  %s\n"%(line[0],line[1]))
	
#to print result get_exec_by_name(programe_name=None) line b line	
def print_byname(name):
	for line in get_exec_by_name(name):
		print ("%s  :  %s\n"%(line[0],line[1]))






#exp1
print ("\n\nex1 :\n")
print_bycategories(["Network"])
#exp2
print ("\n\n\n\n\nex2 :\n")
print_byname(["firefox"])

