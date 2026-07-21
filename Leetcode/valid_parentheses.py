

def valid(s):

    mp = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    stack = []

    for ch in s:

        if ch in mp.values():

            stack.append(ch)

        else:

            if not stack:
                return False
            if stack.pop() != mp[ch]:
                return False
            

    return len(stack) == 0


print(valid('(){{}'))


