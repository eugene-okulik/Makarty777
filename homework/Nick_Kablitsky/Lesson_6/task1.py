# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову)
# в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” и после этого выводит
# получившийся текст на экран. Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
# но уже преобразованного.
text = 'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

words = text.split()
fin_words = []

for word in words:
    if word[-1] in '.,':
        fin_words.append(word[:-1] + 'ing' + word[-1])
    else:
        fin_words.append(word + 'ing')
print(fin_words)
