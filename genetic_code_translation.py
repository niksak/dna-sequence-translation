"""Created by:   Nikos Sakellariou
   Date      :   4.17.2015
   A script about translating genetic code sequences into proteins
   Input: The genetic code sequence in triplets
   Output: The proteins coding
   Sources: http://en.wikipedia.org/wiki/DNA_codon_table
"""
import re

genetic_code = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L',
'CTC':'L','CTA':'L','CTG':'L','ATT':'I',
'ATC':'I','ATA':'I','ATG':'M','GTT':'V',
'GTC':'V','GTA':'V','GTG':'V','TCT':'S',
'TCC':'S','TCA':'S','TCG':'S','CCT':'P',
'CCC':'P','CCA':'P','CCG':'P','ACT':'T',
'ACC':'T','ACA':'T','ACG':'T','GCT':'A',
'GCC':'A','GCA':'A','GCG':'A','TAT':'Y',
'TAC':'Y','TAA':'Ochre','TAG':'Amber',
'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
'TGT':'C','TGA':'Opal','TGG':'W','CGT':'R',
'CGC':'R','CGA':'R','CGG':'R','AGT':'S',
'AGC':'S','AGA':'R','AGG':'R','GGT':'G',
'GGC':'G','GGA':'G','GGG':'G'}


# splits the input string into triplets and translates them.
# it stores the results in a string
def genetic_code_translation(genetic_code,input_sequence):
	#elements = input_sequence.split(); #If input sequence is splited by space
	elements = re.findall('...',input_sequence)
	proteins_sequence = ''
	for element in elements:
		proteins_sequence = proteins_sequence + genetic_code[element]
	print elements	
	return proteins_sequence
	

elements = ''
dna_seq = ''
while(1):
	input_sequence = raw_input('Enter the DNA sequence. \n');
	input_sequence = input_sequence.upper()
	dna_seq = dna_seq + input_sequence
	elements = elements + genetic_code_translation(genetic_code,input_sequence)
	
	if elements[-1] == 'l' or elements[-1] == 'r' or elements[-1] == 'e':
		break
print "Your DNA sequence is: ",dna_seq
print "The final output is", elements
