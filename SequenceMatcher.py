def findMatches(referenceFile, dataFile):
	with open(referenceFile, 'r') as refFile, open(dataFile, 'r') as data, open('matches.fasta', 'w') as matches, open('mismatches.fasta', 'w') as mismatches:
		ref = refFile.readlines()[1] #first line is header
		sequences = getSequences(data.readlines()) 
		numberMatched = 0
		numberMismatched = 0
		for sequence in sequences:
			if sequence in ref or reverseComplement(sequence) in ref:
				matches.write(">" + str(numberMatched) + "\n")
				matches.write(sequence + "\n")
				numberMatched += 1
			else:
				mismatches.write(">" + str(numberMismatched) + "\n")
				mismatches.write(sequence + "\n")
				numberMismatched += 1
		print("Number of matches: " + str(numberMatched) + "\n")
		print("Number of mismatches: " + str(numberMismatched))


def reverseComplement(sequence):
	complement = {'A': 'T', 'C': 'G', 'G' : 'C', 'T': 'A'}
	reverseComplement = ""
	for base in reversed(sequence):
		reverseComplement += complement.get(base, base) #first parameter of get is key; second is default return value if not found
	return reverseComplement

def getSequences(lines):
	lines.pop(0) #ignoring first header
	lines.append("> end")  #marking end of last sequence
	sequences = []
	sequence = ""
	for line in lines:
		if line.startswith('>'): #we have reached the end of a sequence
			sequences.append(sequence)
			sequence = ""
		else: #this line is part of a sequence
			sequence += line.rstrip()
	return sequences