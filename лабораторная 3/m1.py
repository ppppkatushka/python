# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def c(items_list, name):
    for i in range(len(items_list)):
        if (items_list[i] == name):
            return i;

for find_item in ['банан', 'груша', 'персик']:
    index_item = c(items_list, find_item);
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


