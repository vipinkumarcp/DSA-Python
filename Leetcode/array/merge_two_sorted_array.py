
def merge(a,b):

    i=j = 0

    ans = []

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            ans.append(a[i])
            i+=1

        else:

            ans.append(b[j])
            j+=1
    
    ans.extend(a[i:])
    ans.extend(b[j:])

    return ans


print(merge([1,2,4],[3,5,6]))
