a = 33
b = 11
# def f (a, b):
#     if b == 0:
#         return 1
#     elif b % 2 == 0:
#         a = a * a
#         b = b // 2
#         return a * f(a, b - 1)
#     else:
#         return a * f(a, b - 1)
# print(f (a, b))


def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
print(sum(a, b))






