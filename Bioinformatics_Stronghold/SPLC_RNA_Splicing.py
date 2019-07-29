from Utilities import fastaDict
from Utilities import translateRNA
from Utilities import transcribeDNAtoRNA
from Utilities import findComplementary

def removeIntrons(genomic_sequence, intron_sequences):

    for intron in intron_sequences:
        genomic_sequence = genomic_sequence.replace(intron, "")

    return genomic_sequence


if __name__ == "__main__":
    # Read fasta file
    fasta_input = open("inputs/SPLC.in","r").readlines()

    # Remove end of line ("\n")
    fasta_input = list(map(lambda x: x.replace("\n",""), fasta_input))

    # Convert to dictionary
    fasta_dict = fastaDict(fasta_input)

    # Get genomic DNA sequence
    genomic_id = fasta_input[0].replace(">","")
    genomic_sequence = fasta_dict[genomic_id]

    # Get intronic regions
    introns = []
    for id, sequence in fasta_dict.items():
        if id == genomic_id:
            continue

        else:
            introns.append(sequence)

    # Get exonic DNA regions
    exon_sequence = removeIntrons(genomic_sequence, introns)

    # Transcribe to RNA
    RNA_sequence = transcribeDNAtoRNA(exon_sequence)

    # Translate to protein
    protein_sequence = translateRNA(RNA_sequence)

    output_file = open("outputs/SPLC.out", "w")
    output_file.write(protein_sequence)
