num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

num_list = [num1, num2, num3, num4]
num_average = sum(num_list) / len(num_list)

num_product = num1 * num2 * num3 * num4

print(f'{num_product:.0f} {num_average:.0f}')
print(f'{num_product:.3f} {num_average:.3f}')