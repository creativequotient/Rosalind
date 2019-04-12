#Compute locations in which k-mers are approximately homologous with input_pattern ( Hamming Distance <= 3 )

#Read contents of rosalind_ba1h.txt for inputs
with open("rosalind_ba1h.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_pattern = input[0] #Pattern to be approximated to
    input_sequence = input[1] #Sequence to be searched
    input_d = int( input[2] ) #d, the max allowable Hamming distance

#Function from BA1G, used to compute Hamming distance between pattern and k-mer
def HammingDistance( sequence_1, sequence_2 ):
    distance = 0
    for base_1, base_2 in zip( sequence_1, sequence_2 ): #base_1 and base_2 -> base at index i of sequences 1 and 2 respectively
        if base_1 != base_2: #Compare both bases
            distance += 1 #Increase distance by 1 if bases are not the same
    return distance

def FindApproximateMatches( sequence, pattern, d ):
    locations = [] #Locations where pattern matches k-mer with Hamming distance <= 3

    for i in range(len(sequence) - len(pattern)):
        subsequence = sequence[i:i + len(pattern)] #Subsequence to be compared to pattern
        if HammingDistance( pattern, subsequence ) <= d: #Checks if Hamming distance <= d
            locations.append( i ) #Update locations with i

    return locations

#Obtain candidate locations meeting requirements
locations = FindApproximateMatches( input_sequence, input_pattern, input_d )

#Format output to console
for i, loc in enumerate(locations):
    if i == 0:
        print( str(loc), end="" )
    else:
        print( " " + str(loc), end="" )

