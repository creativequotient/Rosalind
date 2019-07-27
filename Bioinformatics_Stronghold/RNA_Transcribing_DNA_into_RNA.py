def transcribeDNAtoRNA(DNA_sequence):
    def __transcribe(nucleotide):
        DNAtoRNA = {
            "A":"A",
            "T":"U",
            "G":"G",
            "C":"C"
        }
        return DNAtoRNA[nucleotide]
    return "".join(map(__transcribe, DNA_sequence))

if __name__ == "__main__":
    DNA_sequence = input("Input DNA sequence: ")

    print(transcribeDNAtoRNA(DNA_sequence))
