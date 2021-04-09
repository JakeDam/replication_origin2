# Determines the skew (difference between G and C) for each base position in a given genome
def skew(genome):
    skews = [0]
    skew = 0
    for base in genome:
        if base == 'G' or base == 'g':
            skew += 1
            skews.append(skew)
        elif base == 'C' or base == 'c':
            skew -= 1
            skews.append(skew)
        else:
            skews.append(skew)
    return skews

# Determines the locations of minimum skew values from a given genome
def minimum_skew(genome):
    skew_array = skew(genome)
    min_skew = 0
    min_skews = []
    for i in range(0, len(skew_array)) :
        if skew_array[i] < min_skew:
            min_skews = []
            min_skews.append(i)
            min_skew = skew_array[i]
        elif skew_array[i] == min_skew:
            min_skews.append(i)
    return min_skews
    
# Calculates hamming distance between two nucleotide sequences 
def hamming_dist(seqA, seqB):
    h_dist = 0 
    for i in range(0, len(seqA)):
        if seqA[i] != seqB[i]:
            h_dist += 1
    return h_dist

# Determines the location of approximate matches of a pattern to a given genome
def approximate_match(pattern, genome, d):
    positions = []
    for i in range(0, len(genome) - len(pattern) + 1):
        subset = genome[i:i + len(pattern)]
        mismatches = 0
        for j in range(0, len(subset)):
            if subset[j] != pattern[j]:
                mismatches += 1
        if mismatches <= d:
            positions.append(i)
    return positions

# Determines the number of matches or near matches of a pattern to a given genome
def approximate_pattern_count(pattern, genome, d):
    count = 0
    for i in range(0, len(genome) - len(pattern) + 1):
        subset = genome[i:i + len(pattern)]
        mismatches = 0
        for j in range(0, len(subset)):
            if subset[j] != pattern[j]:
                mismatches += 1
        if mismatches <= d:
            count += 1
    return count
