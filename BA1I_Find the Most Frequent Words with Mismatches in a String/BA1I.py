#Read contents of rosalind_ba1i.txt for inputs
with open("rosalind_ba1i.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be searched
    input_k = int( input[1].split(" ")[0] ) #k, denoting the length of k-mers
    input_d = int( input[1].split(" ")[1] ) #d, denoting the maximum allowed Hamming distance

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

def most_frequent_with_mismatch( sequence, k, d ):

    #Generate all possible k-mers
    patterns = permute_dna("", k)

    #Keep track of patterns and their matches in sequence
    tracker = []

    for pattern in patterns:
        matches = FindApproximateMatches(sequence, pattern, d)
        if len(matches) != 0: #Checks that there are matches with pattern
            tracker += [ (pattern, len(matches) ) ] #Appends [pattern, matches] to tracker

    tracker.sort( key=lambda x: -x[1] ) #Sort tracker in descending order by frequency of matches

    max_freq = tracker[0][1] #Obtain max frequency of matches

    output = []

    #Appends patterns with freq == max_freq to output
    for pattern, freq in tracker:
        if freq == max_freq:
            output.append( pattern )
        else:
            break

    return output

#Obtain most frequently matched matterns within sequence with hamming distance <= d
patterns = most_frequent_with_mismatch(input_sequence, input_k, input_d)

#Format output to console
for i, pattern in enumerate(patterns):
    if i == 0:
        print( str(pattern), end="" )
    else:
        print( " " + str(pattern), end="" )
