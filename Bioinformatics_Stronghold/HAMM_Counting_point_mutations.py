def calculateHammingDistance(sequence_1, sequence_2):
    # Seqences are assumed to be of the same length
    hammingDistance = 0

    # Iterate over nucleotides from both sequences and compare
    for nucleotide_1, nucleotide_2 in zip(sequence_1, sequence_2):

        # If nucleotides are not the same, increase hamming distance by 1
        if nucleotide_1 != nucleotide_2:
            hammingDistance += 1

    return hammingDistance

if __name__ == "__main__":

    input_sequences = open("inputs/HAMM.in", "r").readlines()
    input_sequences = list(map(lambda x: x.replace("\n", ""), input_sequences))

    print(calculateHammingDistance(input_sequences[0], input_sequences[1]))
