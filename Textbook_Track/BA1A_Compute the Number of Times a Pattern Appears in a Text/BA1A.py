#Read contents of rosalind_ba1a.txt for inputs
with open("rosalind_ba1a.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be searched
    input_pattern = input[1] #Pattern to be located

def PatternCount( text, pattern ):
    counter = 0
    #Iterate through entire string, checking if each substring == pattern
    for i in range(len(text) - len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            counter += 1 #Update counter by 1
    return counter

print( PatternCount( input_sequence, input_pattern ) ) #Prints the number of times the pattern appears in the sequence