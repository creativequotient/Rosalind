#Read contents of rosalind_ba1c.txt for inputs
with open("rosalind_ba1c.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be converted

def ReverseComplement( sequence ):
    output = ""
    for i in sequence:
        if i == "A":
            output += "T"
        elif i == "T":
            output += "A"
        elif i == "G":
            output += "C"
        else:
            output += "G"
    return output[::-1] #Reverse output to obtain reverse complement to be from 5' -> 3'

print( ReverseComplement( input_sequence ) )
