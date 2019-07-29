def enumKMers(sequence, length, kmers = []):
    # Return kmers is length is <= 0 so as not not wrongly extend the length of
    # kmers further
    if length <= 0:
        return kmers

    # Enables the function to be called without initial empty list of kmers
    if kmers == []:

        # Ensures sequence is sorted so that output is lexicographical
        sequence = sorted(sequence)

        # Set kmers == sequence and decrement length by 1
        return enumKMers(sequence, length - 1, sequence)

    # Takes care of base case where length == 1
    if length == 1:
        output = []
        for kmer in kmers:
            for seq in sequence:
                output.append(kmer + seq)
        return output

    # General case where length > 1
    else:
        output = []
        for kmer in kmers:
            for seq in sequence:
                output += enumKMers(sequence, length - 1, [kmer + seq])
        return output

if __name__ == "__main__":

    # Read input file
    f = open("inputs/LEXF.in", "r")

    # Read first line of input file, sequence
    sequence = f.readline().replace("\n","").split(" ")

    # Read second line of input file, length of kmer
    n = int(f.readline().replace("\n",""))

    # Generate lexicographically sorted kmers
    kmers = enumKMers(sequence, n)

    # Output to file
    output = open("outputs/LEXF.out", "w", newline="\n")
    for kmer in kmers:
        output.write("{}\n".format(kmer))
