#! /usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import argparse

def ext_pallet(ext,counte,tottal):
	types={"py":"Python",
	"pyc":"Python binary",
	"c":"C lang",
	"h":"C lang",
	"w":"C lang",
	"cpp":"C++",
	"cc":"C++",
	"hh":"C++",
	"cp":"C++",
	"c++":"C++",
	"hpp":"C++",
	"cxx":"C++",
	"cs":"C#",
	"pl":"Perl",
	"pm":"Perl",
	"t":"Perl",
	"html":"html+css",
	"htm":"html+css",
	"css":"html+css",
	"js":"JavaScript",
	"java":"Java",
	"class":"Java",
	"jar":"Java",
	"asm":"Assembler",
	"out":"C lang out files",
	"sh":"Bash",
	"bat":"MS Batch files",
	"cmd":"MS Batch files",
	"ps":"PowerShell",
	"ps1":"PowerShell",
	"rb":"Ruby",
	"exe":"MS binary",
	"go":"GO lang",
	"php":"PHP",
	"php5":"PHP",
	"php7":"PHP",
	"php8":"PHP",
	"sql":"SQL script",
	"zip":"Compressed Data",
	"gz":"Compressed Data",
	"xz":"Compressed Data",
	"7z":"Compressed Data",
	"tgz":"Compressed Data",
	"rar":"Compressed Data",
	"pas":"Pascal"}
	count=[]
	extname=[]
	for i in ext:
		try:
			e=types[i]
		except:
			pass
		else:
			if extname.count(e)==0:
				count.append(counte[ext.index(i)])
				extname.append(e)
			else:
				index=extname.index(e)
				count[index]+=counte[ext.index(i)]
	out=""
	for i in range(len(extname)):
		out+="{}: {} ({:.2f}%)\n".format(extname[i],count[i],float(count[i]*100)/float(tottal))
	return len(extname),out

parser = argparse.ArgumentParser()
parser.add_argument('file', action="store", help='File with list of plain files (~# find ./ -name "*")')
parser.add_argument('-o', dest="outfile", default="None", action="store", help='Output file. If none, copy to \"out-\"+file')
args = parser.parse_args()

if args.outfile=="None":
	args.outfile="out-"+args.file
file=open(args.file,'r')
files=file.read().split('\n')[0:-1]
file.close()
ext=['']
out=[]
outcount=[]
f_len=len(files)
for file in files:
	sys.stderr.write('\r%s/%s' % (files.index(file)+1,f_len))
	extencion=file.split('/')[-1].split('.')
	if len(extencion)>1:
		extencion=extencion[-1].lower()
		if ext.count(extencion)==0:
			ext.append(extencion)
			out.append([extencion,file])
			outcount.append(1)
		else:
			out[ext.index(extencion)-1].append(file)
			outcount[ext.index(extencion)-1]+=1
print ("\nCopy result to "+args.outfile+"...")
file=open(args.outfile,'w')

ecount,ewr=ext_pallet(ext[1:],outcount,f_len)
file.write("[FILE TYPE] [COUNT] [%]\n")
file.write(ewr)
num=len(out)+9+ecount
file.write("[STRING] [COUNT] [EXTENSION]\n")
for i in range(len(out)):
	out[i][1:]=list(set(out[i][1:]))
	if i!=0:
		num+=len(out[i-1])+3
	file.write ("["+str(num)+"] ["+str(len(out[i])-1)+"] "+out[i][0]+"\n")
file.write("\n\n\n")

for i in out:
	for ii in range(0,len(i)):
		if ii==0:
			file.write ("\n\n\n[EXT] "+i[ii]+"\n")
		else:
			file.write( i[ii]+"\n")
file.close()
