'''
This solution is a greedy solution to the problem by generating all possible permutations of k-mers and then calculating the Hamming Distance
A more optimal solution can be achieved by obtaining nCr (where n is the length of the sequence and r is the max Hamming distance) indices
and then permutating the k-mers at those indices instead such that all permutations produced are of only Hamming distance <= D
'''

#Read contents of rosalind_ba1n.txt for inputs
with open("rosalind_ba1n.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be converted
    input_d = int( input[1] ) #Max Hamming Distance

#Generates all possible permuations of DNA that can be formed of len == length
def permute_dna( perm, length ):
    if len( perm ) == length:
        return [perm]

    bases = ("A", "T", "G", "C") #Possible bases that can be added

    permutations = [] #All permutations of DNA

    for base in bases:
        permutations += permute_dna( perm + base, length )

    return permutations

#Function from BA1G, used to compute Hamming distance between pattern and k-mer
def HammingDistance( sequence_1, sequence_2 ):
    distance = 0
    for base_1, base_2 in zip( sequence_1, sequence_2 ): #base_1 and base_2 -> base at index i of sequences 1 and 2 respectively
        if base_1 != base_2: #Compare both bases
            distance += 1 #Increase distance by 1 if bases are not the same
    return distance

#Generate d-Neighborhood of a sequence
def dNeighborhood( sequence, d ):
    patterns = permute_dna( "", len(sequence) ) #Generates all possible k-mers of len(sequence)
    output = []
    for pattern in patterns:
        if HammingDistance(pattern, sequence) <= d: #Checks if Hamming distance between pattern and sequence <= d
            output.append( pattern )
    return output

#Generate neighbors of input_sequence of Hamming distance <= input_d
neighbors = dNeighborhood( input_sequence, input_d )

#Outputs neighbors
for pattern in neighbors:
    print(pattern)