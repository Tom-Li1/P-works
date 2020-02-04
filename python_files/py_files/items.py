width = int(input("Please enter width:"))

price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print("=" * width)

print(header_fmt.format("Itmes", "Price"))

print("-" * width)

print(fmt.format('A', 0.4))
print(fmt.format('B', 0.5))
print(fmt.format('C', 1.92))
print(fmt.format('D(500ml)', 8))
print(fmt.format('E(150g)', 5))

input()