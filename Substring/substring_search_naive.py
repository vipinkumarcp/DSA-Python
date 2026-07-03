
def naive_search(pattern,text):

    m = len(pattern)
    n =  len(text)

#this operation takes O(n)  

    for i in range(n-m+1):

        #track the letters in the pattern (starting 0)
        #from left to right

        j = 0

        #consider all the letters of the pattern o(m)
        #this approch take o(m*n)
        while j<m:

            if text[i+j] != pattern[j]:
                break

            #consider next character
            j = j + 1

        if j == m:

            print("Found match at index ", i)



if __name__ == '__main__':

    naive_search('abcd','abcdfghhabcd')



