#Read contents of rosalind_ba1b.txt for inputs
with open("rosalind_ba1b.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be searched
    input_k = int( input[1] ) #k-mer to be returned

def FrequentWords( sequence, k ):
    tracker = {} #Dictionary to keep track of substring and frequency ["substring": frequency]
    for i in range( len(sequence) - k ):
        substring = sequence[i:i+k] #Obtains substring from i:i+k

        #Update substring frequency in tracker
        if substring in tracker:
            tracker[substring] = tracker[substring] + 1
        else:
            tracker[substring] = 1

    #Obtain key value pairs and sort by descending order of frequency
    tracker = list( tracker.items() )
    tracker.sort( key= lambda x: -x[1] )

    #Obtain most frequent k-mer(s)
    max_freq = tracker[0][1]
    output = []
    for substring, freq in tracker:
        if freq == max_freq:
            output.append(substring)
        else:
            break

    #Return output of most frequent k-mers
    return output

#Most frequently occuring k-mer(s)
most_frequent_k_mers = FrequentWords( input_sequence, input_k )

#Format output to console
for i, substring in enumerate(most_frequent_k_mers):
    if i == 0:
        print( substring, end="" )
    else:
        print( " " + substring, end="" )
