#! /usr/bin/env python
DNASeq = raw_input("Enter DNA Sequence :")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")
SeqLength = float(len(DNASeq))
print "Sequence Length: %d" % (SeqLength)
BaseList = list(set(DNASeq))
for Base in BaseList:
	Percent = 100 * DNASeq.count(Base) / SeqLength
	print "%s: %4.1f%%" % (Base,Percent)
	
for Test in range(65,73):
	for Num in range (1,13):
		print chr(Test) + str(Num),
	print