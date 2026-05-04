
def anagram_check(word1 :str,word2:str) -> bool:

    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    if word1_sorted !=word1_sorted:
        return False
    
    for i in range(len(word1_sorted)):

        if word1_sorted[i] != word2_sorted[i]:

            return False

    return True


print(anagram_check("car","rac"))