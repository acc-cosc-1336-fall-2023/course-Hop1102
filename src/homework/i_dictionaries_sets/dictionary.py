#
def get_p_distance(list1, list2):
    assert len(list1) == len(list2)
    diff_count = sum(c1 != c2 for c1, c2 in zip(list1, list2))
    return diff_count / len(list1)

def get_p_distance_matrix(list1):
    n = len(list1) 
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = get_p_distance(list1[i], list1[j])
             
    return matrix 
#sample
list1 = [
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
    ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T']
    ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
    
]

distance_matrix = get_p_distance_matrix(list1) 

for row in distance_matrix:
    print(" ".joint(f"{val:.5f}" for val in row))