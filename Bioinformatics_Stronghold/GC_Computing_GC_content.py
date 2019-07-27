def computeGC(sequence):
    def _helper(base):
        if base == "G" or base == "C":
            return 1
        else:
            return 0
    GC_array = sum(map(_helper, sequence))
    return GC_array * 100.0 / len(sequence)

if __name__ == "__main__":
    DNA_sequence = "ATGCCATGATGAGGGG"

    print(computeGC(DNA_sequence))
