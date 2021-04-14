# Replication Origin 2
## Coding Challenges from UCSD's Bioinformatics I Week 2

Python script that contains tools for analyzing the repilication origin of genomes:
- skew: Determines the skew (difference between C and G) at all points of a genome
- minimum_skew: Determines the points in the genome with the lowest skew value
- hamming_dist: Calculates the Hamming Distance between two nucleotide sequences
- approximate_match: Determines the location of approximate (within a certian number of bases) matches of a pattern to a genome
- approximate_pattern_count: Counts the number of approximate matches of a pattern to a genome
-neighbors: Generates the d-neighborhood (set of all k-mers whose hamming distance from the pattern does not exceed d)
 for a given DNA sequence
 -immidiate_neighbors: Generates the d=1 neighborhood for a given DNA sequence
 -max_map: Returns the maximum value from a dictionary 
 -freq_words_with_mismatches: Returns the most frequent k-mer mismaches to a pattern with mismatches less than or equal to a given value, d
 -reverse_complement: Takes in a DNA sequence and returns its reverse complement
 -freq_mismatch_rev_comp: Returns the most frequent k-mer mismatches including reverse complements to a pattern with mismatches less than or equal to a given value, d