def selection_sort(lst):
    for itm in range(len(lst)):
        min_idx = itm
        for vlu in range(itm+1, len(lst)):
            if lst[min_idx] > lst[vlu]:
                min_idx = vlu
            lst[itm], lst[min_idx] = lst[min_idx], lst[itm]
                
    return lst

if __name__ == "__main__":
    lst = [9,3,88,4,22,5,66,7,1]
    print("\n\nBefore Sorting: ", lst)
    data_selection_sort = selection_sort(lst)
    print("AFTER SELECTION SORT: ", data_selection_sort)
