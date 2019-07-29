def findMotif(sequence, motif):
    output = []
    for i in range(len(sequence) - len(motif)):
        if sequence[i:i + len(motif)] == motif:
            output.append(i + 1)

    return output

if __name__ == "__main__":

    # Read file to obtain inputs
    f = open("inputs/SUBS.in", "r")

    # Inputs
    sequence = f.readline().replace("\n","")
    motif = f.readline().replace("\n","")

    # Find location(s) of motif
    motifIndex = findMotif(sequence, motif)

    # Write to output
    output = open("outputs/SUBS.out", "w")

    motifIndex = map(str, motifIndex)
    output.write(" ".join(motifIndex))
