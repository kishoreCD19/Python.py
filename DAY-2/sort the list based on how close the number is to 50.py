#sort the list based on how close the number is to 50:
def myfunc (n):
    return abs (n-50)
thislist = [100,50,65,82,73]
thislist.sort(key = myfunc)
print(thislist)

// output = [50, 65, 73, 82, 100] //
