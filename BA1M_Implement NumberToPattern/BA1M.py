#Read contents of rosalind_ba1n.txt for inputs
with open("rosalind_ba1n.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = int( input[0] ) #Sequence to be converted
    input_k = int( input[1] ) #Length of sequence

#Converts number to pattern
def NumberToPattern( number, k ):
    NumToBase = { 0:"A", 1:"C", 2:"G", 3:"T" }
    pattern = ""
    for i in range(k):
        pattern = NumToBase[ number%4 ] + pattern
        number = number // 4
    return pattern

print( NumberToPattern(input_sequence, input_k) )
