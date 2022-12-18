from mpi4py import MPI
import math

def insertionSort(arr):
 	# ref https://www.geeksforgeeks.org/python-program-for-insertion-sort/
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

comm = MPI.COMM_WORLD
max_processors = comm.size

data = [random.randrange(1,100) for i in range(1000000)]

new_list = []
bin_size = math.floor(int((max(data)-min(data))/comm.size))

for rank in range(max_processors):
	for x in data:
		if (x >= bin_size*rank+rank) and x<=(bin_size+bin_size*rank+rank):
    		new_list.append([x])

v = comm.scatter(new_list,0)
print("Rank is ",comm.rank, " data is ", v)
v = insertionSort(v)
g = comm.gather(v,0)

if comm.rank==0:
    for i in range(len(g)):
        print("Rank:",i," ",g[i])





        