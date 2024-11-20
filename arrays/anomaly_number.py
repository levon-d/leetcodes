from collections import Counter
def find_largest_anomaly(arr):

    element_counts = Counter(arr)
    largest = -1 
    arr_sum = sum(arr)

    for num in arr: 
        
        target = (arr_sum - num) / 2 

        if (target % 1) != 0:
            continue 
        
        target = int(target)

        if target in element_counts and (target != num or element_counts[target] > 1): 
            largest = max(largest, num)

    return largest

print(find_largest_anomaly([1, 2, 3, 4, 6])) 

    

    
