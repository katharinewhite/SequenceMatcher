import unittest
import SequenceMatcher
import os

class SequenceMatcherTests(unittest.TestCase):

	def setUp(self):
		with open('test_ref.fasta', 'w') as ref, open('test_test.fasta', 'w') as test:
			ref.write(">ref\n")
			ref.write("TAGCATGTTGGCGCCAAAGC\n")
			test.write(">0\n")
			test.write("TAGCATGTTGGCGCCAAAGC\n")
			test.write(">1\n")
			test.write("GCTTTGGCGCCAACATGCTA\n")

	def tearDown(self):
		os.remove('test_ref.fasta')
		os.remove('test_test.fasta')		

	def test_reverse_complement(self):
		sequence = "TAGCATGTTGGCGCCAAAGC"
		self.assertEqual(SequenceMatcher.reverseComplement(sequence),"GCTTTGGCGCCAACATGCTA")

	def test_get_sequences_from_multiple_lines(self):
		lines = [">0\n","TAGCAT\n","CACCTT\n",">1\n","GATAGC\n","TCCGAG\n"]
		self.assertEqual(SequenceMatcher.getSequences(lines), ["TAGCATCACCTT", "GATAGCTCCGAG"])

	def test_match_sequence_and_reverse_complement_of_sequence(self):
		SequenceMatcher.findMatches('test_ref.fasta', 'test_test.fasta')
		with open('matches.fasta', 'r') as matchesFile, open('mismatches.fasta','r') as mismatches:
			matches = matchesFile.readlines();
			self.assertEqual(len(matches),4) #two headings and two sequences
			self.assertEqual(matches[1],"TAGCATGTTGGCGCCAAAGC\n") #first sequence
			self.assertEqual(matches[3],"GCTTTGGCGCCAACATGCTA\n") #second sequence (reverse complement)
			self.assertEqual(len(mismatches.readlines()),0) #no mismatches
		
if __name__ == '__main__':
	unittest.main()