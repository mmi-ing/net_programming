my_url = 'https://search.daum.net/search?w=tot&q=bigdata'

my_list = my_url.split('?')[1].split('&')

my_dic = {}

for list in my_list:
    key, value = list.split('=')
    my_dic[key] = value

print(my_dic)

my_dic['q'] = 'iot'
print(my_dic)
