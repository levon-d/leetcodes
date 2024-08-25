class Solution:

    def binarySearch(self, l, r, arr, target): 
        if l > r:
            return -1
        
        if arr[l] == target:
            return l 
        elif arr[r] == target:
            return r

        mid = (l+r)//2 

        if arr[mid] == target:
            return mid 
        elif target > arr[mid]:
            return self.binarySearch(mid+1, r, arr, target)
        else:
            return self.binarySearch(l, mid-1, arr, target)

    def binarySearchForRowFind(self, l, r, arr, target): 
        if l > r:
            return l 
        
        mid = (l+r) // 2 

        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            if mid == len(arr) - 1 or arr[mid+1] > target:
                return mid 
            return self.binarySearchForRowFind(mid+1, r, arr, target)
        else:
            return self.binarySearchForRowFind(l, mid-1, arr, target)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_starts = [row[0] for row in matrix]
        target_row_index = self.binarySearchForRowFind(0, len(row_starts)-1, row_starts, target)
        target_row = matrix[target_row_index]

        index = self.binarySearch(0, len(target_row)-1, target_row, target)

        return True if index != -1 else False 
