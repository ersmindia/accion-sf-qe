l= ['APPLE', 'FOX', 'ANT', 'BAT', 'BALL']
print l
l_size=len(l)
temp=''
sort_list=[]
for i in range(l_size):
	print i
	for j in l:
		print j
		if(i<l_size):
			if(j>l[i+1]):
				temp=j
				l[i]=l[i+1]
				l[i+1]=temp
				print l
print l

				
	