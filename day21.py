import time


def read_file(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_list =[sub.replace('(', '').replace(')', '').replace(',', '').split(' contains ') for sub in content_list]
    for idx, i in enumerate(content_list):
        content_list[idx][0] = i[0].split()
        content_list[idx][1] = i[1].split()
    return content_list


def find_allergen(lst, allergen, products, allergens, product_allergen):
    allergen_product = []
    for k in lst:
        if allergen in k[1]:
            allergen_product.append(k[0])
    all_pr = list(set.intersection(*map(set,allergen_product)))
    if len(all_pr) == 1:
        all_pr = all_pr[0]
    else:
        if len([value for value in all_pr if value in products]) == 1:
            all_pr = [value for value in all_pr if value in products][0]
        else:
            return products, [allergens[-1]] + allergens[:-1], product_allergen
    products[:] = (value for value in products if value != all_pr)
    allergens.pop(allergens.index(allergen))
    product_allergen.append([all_pr, allergen])
    return products, allergens, product_allergen


start_time = time.time()
l = read_file('input_d21.txt')
no_allergens = []
allergens = []
products = []
for i in l:
    products.extend(i[0])
    allergens.extend(i[1])

allergens = list(dict.fromkeys(allergens))
product_allergen = []
while len(allergens) != 0:
    products, allergens, product_allergen = find_allergen(l, allergens[0], products, allergens, product_allergen)

print('1st part answer: ', len(products))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

product_allergen.sort(key = lambda x: x[1])
str = ''
for i in product_allergen:
    str += i[0]+','

print('2nd part answer: ', str)
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
