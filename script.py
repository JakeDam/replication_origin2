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

# Determines the minimum skew values from a given genome
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

genome = open('/home/jakedam/ucsd-bioinformatics/bioinformatics-I/week2/replication_origin2/datasets/dataset_7_10.txt').read()

print(minimum_skew(genome))