#! /usr/bin/env python

DNASeq = 'ATGAAC'
DNASeq = raw_input("Enter a DNA Sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")

print 'Sequence:', DNASeq

#Calculate the sequence length and its relative base composition
SeqLength = float(len(DNASeq))
print 'Sequence Length:', SeqLength
NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')
pctA = "A: %.1f%%" % (100*NumberA/SeqLength)
print pctA
print "C: %.1f%%" % (100*NumberC/SeqLength)
print "G: %.1f%%" % (100*NumberG/SeqLength)
print "T: %.1f%%" % (100*NumberT/SeqLength)
print "There are %d A bases." % (NumberA)
print "A occurs in %d bases out of %d total; this is %.2f%%." % (NumberA, SeqLength, NumberA/SeqLength)

#See if all bases are A,C,G,T
BaseList = "ACGT"
BaseSeq = list(set(DNASeq))
print BaseSeq
for Base in BaseSeq:
	if Base == ('A' and 'C' and 'T' and 'G'):
		print "All good"
	else:
		print "Bad!"

#Calculate the melting temperature of the sequence.
TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT
if SeqLength > 14:
	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print "Tm Long (>14): %.1f C" % (MeltTempLong)
else:
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	print "Tm Short (<14): %.1f C" % (MeltTemp)