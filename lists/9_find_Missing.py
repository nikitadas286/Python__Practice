lst = [1, 2, 3, 5]
n = 5
expected = n*(n+1)//2
actual = sum(lst)

print(expected - actual)