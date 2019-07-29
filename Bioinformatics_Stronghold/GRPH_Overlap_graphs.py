from Utilities import fastaDict

# Create dictionary of {suffix, [id,..]} pairs
def createSuffixMap(fasta, k):
    map = {}
    for id, sequence in fasta.items():
        suffix = sequence[-k:]
        if suffix in map:
            map[suffix].append(id)
        else:
            map[suffix] = [id]
    return map

# Create dictionary of {prefix, [id,..]} pairs
def createPrefixMap(fasta, k):
    map = {}
    for id, sequence in fasta.items():
        prefix = sequence[:k]
        if prefix in map:
            map[prefix].append(id)
        else:
            map[prefix] = [id]
    return map

# Create prefix and suffix maps
def createMaps(fasta, k):
    return (createPrefixMap(fasta,k), createSuffixMap(fasta,k))

# Create adjacency list of overlapping FASTA entries
def adjacencyList(fasta, k):
    prefixMap, suffixMap = createMaps(fasta, k)
    output = []

    # Iterate over suffixMap and append ids that have the same prefix in prefixMap
    for suffix, suffix_ids in suffixMap.items():
        if suffix in prefixMap:
            prefix_ids = prefixMap[suffix]
            for suffix_id in suffix_ids:
                for prefix_id in prefix_ids:
                    if prefix_id == suffix_id:
                        continue
                    output.append((suffix_id, prefix_id))

    return output

if __name__ == "__main__":

    # Read input file
    fasta_file = open("inputs/GRPH.in", "r").readlines()
    fasta_file = list(map(lambda x: x.replace("\n",""), fasta_file))

    # Assemble input file into dictionary of {fasta_id, sequence} pairs
    fasta = fastaDict(fasta_file)

    # Generate adjacency list of k = 3
    adjList = adjacencyList(fasta, 3)

    # Write output
    output_file = open("outputs/GRPH.out", "w")
    for id1, id2 in adjList:
        output_file.write("{0} {1}\n".format(id1, id2))
