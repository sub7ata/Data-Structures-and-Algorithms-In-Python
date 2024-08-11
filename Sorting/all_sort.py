import random


class CustomSort:

    def bubble_sort(self, arr):
        """BUBBLE SORT"""
        indexing_length = len(arr) - 1
        is_sorted = False

        while not is_sorted:
            is_sorted = True

            for i in range(indexing_length):
                if arr[i] > arr[i + 1]:
                    is_sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr

    def bubble_asc(self, arr):
        """BUBBLE SORT (ACCENDING ORDER)"""
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

    def bubble_desc(self, arr):
        """BUBBLE SORT (DECENDING ORDER)"""
        num = len(arr)

        for each in range(num - 1, 0, -1):
            swapped = False

            for ele in range(each):
                if arr[ele] < arr[ele + 1]:
                    swapped = True
                    arr[ele], arr[ele + 1] = arr[ele + 1], arr[ele]

            if not swapped:
                break
        return arr

    def selection_sort(self, arr):
        """SELECTION SORT"""
        indexing_length = range(len(arr) - 1)

        for each in indexing_length:
            min_value = each

            for valu in range(each + 1, len(arr)):
                if arr[valu] < arr[min_value]:
                    min_value = valu

            if min_value != each:
                arr[min_value], arr[each] = arr[each], arr[min_value]

            return arr

    def selection_asc(self, arr):
        """SELECTION SORT(ACCENDING ORDER)"""
        n = len(arr)

        for i in range(n - 1):
            min_idx = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def selection_desc(self, arr):
        """SELECTION SORT(DECENDING ORDER)"""
        num = len(arr)

        for i in range(num - 1, 0, -1):
            max_idx = 0

            for j in range(1, i + 1):
                if arr[j] < arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        """INSERTION SORT"""
        indexing_length = len(arr)

        for i in range(1, indexing_length):
            temp = arr[i]
            k = i

            while k > 0 and temp < arr[k - 1]:
                arr[k] = arr[k - 1]
                k -= 1
                arr[k] = temp
        return arr

    def insertion_asc(self, arr):
        """INSERTION SORT(ACCENDING ORDER)"""
        indexing_length = len(arr)
        for i in range(1, indexing_length):
            value_to_sort = arr[i]

            while arr[i - 1] > value_to_sort and i > 0:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1

        return arr

    def insertion_desc(self, arr):
        """INSETTION SORT(DECENDING ORDER)"""
        n = len(arr)
        for i in range(1, n):
            x = arr[i]
            j = i - 1

            while j >= 0 and x > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = x

        return arr


lst = [random.randint(10, 99) for _ in range(10)]
print("Before Soring: ", lst)

obj = CustomSort()
print(f"\n\nBubble Sort: {obj.bubble_sort(lst.copy())}")
print(f"Bubble ASC: {obj.bubble_asc(lst.copy())}")
print(f"Bubble DESC: {obj.bubble_desc(lst.copy())}")

print(f"\n\nSelection Sort: {obj.selection_sort(lst.copy())}")
print(f"Selection ASC: {obj.selection_asc(lst.copy())}")
print(f"Selection DESC: {obj.selection_desc(lst.copy())}")

print(f"\n\nInsertion Sort: {obj.insertion_sort(lst.copy())}")
print(f"Insertion ASC: {obj.insertion_asc(lst.copy())}")
print(f"Insertion DESC: {obj.insertion_desc(lst.copy())}")
