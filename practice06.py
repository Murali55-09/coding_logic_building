#  Print the table of a given number (n × 1 to n × 10).
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")   

#  Print the sum of first n natural numbers.
n = 10
sum_natural = sum(range(1, n + 1))
print(f"The sum of the first {n} natural numbers is: {sum_natural}")