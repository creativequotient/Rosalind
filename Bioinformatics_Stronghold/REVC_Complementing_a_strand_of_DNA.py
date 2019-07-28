def findComplementary(DNA_sequence):

    # Define helper function to find complementary sequence
    def __complement(nucleotide):
        nucleotides = {
            "A":"T",
            "C":"G",
            "G":"C",
            "T":"A"
        }
        return nucleotides[nucleotide]

    # Find complementary sequence and then reverse sequence (to orientate sequence from 5' -> 3')
    return "".join(reversed(list(map(__complement, DNA_sequence))))

if __name__ == "__main__":
    DNA_sequence = input("Input DNA sequence: ")

    print(findComplementary(DNA_sequence))
