from .constants import VALUE, TYPE, ARRAY_IN_ARRAY_REGEX, ARRAY_REGEX, VALUE_REGEX, TYPES
from .constants import RegularExpressions as Expression
import regex



def to_json(obj) -> str:
    # if type(obj) == tuple:
    #     serialized = []
    #     for i in obj:
    #         serialized.append(f"{to_json(i)}")
    #     ans = ", ".join(serialized)
    #     return f"[{ans}]"
    # else:
    #     return f"\"{str(obj)}\""

    if isinstance(obj, TYPES):
        if isinstance(obj, str):
            return '"' + obj.replace("\\", "\\\\").replace('"', "\"").replace("'", "\'") + '"'
        else:
            return str(obj)

    if isinstance(obj, list):
        return '[' + ', '.join([to_json(item) for item in obj]) + ']'

    if isinstance(obj, dict):
        return '{' + ', '.join([f'{to_json(key)}: {to_json(value)}'
                                    for key, value in obj.items()]) + '}'

def from_json(string: str):
    string = string.strip()

    if regex.fullmatch(Expression.INT.value, string):
        return int(string)

    if regex.fullmatch(Expression.STR.value, string):
        string = string.replace("\\\\", "\\").replace(r"\"", '"').replace(r"\'", "'")
        return string[1:-1]

    if regex.fullmatch(Expression.FLOAT.value, string):
        return float(string)

    if regex.fullmatch(Expression.BOOL.value, string):
        return True if string == 'True' else False

    if regex.fullmatch(Expression.NONE.value, string):
        return None

    if string.startswith("[") and string.endswith("]"):
        string = string[1:-1]
        matches = regex.findall(Expression.ANY_VALUE.value, string)
        return [from_json(match[0]) for match in matches]

    if string.startswith("{") and string.endswith("}"):
        string = string[1:-1]
        matches = regex.findall(Expression.ANY_VALUE.value, string)
        return {from_json(matches[i][0]): from_json(matches[i + 1][0])
                    for i in range(0, len(matches), 2)}
    # if data == '[]':
    #     return tuple()
    # elif data[0] == '[':
    #     data = data[1:len(data) - 1]
    #     parsed = []
    #     depth = 0
    #     quote = False
    #     substr = ""
    #     for i in data:
    #         if i == '[':
    #             depth += 1
    #         elif i == ']':
    #             depth -= 1
    #         elif i == '\"':
    #             quote = not quote
    #         elif i == ',' and not quote and depth == 0:
    #             parsed.append(from_json(substr))
    #             substr = ""
    #             continue
    #         elif i == ' ' and not quote:
    #             continue

    #         substr += i

    #     parsed.append(from_json(substr))
    #     return tuple(parsed)
    # else:
    #     return data[1:len(data) - 1]


# def from_json(string):
#     if string == '{}':
#         return frozendict()
#     elif string[0] == '{':
#         ans = dict()
#         string = string[1:len(string) - 1]
#         if re.match(ARRAY_IN_ARRAY_REGEX, string):
#             temp =""
#             flag = False
#             save_i = 0
#             ans_list = []
#             balance = 0
#             balance1 = 0
#             for i in range(8, len(string)):
#                 if string[i] == '[' and not flag:
#                     balance1 += 1
#                 elif string[i] == ']' and not flag:
#                     balance1 -= 1
#                 if string[i] == '[' and not flag and balance1 <= 2:
#                     continue
#                 elif string[i] == ']' and not flag and balance1 < 2:
#                     continue
#                 elif string[i] == '{' and not flag:
#                     balance += 1
#                 elif string[i] == '}' and not flag:
#                     balance -= 1
#                 elif string[i] == '\"':
#                     flag = not flag
#                 elif string[i] == ',' and not flag and balance == 0 and balance1 != 0:
#                     if temp != "" and temp != "[]":
#                         ans_list.append(from_json(temp))
#                     else:
#                         ans_list.append({})
#                     temp = ""
#                     continue
#                 elif string[i] == ' ' and not flag and balance == 0:
#                     continue
#                 elif string[i] == "," and not flag and balance1 == 0:
#                     if temp != "" and temp != "[]":
#                         ans_list.append(from_json(temp))
#                     else:
#                         ans_list.append({})
#                     save_i = i
#                     temp = ""
#                     break
#                 temp += string[i]  
#             ans[VALUE] = {}

#             ans_list = tuple(ans_list)

#             for i in range(0, len(ans_list), 2):

#                 ans[VALUE][ans_list[i]] = ans_list[i + 1]

#             temp = ""
#             for i in range(save_i + 11, len(string)):
#                 if string[i] =='\"':
#                     ans[TYPE] = temp
#                     temp = ""
#                     break
#                 else:
#                     temp += string[i]
#         elif re.match(ARRAY_REGEX, string):
#             temp = ""
#             flag = False
#             save_i = 0
#             ans_list = []
#             balance = 0
#             for i in range(10, len(string)):
#                 if string[i] == '{' and not flag:
#                     balance += 1
#                 elif string[i] == '}' and not flag:
#                     balance -= 1
#                 if string[i] == '\"':
#                     flag = not flag
#                 elif string[i] == ',' and not flag and balance == 0:
#                     ans_list.append(from_json(temp))
#                     temp = ""
#                     continue
#                 elif string[i] == ' ' and not flag and balance == 0:
#                     continue
#                 elif string[i] == "]" and not flag and balance == 0:
#                     if temp != "":
#                         ans_list.append(from_json(temp))
#                     save_i = i
#                     temp = ""
#                     break
#                 temp += string[i]
#             ans_list = tuple(ans_list)
#             ans[VALUE] = ans_list

#             for i in range(save_i + 12, len(string)):
#                 if string[i] == '\"':
#                     ans[TYPE] = temp
#                     temp = ""
#                     break
#                 else:
#                     temp += string[i]

#         elif re.match(VALUE_REGEX, string):
#             temp = ""
#             flag = False
#             save_i = 0
#             balance = 0
#             for i in range(9, len(string)):
#                 if string[i] == '{' and not flag:
#                     balance += 1
#                 elif string[i] == '}' and not flag:
#                     balance -= 1
#                 elif string[i] == '\"':
#                     flag = not flag
#                 elif string[i] == "," and not flag and balance == 0:
#                     if temp != "":
#                         ans[VALUE] = from_json(temp)
#                     save_i = i
#                     temp = ""
#                     break
#                 temp += string[i]
#             for i in range(save_i + 11, len(string)):
#                 if string[i] == '\"':
#                     ans[TYPE] = temp
#                     temp = ""
#                     break
#                 else:
#                     temp += string[i]

#         else:
#             temp = ""
#             flag = False
#             i = 10
#             while i < len(string):
#                 if string[i] == '\"' and not flag:
#                     ans[TYPE] = temp
#                     temp = ""
#                     flag = True
#                     i += 11
#                 elif string[i] == '\"' and flag:
#                     ans[TYPE] = temp
#                     temp = ""
#                     break
#                 else:
#                     temp += string[i]
#                 i += 1
#         return frozendict(ans)