#using set function we make add the two sets
print("Enter 5 Elements for Set A: ")
setOne = []
for i in range(5):
    setOne.append(input())
setOne = set(setOne)

print("Enter 5 Elements for Set B: ")
setTwo = []
for i in range(5):
    setTwo.append(input())
setTwo = set(setTwo)

print("\nUnion of Two Sets A and B are:")
print(setOne | setTwo)


// output= Enter 5 Elements for Set A: 
2
5
6
3
5
Enter 5 Elements for Set B: 

5
5
6
9
7
Union of Two Sets A and B are:
{'2', '', '9', '7', '5', '3', '6'}   //
