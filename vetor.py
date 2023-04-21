def search(v, x):
    indice = 0
    i = 0
    for element in v:
        if element == x:
            indice = i
            break
        i += 1
    
    if indice == 0:
        return -1
    else: 
        return indice

def insert(v, x, k):
    if k >= len(v):
        for i in range(len(v), k):
            v.append(0)
        v.append(x)
    else:
        v.append(None)
        for i in range(len(v) - 1, k, -1):
            v[i] = v[i - 1]
        v[k] = x
        
            
            
def remove(v, x):
    for i in range(len(v)):
        if v[i] == x:
            for j in range(i, len(v) - 1):
                v[j] = v[j + 1]
            v.pop()
            return i
    return -1


v = [0, -1, -2, -2, -4, -5]
rs = search(v, -2)
print(rs)

insert(v, 2, 3)
print(v)

insert(v, 10, 10)
print(v)

rr = remove(v, -2)
print(rr)

print(v)

