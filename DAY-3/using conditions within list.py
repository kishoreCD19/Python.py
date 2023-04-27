#return "orange" instead of "banana"
fruits = ["banana","orange","apple"]
newlist = [x if x != "banana" else "orange" for x in fruits ]
print (newlist)


// output = ['orange', 'orange', 'apple'] //
