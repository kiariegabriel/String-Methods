l=['Hey','There','Buddy']
l_n=list()
for i in range(len(l)):
	n=l[i].replace(l[i][0],'')
	l_n.append(n)
print(l_n)