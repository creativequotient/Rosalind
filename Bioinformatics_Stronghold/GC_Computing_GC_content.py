# Compute GC content of a given DNA sequence
def computeGC(sequence):

    # Define helper function to count G and C
    def _helper(base):
        if base == "G" or base == "C":
            return 1
        else:
            return 0

    # Sum array to get number of G and C
    GC_array = sum(map(_helper, sequence))

    # Return GC content in percentage
    return GC_array * 100.0 / len(sequence)

# Convert list of IDs and DNA sequences to dictionary with {ID: sequence} key, value pairs
def fastaDict(fasta):

    # Define current sequence ID
    currentSeq = None

    # Output dictionary of {ID: sequence} pairs
    output = {}

    # Iterate over fasta and update output dictionary
    for line in fasta:
        if line.startswith(">"):
            currentSeq = line.replace(">","")
            output[currentSeq] = ""
        else:
            output[currentSeq] += line

    # Return fasta dictionary
    return output

if __name__ == "__main__":
    # Read fasta file
    fasta_input = open("inputs/GC.in","r").readlines()

    # Remove end of line ("\n")
    fasta_input = list(map(lambda x: x.replace("\n",""), fasta_input))

    # Convert to dictionary
    fasta_dict = fastaDict(fasta_input)

    # Determine GC content
    gc_content = list(map(lambda x: (x[0], computeGC(x[1])), fasta_dict.items()))

    # Sort by GC content
    gc_content = sorted(gc_content, key=lambda x: -x[1])

    print("{0}\n{1:6f}".format(gc_content[0][0], gc_content[0][1]))
