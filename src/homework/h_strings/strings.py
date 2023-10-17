#
def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Input strings should be same length")
    
    hamming_distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1

    return hamming_distance

def get_dna_complement(dna):
    complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement_dna = ''.join(complement_dict[base] for base in reversed(dna))
    return complement_dna

    