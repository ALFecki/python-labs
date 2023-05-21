from .constants import VALUE, TYPE, ARRAY_IN_ARRAY_REGEX, ARRAY_REGEX, VALUE_REGEX
import re


def to_json(obj) -> str:
    if type(obj) == tuple:
        serialized = []
        for i in obj:
            serialized.append(f"{to_json(i)}")
        ans = ", ".join(serialized)
        return f"[{ans}]"
    else:
        return f"\"{str(obj)}\""


def from_json(data: str):
    if data == '[]':
        return tuple()
    elif data[0] == '[':
        data = data[1:len(data) - 1]
        parsed = []
        depth = 0
        quote = False
        substr = ""
        for i in data:
            if i == '[':
                depth += 1
            elif i == ']':
                depth -= 1
            elif i == '\"':
                quote = not quote
            elif i == ',' and not quote and depth == 0:
                parsed.append(from_json(substr))
                substr = ""
                continue
            elif i == ' ' and not quote:
                continue

            substr += i

        parsed.append(from_json(substr))
        return tuple(parsed)
    else:
        return data[1:len(data) - 1]
