from random import random
import numpy as np
a = np.array([[1,0,1,0],
			  [1,1,0,0],
			  [0,1,0,1],
			  [0,0,1,1]])

toSolve = np.array([[1,0,1,0],
			        [1,2,0,0],
			        [2,1,2,2],
			        [0,0,1,1]])
allTwos = np.array([[2,2,2,2],
			        [2,2,2,2],
			        [2,2,2,2],
			        [2,2,2,2]])
def checkRows(arr):
	passedTest = True
	for row in arr[:]:
		# print row
		countZeros = 0
		countOnes = 0
		for column in row:
			if column == 0:
				countZeros += 1
			if column == 1:
				countOnes += 1
		if countOnes != countZeros:
			passedTest = False
	return passedTest

def checkColumns(arr):
	passedTest = True 

	columns = []
	for i in range(4):
		columns+=[arr[:,i]]
	for column in columns:
		countZeros= 0
		countOnes= 0
		for row in column:
			if row == 0:
				countZeros += 1 
			if row == 1:
				countOnes += 1 
		if countOnes !=countZeros:
			passedTest = False 
	return passedTest				


def checkIdenticalRow(arr):
	passedTest = True
	rows = arr[:]
	# print np.bincount(rows)
	# print rows
	listRows = []
	for row in rows:
		listRows.append(list(row))

	for row in listRows:
		if listRows.count(row) != 1:
			passedTest = False
	return passedTest

def checkIdenticalColumn(arr):
	passedTest = True 

	listColumns = []
	for i in range(4):
		listColumns+=[list(arr[:,i])]
	for column in listColumns:
		if listColumns.count(column) != 1:
			passedTest = False
	return passedTest
def solve(arr):
	arrayToSolve = arr[:,:]

	workingArray = []
	unsolved = True
	solvedArray = []
	i = 0
	while unsolved == True:
		# The janky way of breaking the reference chain
		workingArray = np.array(list(arr[:,:]))

		# print('unsolved')
		# print workingArray
		for idx,row in enumerate(workingArray[:,]):
			# print row
			workingArray[idx,:] = np.array([int(round(random())) if elem > 1 else elem for elem in workingArray[idx,:]])
			# workingArray[idx,:] = [round(random()) if elem > 1 else elem for elem in workingArray[idx,:]]
		# print('test solution')
		# print workingArray
		# if workingArray.all() == a.all():
		# 	print(work)
		# 	print('success')
		i +=1
		if checkRows(workingArray) and checkColumns(workingArray) and checkIdenticalRow(workingArray) and checkIdenticalColumn(workingArray):
		 print('success')
		 unsolved = False
		 solvedArray = workingArray
		 print('%s tries'%str(i))
	return solvedArray 



print 'rows good', checkRows(a) 	
print 'columns good', checkColumns(a)
print 'iden row good', checkIdenticalRow(a)
print 'iden column good', checkIdenticalColumn(a)
print solve(allTwos)