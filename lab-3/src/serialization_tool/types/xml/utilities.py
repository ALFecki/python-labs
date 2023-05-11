import re
from .constants import VALUE_REGEX

intent = 0


def to_xml(obj):
    if type(obj) == tuple:
        serialized = []
        for el in obj:
            global intent
            intent += 1
            isType = False
            if type(el) == tuple:
                isType = True
            serialized.append(
                f"\n"
                + ((intent - 1) * "\t")
                + f"<{type(el).__name__}>"
                + (isType * intent * "\t")
                + f"{to_xml(el)}"
                + (isType * '\n')
                + (isType * (intent - 1) * "\t")
                + f"<{type(el).__name__}/>"
            )
            intent -= 1
        res = " ".join(serialized)
        return f"{res}"
    else:
        return f"{str(obj)}"

string_count = 0
depth = 0

def from_xml(data: list[str]):
    result = []
    temp_tuple = []
    global string_count, depth
    data = data[string_count:len(data) - string_count]
    for string in data:
        string_count += 1
        if "<tuple>" in string:
            depth += 1
        if not "<tuple>" in string and not "<tuple/>" in string:
            if depth > 1:
                temp_tuple.append(from_xml(data[string_count:len(data) - string_count]))
            value_str = re.search(VALUE_REGEX, string).group(1)
            temp_tuple.append(value_str)
        elif "<tuple/>" in string:
            depth -= 1
            if len(temp_tuple) != 0:
                result.append(tuple(temp_tuple))
                temp_tuple.clear()
    if len(temp_tuple) != 0:
        result.append(tuple(temp_tuple))
    return tuple(result)