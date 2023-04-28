
BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

"""Работает если нет ..."""
# def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
#     page_text = text[start:start+size]
#     c = 0
#     for i in page_text[::-1]:
#         if i in [',', '.', '!', ':', ';', '?']:
#             break
#         c += 1
#     return (text[start:start+size-c], len(text[start:start+size-c]))

# text = '— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, в чём вопрос.'
# text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'
# text = 'Раз. Два. Три. Четыре. Пять. Прием!'
# Функция, возвращающая строку с текстом страницы и ее размер
start, size = 0, 0
symbols = [',', '.', '!', ':', ';', '?']
tx = ''
# text = 'Да? Вам показалось?.. Ну, хорошо,'
text = 'Да? Ну,..'
def get_part_text(text, start, size):
    c = 0
    print('start + size =', start + size, 'len =', len(text))
    tx = text[start:]
    rs = ''
    l_s = []
    rsum = 0
    for s in tx.split():
        print(s, len(s))
        if c == 0:
            rs = s
            c = 1
            l_s.append(s)
        else:
            if len(rs) < size:
                l_s.append(s)
                c = c + 1
            else:
                break
            rs = rs + ' ' + s
        print(len(rs), size)

    # rs = " ".join(l_s)

    return (rs, len(rs))

    # text_r = tx[::-1]
    # print(text_r)
    # for j in range(len(text_r)):
    #     if text_r[j] in symbols:
    #         c = c + 1
    #         print('j...=', j)
    #     else:
    #         return (text[start:len_tx], len(text[start:len_tx]))
    #     # elif text_r[j] in symbols and text_r[j - 1] not in symbols and text_r[j + 1] not in symbols:
    #     #     print('j.=', j)
    #     #     return (text[start:start + size], len(text[start:start + size]))
print(*get_part_text(text, 0, 6), sep='\n')

# print(*_get_part_text(text, 5, 9), sep='\n')
# print(*_get_part_text(text, 22, 145), sep='\n')
# print(*_get_part_text(text, 22, 30), sep='\n')
# print(*_get_part_text(text, 54, 70), sep='\n')
# print(*_get_part_text(text, 0, 54), sep='\n')
    # # end_signs = ',.!:;?'
    # # counter = 0
    # # if len(text) < start + size:
    # #     size = len(text) - start
    # #     text = text[start:start + size]
    # # else:
    # #     if text[start + size] == '.' and text[start + size - 1] in end_signs:
    # #         text = text[start:start + size - 2]
    # #         size -= 2
    # #     else:
    # #         text = text[start:start + size]
    # #     for i in range(size - 1, 0, -1):
    # #         if text[i] in end_signs:
    # #             break
    # #         counter = size - i
    # # page_text = text[:size - counter]
    # # page_size = size - counter
    # return page_text, page_size


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass
    # with open(path, 'r') as file:
    #     text = file.read()
    # start, page_number = 0, 1
    # while start < len(text):
    #     page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
    #     start += page_size
    #     book[page_number] = page_text.strip()
    #     page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)