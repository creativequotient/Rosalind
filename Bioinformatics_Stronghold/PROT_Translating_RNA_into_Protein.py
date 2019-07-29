def translateRNA(RNA_sequence):

    # Translated protein sequence
    protein = ""

    # RNA to amino acid table
    translationTable = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    # Translation start site
    start = -1

    # Locate starting site
    for i in range(len(RNA_sequence)):
        if translationTable[RNA_sequence[i:i+3]] == "M":
            start = i
            break

    # Iterate over RNA_sequence and translate RNA to protein in codon triplets
    for i in range(start, len(RNA_sequence), 3):

        amino_acid = translationTable[RNA_sequence[i:i+3]]

        # Add amino_acid to protein if not a stop codon, else, break
        if amino_acid != "*":
            protein += amino_acid

        else:
            break

    return protein

if __name__ == "__main__":
    RNA_sequence = open("inputs/PROT.in", "r").readline().replace("\n","")
    protein_sequence = translateRNA(RNA_sequence)

    output_file = open("outputs/PROT.out", "w")
    output_file.write(protein_sequence)
