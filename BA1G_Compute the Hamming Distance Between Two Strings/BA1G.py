#Compute the Hamming distance between two strings

#Read contents of rosalind_ba1g.txt for inputs
with open("rosalind_ba1g.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence_1 = input[0] #Sequence 1 to be compared with sequence 2
    input_sequence_2 = input[1] #Sequence 2 to be compared with sequence 1

def HammingDistance( sequence_1, sequence_2 ):
    distance = 0
    for base_1, base_2 in zip( sequence_1, sequence_2 ): #base_1 and base_2 -> base at index i of sequences 1 and 2 respectively
        if base_1 != base_2: #Compare both bases
            distance += 1 #Increase distance by 1 if bases are not the same
    return distance

print( HammingDistance(input_sequence_1, input_sequence_2) )
