# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero” и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
# но уже преобразованного.

# Непосредственно текст
text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

# Инициализация словаря и дробление текста
words = text.split()
fin_words = []

# Цикл перебора раздробленных слов
for word in words:
    # Поиск на конце слова '.' или ','
    if word[-1] in '.,':
        # Если нашлось, то не учитываем ласт символ(знак препинания), добавляем к нему ing + переместить знак
        fin_words.append(word[:-1] + 'ing' + word[-1])
    # Если не нашлось '.' или ',', то тупо добавляем ing
    else:
        fin_words.append(word + 'ing')
print(' '.join(fin_words))
