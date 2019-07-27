#Read contents of rosalind_ba1d.txt for inputs
with open("rosalind_ba1e.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be searched
    _input = input[1].split(" ") #Split input[1] to give a list containing k, L and t
    input_k = int( _input[0] ) #k
    input_L = int( _input[1] ) #L
    input_t = int( _input[2] ) #t

def LocateClumps( sequence, k, L, t ):
    patterns = [] #Candidates that occur at least t times in each clump of length, L
    for i in range(len(sequence) -  L):
        subsequence = sequence[i:i + L] #Subsequence of length L within which to locate clumps
        tracker = {} #Tracker to keep track of subsequences occuring
        for j in range(len(sequence) - k):
            pattern = subsequence[j: j + k] #pattern of k length within one clump

            #Update tracker
            if pattern in tracker:
                tracker[pattern] += 1
            else:
                tracker[pattern] = 1

        #Convert dictionary to sorted list (in descending order of occurance)
        tracker = list( tracker.items() )
        tracker.sort( key=lambda x: -x[1] )

        #Adds patterns that occur >= t times in clump to patterns
        for pattern, freq in tracker:
            if freq >= t and pattern not in patterns:
                patterns.append( pattern )

    return patterns

#Obtain candidate patterns meeting requirements
patterns = LocateClumps( input_sequence, input_k, input_L, input_t )

#Format output to console
for i, pattern in enumerate(patterns):
    if i == 0:
        print( str(pattern), end="" )
    else:
        print( " " + str(pattern), end="" )
