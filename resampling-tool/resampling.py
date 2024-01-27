from random import shuffle
import sys
import numpy as np
import math

source_file = input("Enter the name of file you would like to open and process: ")
with open(source_file, 'r') as f:
    data = np.genfromtxt(f,delimiter=";",encoding="utf-8",dtype="str",usecols=(0,1,2,3,4))

number_of_blocks = int(input("Enter the number of blocks your IDs belong to: "))
number_of_chunks = int(input("Enter the number of chunks to split block into: "))
number_of_resamples = int(input("Enter the number of chunks to resample your chunks: "))
print(end = "\n")

#np.set_printoptions(threshold=sys.maxsize)
experimental_set = np.empty((number_of_blocks,number_of_resamples,number_of_chunks))
for i in range(1,number_of_blocks+1):
	a = data[np.where(data[:,1] == str(i))]
	for z in range(1,number_of_resamples+1):
		sumchecklist = [None] 
		while True:
			np.random.shuffle(a)
			lena = ((np.size(a,0)//number_of_chunks))
			osta = ((np.size(a,0)%number_of_chunks))
			#print("This is block №", i, ", resample iteration № ", z, end = "\n")
			print(lena, osta, end = ", but after optimization of size: ")
			if osta != 0:
				b = a[:(osta*(-1)), :]
			else:
				b = a
			lenb = ((np.size(b,0)//number_of_chunks))
			ostb = ((np.size(b,0)%number_of_chunks))
			print(lenb, ostb, end = "\n")
			clst = np.vsplit(b, number_of_chunks)
			if clst not in sumchecklist:
				break
			else:
				print("!!!!!!!!!!!!!!!!!!!!! Protection from similar selections triggered, reshuffling the selection", end = "\n")
				continue
		sumchecklist.append(clst) 
		for idx, element in enumerate(clst):
			#print(element, end="\n\n")
			delivered = data[np.where(element[:,2] == "1")]
			opened = data[np.where(element[:,3] == "1")]
			openrate = float(np.size(opened,0)/np.size(delivered,0))
			print("This is block №", i, ", resample iteration № ", z, ", chunk №", idx+1, end = "\n")
			print(openrate, end = "\n\n")
			experimental_set[i-1,z-1,idx]=openrate
print(experimental_set, end = "\n\n")

for i in range(len(experimental_set)):
	ORsum = 0.0
	w = 0
	for j in range(len(experimental_set[i])):
		for k in range(len(experimental_set[i][j])):
			ORsum = ORsum + experimental_set[i][j][k]
			w = w+1
	ORaverage = float(ORsum/w)
	Variance = 0.0
	w = 0
	for j in range(len(experimental_set[i])):
		for k in range(len(experimental_set[i][j])):
			Variance = Variance + (ORaverage - experimental_set[i][j][k])**2
			w = w + 1
	Variance = Variance / (w-1)
	se = math.sqrt(Variance)
	delta = 1.96*se
	minv = ORaverage-delta
	maxv = ORaverage+delta
	print("Average OR Block №", i+1," is ", ORaverage, " +- ", delta, " -  from ", minv, " to ", maxv, end="\n\n")