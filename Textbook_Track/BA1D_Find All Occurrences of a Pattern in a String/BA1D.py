#Read contents of rosalind_ba1d.txt for inputs
with open("rosalind_ba1d.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_pattern = input[0] #Pattern to be located
    input_sequence = input[1] #Sequenced to be searched

def LocatePattern( sequence, pattern ):
    locations = [] #Stores 0-based indices where pattern occurs in the sequence

    for i in range(len(sequence) - len(pattern)):
        subsequence = sequence[i:i+len(pattern)] #Obtains subsequence
        if subsequence == pattern: #Checks if subsequence == pattern
            locations.append(i) #Update locations

    return locations

#Obtain locations of pattern occurences
locations = LocatePattern( input_sequence, input_pattern )

#Format output to console
for i, loc in enumerate(locations):
    if i == 0:
        print( str(loc), end="" )
    else:
        print( " " + str(loc), end="" )