class RabinKarp:

    def __init__(self,pattern,text):
        self.pattern = pattern
        self.text = text
        #size of the alphabet (26)
        self.d = 26
        #prime number for modulo number
        self.q = 31


    def search(self):

        m = len(self.pattern)
        n = len(self.text)

        #hashes for region of text and pattern
        hash_text = 0
        hash_pattern = 0

        #largest ploynomial term 
        h = 1

        for _ in range(m-1):
            h = (h*self.d) % self.q

        #pre compute the hash of the pattern O(M)

        for i in range(m):
            #fingerprint function
            hash_pattern = (self.d * hash_pattern + ord(self.pattern[i])) % self.q
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.q


        #slide the pattern over the text one by one
        for i in range(n-m+1):

            #chech the hash value of current window of the text
            # and pattern .if the values match then only check charachters one by one

            if hash_text == hash_pattern:

                #naive apparoch to  check the characters 

                j = 0

                while j < m :
                    if self.text[i+j] != self.pattern[j]:
                        break
                    j = j + 1

                if j == m :
                    print("Found match at index %s" % i)


        
            # update the hash for the actuall substring of the text
            #apply rolling hash approch

            if i < n - m:

                hash_text = (self.d * (hash_text - ord(self.text[i]) * h) + ord(self.text[i+m])) % self.q

                # we might get negative value so we have to make sure the hash is positive
                if hash_text < 0:
                    hash_text = hash_text + self.q




if __name__ == '__main__':

    algorithm = RabinKarp('abcd','abcdfgashdshabcd')
    algorithm.search()















