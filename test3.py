# Не удаляйте эти объекты - просто используйте
book: dict[int, str] = {}
PAGE_SIZE = 100
path = '/home/vtoroy/PycharmProjects/TelegramBot/book.txt'

def get_part_text(original: str, start: int, size: int) -> tuple[str, int]:
    sp = ['.', ',', '!', '?', ':', ';']
    if start + size + 1 <= len(original) and original[start + size - 1] in sp and original[start + size] in sp:
        end = start + size - 2
    else:
        end = start + size
    end = end if end <= len(original) else len(original)
    original = original[start:end]
    end = len(original)
    for i in range(len(original) - 1, 0, -1):
        if original[i] in sp:
            end = i + 1
            break
    result_string = original[0:end]
    return result_string, len(result_string)

# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    start, num_line = 0, 1
    while len(data) > 0:
        # start=0
        line, len_line = get_part_text(data, start, PAGE_SIZE)
        book[num_line] = line
        # data = data[start + len_line:]
        # # data = data[start:start + len_line]
        start = start + len_line + 1
        num_line = num_line + 1

prepare_book(path)
print(book)

# # Дополните эту функцию, согласно условию задачи
# def prepare_book(path: str) -> None:
#     with open(path, 'r', encoding='utf-8') as f:
#         data = f.read()
#     num_line = 1
#     while len(data) > 0:
#         start = 0
#         line, len_line = get_part_text(data, start, PAGE_SIZE)
#         book[num_line] = line.strip()
#         data = data[start + len_line:]
#         num_line = num_line + 1
#
# prepare_book(path)
# print(book)