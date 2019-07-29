from Utilities import findComplementary as complementary

# Locate restriction sites and their respective lengths between min and max
def locateRestrictionSites(sequence, min, max):

    # Locate restriction sites of length n
    def __findRE(sequence, n):

        output = []

        # Iterate over sequence and check for restriction site
        for i in range(len(sequence) - n + 1):

            # Putative RE site
            putativeSeq = sequence[i:i+n]
            
            # Check putative sequence == its complemenary sequence, if true:
            # site is palindromic and hence, an RE site
            if putativeSeq == complementary(putativeSeq):
                output.append((i+1, n))

        return output

    output = []

    # Locate restriction sites of lengths [min, max]
    for n in range(min, max + 1):
        output += __findRE(sequence, n)

    # Sort by index
    output = sorted(output, key=lambda x: x[0])

    return output

if __name__ == "__main__":

    # Read input file
    f = open("inputs/REVP.in", "r")

    # Read fastaID and sequence
    _ = f.readline()
    sequence = f.readlines()
    sequence = list(map(lambda x: x.replace("\n",""), sequence))
    sequence = "".join(sequence)

    # Get restriction sites
    sites = locateRestrictionSites(sequence, 4, 12)

    # Write results to output file
    output_file = open("outputs/REVP.out", "w")

    for index, length in sites:
        output_file.write("{0} {1}\n".format(index, length))
