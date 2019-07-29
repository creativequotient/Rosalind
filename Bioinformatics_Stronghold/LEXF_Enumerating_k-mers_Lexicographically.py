def enumKMers(sequence, length, kmers = []):
    if kmers == []:
        return enumKMers(sequence, length - 1, sequence)

    if length == 1:
        output = []
        for kmer in kmers:
            for seq in sequence:
                output.append(kmer + seq)
        return output

    else:
        output = []
        for kmer in kmers:
            for seq in sequence:
                output += enumKMers(sequence, length - 1, [kmer + seq])
        return output

if __name__ == "__main__":
    f = open("inputs/LEXF.in", "r")
    sequence = f.readline().replace("\n","").split(" ")
    n = int(f.readline().replace("\n",""))
    kmers = enumKMers(sequence, n)
    output = open("outputs/LEXF.out", "w", newline="\n")
    for kmer in kmers:
        output.write("{}\n".format(kmer))
