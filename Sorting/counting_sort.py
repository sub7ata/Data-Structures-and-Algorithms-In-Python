def counting_sort(l=None,k=None):
	output = [0] * len(l)
	count = [0] * k
	for i in l:
		count[i] = count[i]+1
	for i in range(1,k):
		count[i] = count[i] + count[i-1]
	for i in reversed(l):
		output[count[i]-1] = i
		count[i] = count[i] - 1
	for i in range(len(l)):
		l[i] = output[i]

if __name__ == "__main__":
    l = [1, 4, 4, 1, 0, 1]
    K = 5
    print(f"\nBEFORE SORTING:\t\t {l}" )
    counting_sort(l,K)
    print(f"AFTER INSERTION SORT:\t {l}\n")