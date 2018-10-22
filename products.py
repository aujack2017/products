import csv,codecs,os
products = []

#讀取檔案，放入products[]

if os.path.isfile('products.csv'): #檢查檔案在不在
	print('yeah!找到檔案了')

	with codecs.open('products.csv', 'r', encoding='utf-8_sig') as f:
		for line in f:
			if '名稱' in line:
				continue	#繼續
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('找不到檔案~~SORRY')


#輸入產品及價錢
while True:
    name = input('請輸入產品名稱 ：')
    if name == 'q':
    	break
    price = int(input('請輸入商品價格：'))
    products.append([name,price])

print(products)


#寫入檔案
for p in products:
	print(p[0] + '的價格是：' + str(p[1]))
	# print(p[1])

with codecs.open('products.txt','w',encoding='utf-8_sig') as f:
  	for p in products:
  	    f.write(p[0] + ',' + str(p[1]) + '\n')

with codecs.open('products.csv', 'w', encoding='utf-8_sig') as f:
    f.write('名稱' + ',' + '數量' + '\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')




