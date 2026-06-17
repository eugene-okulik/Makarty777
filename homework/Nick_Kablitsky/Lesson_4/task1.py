# просто кортеж
# tuple = (varTuple_1, varTuple_2, varTuple_3, varTuple_4, varTuple_5)
#
# список
# list = [varList_1, varList_2, varList_3, varList_4, varList_5]
#
# просто словарь
# dict = {
#   'keyDict1': varDict1,
#   'keyDict2': varDict2,
#   'keyDict3': varDict3,
#   'keyDict4': varDict4,
#   'keyDict5': varDict5
# }
#
# просто множество
# set = {varSet_1, varSet_2, varSet_3, varSet_4, varSet_5}

# в словарь пихаем каждый элемент

varTuple_1, varTuple_2, varTuple_3, varTuple_4, varTuple_5 = 1, 2, 3, 4, 5
varList_1, varList_2, varList_3, varList_4, varList_5 = 'one', 'two', 'three', 'four', 'five'
varDict_1, varDict_2, varDict_3, varDict_4, varDict_5 = 'I', 'like', 'Yamaha', 'and', 'Honda'
varSet_1, varSet_2, varSet_3, varSet_4, varSet_5 = 1, 2, 3, 4, 5

my_dict = {
    'tuple': (varTuple_1, varTuple_2, varTuple_3, varTuple_4, varTuple_5),
    'list': [varList_1, varList_2, varList_3, varList_4, varList_5],
    'dict': {
        'keyDict1': varDict_1,
        'keyDict2': varDict_2,
        'keyDict3': varDict_3,
        'keyDict4': varDict_4,
        'keyDict5': varDict_5
        },
    'set': {varSet_1, varSet_2, varSet_3, varSet_4, varSet_5}
    }

# Для того, что хранится под ключом 'tuple': выведите на экран последний элемент
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом 'list': добавьте в конец списка еще один элемент, удалите второй элемент списка.
varList_6 = 'six'
my_dict['list'].append(varList_6)
my_dict['list'].pop(1)

# Для того, что хранится 
# под ключом 'dict': добавьте элемент с ключом ('i am a tuple',), любым значением удалите какой-нибудь элемент.
my_dict['dict'][('i am a tuple',)] = '1'
del my_dict['dict']['keyDict_4']

# Для того, что хранится под ключом 'set': добавьте новый элемент в множеств, удалите элемент из множества.
varSet_6 = 6
my_dict['set'].add(varSet_6)
my_dict['set'].remove(varSet_6)
