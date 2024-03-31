def insertion_sort(lst):
    for itm in range(1, len(lst)):
        key = lst[itm]
        j = itm -1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

if __name__ == "__main__":
    lst = [1,9,3,7,2,8,4,6,5,0]
    print("\n\nBefore Sorting: ", lst)
    data_insertion_sort = insertion_sort(lst)
    print("AFTER INSERTION SORT: ", data_insertion_sort)