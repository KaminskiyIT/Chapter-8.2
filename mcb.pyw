#! python3
# mcb.pyw - Сохраняет и загружает фрагменты текста
# в буфер обмена.
# Использование:    руw.ехе mcb.pyw save <ключевое_слово> -
#                       Сохраняет буфер обмена в ключевое слово.
#                   руw.ехе mcb.pyw <ключевое_слово> -
#                       Загружает ключевое слово в буфер обмена.
#                   руw.ехе mcb.pyw list -
#                       Загружает все ключевые слова в буфер
#                       обмена.

import shelve, pyperclip, sys

mcbShelf = shelve.open('C:\\py_lessons\\automatic_by_py\\8\\project2\\data\\mcb')

# TODO: Сохранить содержимое буфера обмена.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: Сформировать список ключевых слов и загрузить содержимое.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
