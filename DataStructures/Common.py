import collections


squares = {x: x * x for x in range(6)}
print(squares)
d1 = collections.OrderedDict(one=1,two=2,three=3)
print(d1,d1.keys())

d2 = {"Yehonatan" : 1, "Tseva": 2}
chain = collections.ChainMap(d1,d2) #multiple dict's into a single mapping
print(chain)

for key in d2:
    print(key)

for key in d2: #printing values
    print(d2[key])

#another approach is using items , then iterate through it:
for item in d2.items():
    print(item)
    print(type(item))

#Following items, we can access key/values directly
values = d2.values()
keys = d2.keys()

#adding or removing keys -> converting the view returned from .keys() into a list.
for key in list(d2.keys()):  # Use a list instead of a view, accessing without a list will raise Runtime Error
    if key == 'Tseva':
        del d2[key]  # Delete a key from prices

print(d2.keys())

for key in sorted(d1, reverse=True): #backwards lexicographical order
    print(key, d1[key])