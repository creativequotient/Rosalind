#Read contents of rosalind_ba1j.txt for inputs
with open("rosalind_ba1j.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be searched
    input_k = int( input[1].split(" ")[0] ) #k, denoting the length of k-mers
    input_d = int( input[1].split(" ")[1] ) #d, denoting the maximum allowed Hamming distance

def most_frequent_with_mismatch_and_complement( sequence, k, d ):

    #Generate all possible k-mers
    patterns = permute_dna("", k)

    #Keep track of patterns and their matches in sequence
    tracker = {} #Dictionary of ["pattern":matches] pairs

    for pattern in patterns:
        matches = FindApproximateMatches(sequence, pattern, d)
        if len(matches) != 0: #Filters out patterns that have 0 matches
            tracker[pattern] = len(matches)  #Adds [pattern, matches] to tracker

    #Process tracker to sum frequencies of both pattern and reverse complement of pattern
    sum_frequencies = {} #Dictionary of ["pattern": pattern matches + reverse complement matches]

    #Updates sum_frequencies with ["pattern": pattern matches + reverse complement matches] pairs
    for pattern in tracker.keys():
        reverse_comp = ReverseComplement( pattern )
        sum_frequencies[ pattern ] = tracker[ pattern ]
        if reverse_comp in tracker:
            sum_frequencies[ pattern ] += tracker[ reverse_comp ]

    #Obtain most frequently occuring pattern
    output = []
    sum_frequencies = list( sum_frequencies.items() ) #Converts dictionary to list of key,value pairs
    sum_frequencies.sort( key=lambda x: -x[1] ) #Sort key, value pairs in descending order of occurance
    max_freq = sum_frequencies[0][1] #Highest frequency of occurance

    #Adds patterns with the max_freq to output
    for pattern, freq in sum_frequencies:
        if freq == max_freq:
            output.append( pattern )
        else:
            break

    return output

#Obtain most frequently matched matterns within sequence with hamming distance <= d
patterns = most_frequent_with_mismatch_and_complement(input_sequence, input_k, input_d)

#Format output to console
print( (" ").join(patterns) )

'''
Helper Functions/Functions from other exercises
'''

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

#Function from BA1H, used to compute locations within sequence where HDistance(pattern, substring) <= d
def FindApproximateMatches( sequence, pattern, d ):
    locations = [] #Locations where pattern matches k-mer with Hamming distance <= 3

    for i in range(len(sequence) - len(pattern)):
        subsequence = sequence[i:i + len(pattern)] #Subsequence to be compared to pattern
        if HammingDistance( pattern, subsequence ) <= d: #Checks if Hamming distance <= d
            locations.append( i ) #Update locations with i

    return locations

#Function from BA1C, used to compute reverse complement
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