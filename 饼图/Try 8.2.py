values = [0.123456, 0.789012, 0.999]

# 保留一位小数的百分比值
print("One decimal place:")
for value in values:
    # print(f"{value:1.1f}%%")
    print('{:1.1f}'.format(value))

# 保留两位小数的百分比值
# print("\nTwo decimal places:")
# for value in values:
#     print(f"{value:1.2f}%%")
#
# # 保留三位小数的百分比值
# print("\nThree decimal places:")
# for value in values:
#     print(f"{value:1.3f}%%")
