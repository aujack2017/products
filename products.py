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
	print(p[0] + '的價格是：' + p[1])
	# print(p[1])

with open('products.txt','w') as f:
  	for p in products:
  	    f.write(p[0] + ',' + p[1] + '\n')

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('名稱' + ',' + '數量' + '\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

