def _get_part_text(original: str, start: int, size: int) -> tuple[str, int]:
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