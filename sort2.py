l=['APPLE', 'FOX', 'ANT', 'BAT', 'BALL']
print l
sort_list=[]
for j in l:
	print j
	if(j==l[0]):
		sort_list.insert(0,j)
	elif(j==l[1]):
		sort_list.insert(4,j)
	elif(j==l[2]):
		sort_list.insert(1,j)
	elif(j==l[3]):
		sort_list.insert(2,j)
	elif(j==l[4]):
		sort_list.insert(3,j)
		
print sort_list
