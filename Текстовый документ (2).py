a, b, c = int(input()), int(input()), int(input())

# if a > c and b > c:
#     print('Равнобедренный')
if a == b == c:
    print('Равносторонний')

elif a == b or a == c or b == c:
    print('Равнобедренный')

else:
    print('Разносторонний')

