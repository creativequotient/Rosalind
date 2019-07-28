def permute(sequence):

    # If sequence has a length of 1, return it
    if len(sequence) == 1:
        return sequence

    # Output list
    output = []

    # Create all possible permutations
    for i in range(len(sequence)):
        curr = sequence[i]
        seq = sequence[:i] + sequence[i+1:]
        permutations = permute(seq)
        permutations = list(map(lambda x: curr + x, permutations))
        output += permutations

    # Return list of permuations
    return output

if __name__ == "__main__":
    # Get value of n (n <= 7)
    input_n = int(input("Input value of n: "))

    # Generate initial sequence
    input_sequence = "".join([str(i) for i in range(1,input_n+1)])

    # Permute sequence
    permutations = permute(input_sequence)

    # Print number of permutations
    print(len(permutations))

    # Print formated permutations
    for permutation in permutations:
        permutation = list(permutation)
        permutation = " ".join(permutation)
        print(permutation)
