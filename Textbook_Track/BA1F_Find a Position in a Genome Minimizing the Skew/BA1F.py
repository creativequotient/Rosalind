#Locte positions in the sequence such that subsequence [0:i] has a GC-skew of 0

#Read contents of rosalind_ba1d.txt for inputs
with open("rosalind_ba1f.txt", "r") as file:
    input = file.read().split("\n") #Spit input at "\n" into a list with two valuess [ sequence, pattern ]
    input_sequence = input[0] #Sequence to be searched

def min_GC_Skew( sequence ):
    skews = [0] #Keeps track of skews from [:i], insert 0 at index 0 as a dummy
    skew = 0 #Keeps track of skew as i in [:i] increases towards |sequnec|

    for i in range(1, len(sequence) + 1 ):
        base = sequence[:i][-1] #Nucleotide at position i
        if base == "C": #If base == "C", decrement skew by 1
            skew -= 1
        elif base == "G": #If base == "G", increment skew by 1
            skew += 1
        skews.append( skew ) #Update skews

    min_skew = min( skews ) #Minimum skew, min( G - C )

    min_locations = [] #Locations which minimum skew occurs

    for i, skew in enumerate(skews): #Appends locations to min_locations if skew at sequence[:i] == min_skew
        if skew == min_skew:
            min_locations.append( i )

    return min_locations




#Obtain candidate patterns meeting requirements
locations = min_GC_Skew( input_sequence )

#Format output to console
for i, loc in enumerate(locations):
    if i == 0:
        print( str(loc), end="" )
    else:
        print( " " + str(loc), end="" )

