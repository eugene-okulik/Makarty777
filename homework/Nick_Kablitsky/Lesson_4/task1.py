# Объявляем переменные.
var_tuple_1, var_tuple_2, var_tuple_3, var_tuple_4, var_tuple_5 = 1, 2, 3, 4, 5
var_list_1, var_list_2, var_list_3, var_list_4, var_list_5 = 'one', 'two', 'three', 'four', 'five'
var_dict_1, var_dict_2, var_dict_3, var_dict_4, var_dict_5 = 'I', 'like', 'Yamaha', 'and', 'Honda'
var_set_1, var_set_2, var_set_3, var_set_4, var_set_5 = 1, 2, 3, 4, 5

# Создаем словарь.
my_dict = {
    'tuple': (var_tuple_1, var_tuple_2, var_tuple_3, var_tuple_4, var_tuple_5),
    'list': [var_list_1, var_list_2, var_list_3, var_list_4, var_list_5],
    'dict': {
        'key_dict1': var_dict_1,
        'key_dict2': var_dict_2,
        'key_dict3': var_dict_3,
        'key_dict4': var_dict_4,
        'key_dict5': var_dict_5
    },
    'set': {var_set_1, var_set_2, var_set_3, var_set_4, var_set_5}
}

# Для того, что хранится под ключом 'tuple': выведите на экран последний элемент.
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом 'list': добавьте в конец списка еще один элемент, удалите второй элемент списка.
var_list_6 = 'six'
my_dict['list'].append(var_list_6)
my_dict['list'].pop(1)

# Для того, что хранится.
# под ключом 'dict': добавьте элемент с ключом ('i am a tuple',), любым значением удалите какой-нибудь элемент.
my_dict['dict'][('i am a tuple',)] = '1'
del my_dict['dict']['key_dict_4']

# Для того, что хранится под ключом 'set': добавьте новый элемент в множеств, удалите элемент из множества
var_set_6 = 6
my_dict['set'].add(var_set_6)
my_dict['set'].remove(var_set_6)

# Выод на экран словря
print(my_dict)
