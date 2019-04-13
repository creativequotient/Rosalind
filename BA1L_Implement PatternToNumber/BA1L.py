#Read contents of rosalind_ba1l.txt for inputs
with open("rosalind_ba1l.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be converted

#Converts pattern to number
def PatterToNumber( sequence ):
    BaseToNumber = { "A":0, "C":1, "G":2, "T":3}
    counter = 0
    for i in range(len(sequence)):
        counter *= 4
        counter += BaseToNumber[ sequence[i] ]
    return counter

print( PatterToNumber(input_sequence) )