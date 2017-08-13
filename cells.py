import numpy as np
import matplotlib.pyplot as plt

c = input("Enter number of cells:")
phase = ["G1", "S", "G2/M"]
a = np.zeros((3,3), dtype = np.int32)

for i in range(0,3):
	print "For phase "+ phase[i]
	a[i][0] = input("Enter the number of cells having RNA in only nucleoplasm:")
	a[i][1] = input("Enter the number of cells having RNA in only nucleolus:")
	a[i][2] = input("Enter the number of cells having RNA present in both:")

	tot = int(a[i][0]+a[i][1]+a[i][2])
	v1 = int(a[i][0])
	v2 = int(a[i][1])
	v3 = int(a[i][2])
	print tot

	if tot != c:
		print "Total number of cells are not equal!"
		break

	p1 = (v1*100.0)/tot
	p2 = (v2*100.0)/tot
	p3 = (v3*100.0)/tot

	print v1, type(v1)
	print tot, type(tot)
	print p1, type(p1)
	print p2
	print p3

	val = [p1,p2,p3]
	obj = ('one','two','three')
	ypos = np.arange(len(obj))

	plt.bar(ypos, val, align='center', alpha=0.5)
	plt.xticks(ypos, obj)
	plt.ylabel('some y')
	plt.xlabel('Phase')
	plt.title('some x')

	# plt.hist(val,bins=3)
	plt.show()

# data to plot
n_groups = 3
g1 = (a[0][0], a[1][0], a[2][0])
g2 = (a[0][1], a[1][1], a[2][1])
g3 = (a[0][2], a[1][2], a[2][2])

 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, g1, bar_width,
                 alpha=opacity,
                 color='b',
                 label='G1')
 
rects2 = plt.bar(index + bar_width, g2, bar_width,
                 alpha=opacity,
                 color='g',
                 label='S')

rects3 = plt.bar(index + bar_width + bar_width, g3, bar_width,
                 alpha=opacity,
                 color='r',
                 label='G2/M')
 
plt.xlabel('Phase')
plt.ylabel('Percentage of cell')
plt.title('RNA in cells')
plt.xticks(index + bar_width, ('G1', 'S', 'G2/M'))
plt.legend()
 
plt.tight_layout()
plt.show()
