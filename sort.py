L = [12,-42,-9,5,45,100]

def tri_insertion(L):
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] < cle:
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle
    
tri_insertion(L)
print(L)