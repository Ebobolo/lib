start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start > end:
    start, end = end, start

for num in range(start, end + 1):
    if num % 2 != 0:
        print(num)