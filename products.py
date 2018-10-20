products = []
price = []
while True:
    name = input('請輸入產品名稱 ：')
    if name == 'q':
    	break
    price = input('請輸入商品價格：')
#    p = []
#    p.append(name)
#    p.append(price)
#    p = [name,price]
    products.append([name,price])

print(products)

# print(products[0][0])

for p in products:
	print(p[0])
	print(p[1])
