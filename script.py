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

# Generates the d-neighborhood (set of all k-mers whose hamming distance from the pattern does not exceed d)
def neighbors(pattern, d):
    if d == 0:
        return set([pattern])
    if len(pattern) == 1:
        return set(('A', 'T', 'C', 'G'))
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_dist(pattern[1:], text) < d:
            for base in ['A', 'T', 'C', 'G']:
                neighborhood.add(base + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

# Generates the d=1 neighborhood for a given sequence
def immediate_neighbors(pattern):
    neighborhood = set()
    for i in range(len(pattern)):
        symbol = pattern[i]
        for x in "ACTG":
            if x != symbol:
                neighbor = pattern[:i] + x + pattern[i+1:]
                neighborhood.add(neighbor)
    return neighborhood

# Returns the largest value from a dictionary 
def max_map(dict):
    return max(dict.values())

# Returns the most frequent k-mer approximate matches of a pattern to a given genome
def freq_words_with_mismatches(genome, k, d):
    patterns = []
    freq_dict = {}
    length = len(genome)
    for i in range(length - k + 1):
        pattern = genome[i:i + k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            if neighbor not in freq_dict:
                freq_dict[neighbor] = 1
            else:
                freq_dict[neighbor] += 1
    m = max_map(freq_dict)
    for pattern in freq_dict:
        if freq_dict[pattern] == m:
            patterns.append(pattern)
    return patterns

# Takes in a DNA sequence and returns its reverse complement 
def reverse_complement(dna):
    complement = ''
    for base in dna:
        if (base == 'A' or base == 'a'):
            complement += 'T'
        elif (base == 'T' or base == 't'):
            complement += 'A'
        elif (base == 'C' or base == 'c'):
            complement += 'G'
        else:
            complement += 'C'
    rev_comp = complement[::-1]
    return rev_comp

# Returns the most frequent k-mer approximate matches and reverse complements of a pattern to a given genome
def freq_mismatch_rev_comp(genome, k, d):
    patterns = []
    freq_dict = {}
    length = len(genome)
    for i in range(length - k + 1):
        pattern = genome[i:i + k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            if neighbor not in freq_dict:
                freq_dict[neighbor] = 1
            else:
                freq_dict[neighbor] += 1
            rev_comp = reverse_complement(neighbor)
            if rev_comp not in freq_dict:
                freq_dict[rev_comp] = 1
            else:
                freq_dict[rev_comp] += 1
    m = max_map(freq_dict)
    for pattern in freq_dict:
        if freq_dict[pattern] == m:
            patterns.append(pattern)
    return patterns

print(len(freq_words_with_mismatches('TGCAT', 5, 2)))