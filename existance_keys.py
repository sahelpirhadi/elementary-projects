def existance_keys(a,b):
    final=[]
    for x in a:
        if b in a[x]:
            final.append(x)
    final.sort()
    return final





sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}

print(existance_keys(sample,2))
