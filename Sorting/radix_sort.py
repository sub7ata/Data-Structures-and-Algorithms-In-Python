def counting_sort(l,pos):
	output = [0] * len(l)
	count = [0] * 10
	for i in range(0,len(l)):
		index = (l[i]//pos)%10
		count[index] = count[index]+1
	for i in range(1,10):
		count[i] = count[i] + count[i-1]
	i = len(l)-1
	while i>=0:
		index = (l[i]//pos)%10
		output[count[index]-1] = l[i]
		count[index] = count[index]-1
		i=i-1
	for i in range(0,len(l)):
		l[i] = output[i]

def radix_sort(l):
	mx = max(l)
	pos = 1
	while mx//pos>0:
		counting_sort(l,pos)
		pos = pos * 10
if __name__ == "__main__":
    l = [319, 212, 6, 8, 100, 50]
    print(f"\nBEFORE SORTING:\t\t {l}" )
    radix_sort(l)
    print(f"AFTER REDIX SORT:\t {l}\n")