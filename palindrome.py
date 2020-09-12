"""
Time - O(n) (n is the number of digits)
O(log(k)) - K is the size of the number log 1000 -> 3, log 100 -> 2

Space - O(1)

"""

class Palindrome(object):
    def PalindromeCheck(self, n):
        b = n
        result = 0
        if n < 0:
            return False
        while b:
            a_mod = b % 10
            b = b // 10
            result = result * 10 + a_mod
        return result == n

n = 121
class_output = Palindrome()
print(class_output.PalindromeCheck(n))