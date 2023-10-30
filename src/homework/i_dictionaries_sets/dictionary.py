
#def get_p_distance(list1, list2):
    #return sum(c1 != c2 for c1, c2 in zip(list1, list2)) / len(list1) 
#def get_p_distance_matrix(strings):
    #n = len(strings) 
    #matrix = [[0.0 for _ in range(n)] for _ in range(n)
    #for i in range(n):
      #  for j in range(n):
       #    if i != j:
        #       matrix[i][j] = get_p_distance(strings[i], strings[j])          
    #return matrix 
#list1 = ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
#list2 = ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
#distance_matrix = get_p_distance(list1, list2) 
#print(f"p-distance between list 1 and list 2 is: {distance_matrix:.5f}")
#strings = [list1] 
#distance_matrix = get_p_distance_matrix(strings) 
#for row in distance_matrix:
  # print(" ".join(f"{val:.5f}" for val in row))


def add_inventory(widgets, widget_name, quantity):
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity 

def remove_inventory_widget(widgets, widget_name):
    if widget_name in widgets:
        del widgets[widget_name]
        return 'record deleted' 
    else:
        return 'Item not found.'
    

    