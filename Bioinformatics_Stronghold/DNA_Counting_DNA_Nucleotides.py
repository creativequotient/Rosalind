def countNuelcotides(sequence):

    # Initialize dictionary of nucleotide counts to 0
    nucleotides = {"A":0,
                   "C":0,
                   "G":0,
                   "T":0}

    # Iterate over sequence and update nucleotide counts
    for nucleotide in sequence:
        nucleotides[nucleotide] += 1

    # Return dictionary of nucleotide counts
    return nucleotides

if __name__ == "__main__":
    DNA_sequence = input("Input DNA sequence: ")

    nucleotideCounts = list(countNuelcotides(DNA_sequence).items())
    nucleotideCounts = sorted(nucleotideCounts, key = lambda x: x[0])
    nucleotideCounts = list(map(lambda x: x[1], nucleotideCounts))

    print("{0} {1} {2} {3}".format(nucleotideCounts[0],
                                   nucleotideCounts[1],
                                   nucleotideCounts[2],
                                   nucleotideCounts[3]))
