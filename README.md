# SequenceMatcher
A simple Python app to detect which of the DNA sequences in a test file are pieces of a given reference sequence. Reverse-complemented test sequences will also be matched.

To use, you will need a version of Python 3 installed (which you can access at https://www.python.org/downloads/).

To run, run the following in your CLI:

python -c "import SequenceMatcher; SequenceMatcher.findMatches(\\"ref.fasta\\",\\"test.fasta\\")"

ref.fasta and test.fasta can be replaced with paths for any reference sequence and test file respectively, as required. Included in this repo are an example ref.fasta containing the HIV-1 reference genome and a test.fasta file containing HIV DNA corrupted with TB.

Output will be in the form of:
- A matches.fasta file containing all the pieces of sequence in test.fasta that were found in ref.fasta
- A mismatches.fasta file containing all the pieces of sequence in test.fasta that were not found in ref.fasta
- A summary of how many pieces of the sequence in matches.fasta and mismatches.fasta printed to the CLI

To run the tests, run

python SequenceMatcherTests.py