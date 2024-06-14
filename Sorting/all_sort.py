class CustomSort:
    
    def bubble_sort(self,list_a):
        indexing_length = len(list_a) - 1
        sorted = False
        
        while not sorted:
            sorted = True
            for i in range(indexing_length):
                if list_a[i] > list_a[i + 1]:  
                    sorted = False
                    list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                    
        return list_a
        
    
    def bubble_asc(self, arr):
        """ACCENDING ORDER BUBBLE SORT"""
        num = len(arr)
        
        for each1 in range(num - 1):
            swapped = False
            
            for each2 in range(num - each1 - 1):
                if arr[each2] > arr[each2 + 1]:
                    arr[each2], arr[each2 + 1] = arr[each2 + 1], arr[each2]
                    swapped = True
                    
            if not swapped:
                break
        return arr
    
    def bubble_desc(self, lst):
        """DECENDING ORDER BUBBLE SORT"""
        num = len(lst)
        
        for each in range(num - 1, 0, -1):
            swapped = False
            
            for ele in range(each):
                if lst[ele] < lst[ele + 1]:
                    swapped = True
                    lst[ele], lst[ele + 1] = lst[ele + 1], lst[ele]

            if not swapped:
                break
        return lst
    
    def selection_sort(self,list_a):
        indexing_length = range(len(list_a) - 1)
        
        for each in indexing_length:
            min_value = each
            
            for valu in range(i + 1, len(list_a)):
                if list_a[j] < list_a[min_value]: 
                    min_value = j
                    
            if min_value != each:
                list_a[min_value], list_a[each] = list_a[each], list_a[min_value]
            
            return list_a
                       
        
    def selection_asc(self, arr):
        """ACCENDING ORDER SELECTION SORT"""
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
        
    def selection_desc(self, arr):
        """DECENDING ORDER SELECTION SORT"""
        num = len(arr)
        for i in range(num - 1, 0, -1):
            max_idx = 0
            for j in range(1, i + 1):
                if arr[j] < arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        return arr


import random
lst = [random.randint(10, 99) for _ in range(10)]
print("Before Soring: ", lst)

obj = CustomSort()
print(f"\n\nBubble Sort: {obj.bubble_sort(lst.copy())}")
print(f"Accending Order(Bubble): {obj.bubble_asc(lst.copy())}")
print(f"Decending Order(Bubble): {obj.bubble_desc(lst.copy())}")

print(f"\n\nAccending Order(Selection): {obj.selection_asc(lst.copy())}")
print(f"Decending Order(Selection): {obj.selection_desc(lst.copy())}")
print(f"Decending Order(Selection): {obj.bubble_desc(lst.copy())}")

