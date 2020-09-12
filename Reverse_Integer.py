class Reverse(object):
    def rev(self, number):
        result = 0
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        def divide(number, divider):
                return int(number * 1.0 / divider)

        def mod(number, m):
            if number < 0:
                return number % -m
            else:
                return number % m

        while number:
            a = mod(number, 10)
            number = divide(number, 10)
            if result > divide(MAX_INT, 10) or (result == divide(MAX_INT, 10) and mod(MAX_INT, 10) > 7):
                return 0
            if result < divide(MIN_INT, 10) or (result == divide(MIN_INT, 10) and mod(MIN_INT, 10) < -8):
                return 0
            result = result * 10 + a
        return result

number = -45678
class_output = Reverse()
print(class_output.rev(number))








