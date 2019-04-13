#Read contents of rosalind_ba1k.txt for inputs
with open("rosalind_ba1k.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be searched
    input_k = int( input[1] ) #k-mer to generate frequency array

#Generates all possible permuations of DNA that can be formed of len == length
def permute_dna( perm, length ):
    if len( perm ) == length:
        return [perm]

    bases = ("A", "T", "G", "C") #Possible bases that can be added

    permutations = [] #All permutations of DNA

    for base in bases:
        permutations += permute_dna( perm + base, length )

    return permutations

#Generates frequency array
def FrequencyArray( sequence, k ):
    #Generate all possible k-mers
    patterns = permute_dna("", k)

    #Initialize dictionary, creating key, value pairs of ["pattern", count]
    frequency_dict = {}
    for pattern in patterns:
        frequency_dict[ pattern ] = 0

    #Iterate over sequence and update frequency_dict
    curr_subsequence = ""
    for i in range( len(sequence) - k + 1 ):
        #Updates curr_subsequence using a sliding window
        if i == 0: #Special case of i == 0
            curr_subsequence = sequence[0:k]
        else:
            curr_subsequence = curr_subsequence[1:] + sequence[i + k - 1]
        #Updates frequency_dict
        frequency_dict[ curr_subsequence ] += 1

    #Obtain frequency_list and sort by lexicographical order
    frequency_list = list( frequency_dict.items() )
    frequency_list.sort( key=lambda x: x[0] )

    #Generate frequency_array of only frequencies
    frequency_array = []
    for _, frequency in frequency_list:
        frequency_array.append( frequency )

    return frequency_array

frequency_array = FrequencyArray( input_sequence, input_k )

print( (" ").join( map(str,(frequency_array)) ) )
