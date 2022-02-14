# Array

### iterate backwards
> [i for i in range(len(nums)-1, -1, -1)]
### sort multiple arrays based on one
> [x for _, x in sorted(zip(Y, X), key=lambda s: s[0])]

# Dictionary
### Sort
> sorted(dict)
### sort by keys
> sorted(mydict.items(), key=lambda x: x[0])
### find key by max value
> max(mydict, key=mydict.get)

# Set
### merge two set
> set(l1) | set(l2)
### find common element of two sets
> set(l1) & set(l2)
