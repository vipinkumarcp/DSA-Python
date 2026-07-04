
def count_ocuurance(pattern,text):

    m = len(pattern)
    n = len(text)

    count = 0

    for i in range(n-m+1):

        j = 0
       

        while j < m:

            if text[i+j] != pattern[j]:
                break

            j = j+1

        if j == m :

            count = count + 1

            print(f"pattern occured at index {i}")


    return f"total times pattern occures {count}"
        


if __name__ == '__main__':

    print(count_ocuurance('abcd','abcdfghhabcd'))

    
