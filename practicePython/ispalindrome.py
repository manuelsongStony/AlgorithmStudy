
def is_palindrome(string):
    result = False

    n = len(string)
    for i in range(n // 2):
        if  string[i] != string[n - 1 - i]:
            return  result

    result = True
    return result


print(is_palindrome("abcaba"))