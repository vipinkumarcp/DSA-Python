

def naive_search(pattern,text):

    m = len(pattern)
    n = len(text)

    for i in range(n-m+1):

        j = 0

        while j < m :

            if text[i+j] != pattern[j]:
                break

            j = j +1

            if m == j:

                print(f"found at {i} ")


if __name__ == '__main__':

    naive_search('abcd','abcdfghhabcd')



