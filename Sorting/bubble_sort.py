def bubble_sort(lst):
    num = len(lst)
    for itm in range(0, num - 1):
        is_swapped = False
        for vlu in range(0, num - itm - 1):
            if lst[vlu] > lst[vlu + 1]:
                lst[vlu], lst[vlu + 1] = lst[vlu + 1], lst[vlu]
                is_swapped = True
        if not is_swapped:
            break
    return lst
    
if __name__ == "__main__":
    lst = [3,5,6,7,8,9,1,4,2,0]
    print("\n\nBefore Sorting: ", lst)
    data_bubble_sort = bubble_sort(lst)
    print("AFTER BUBBLE SORT: ", data_bubble_sort)
    