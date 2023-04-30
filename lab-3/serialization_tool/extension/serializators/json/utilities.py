from frozendict import frozendict
from .constants import VALUE, TYPE, ARRAY_IN_ARRAY_REGEX, ARRAY_REGEX, VALUE_REGEX
import re


def to_json(obj):
    ans = ""
    ans_list = []
    flag = False
    if type(obj) == frozendict or type(obj) == dict:
        for key, value in obj.items():
            if key == VALUE or key == TYPE:
                ans_list.append("" + to_json(key) + ": " + to_json(value) + "")
                flag = True
            else:
                ans_list.append("[" + to_json(key) + ", " + to_json(value) + "]")
                flag = False
        ans += ", ".join(ans_list)
        if flag:
            ans = "{" + ans + "}"
        else:
            ans = "[" + ans + "]"
        return f"{ans}"
    elif type(obj) == tuple:
        serialized = []
        for i in obj:
            serialized.append(f"{to_json(i)}")
        ans = ", ".join(serialized)
        return f"[{ans}]"
    else:
        return f"\"{str(obj)}\""



def from_json(str):
    if str == "{}":
        return frozendict()
    elif str[0] == '{':
        ans = dict()
        string = str[1:len(str) - 1]
        if re.match(ARRAY_IN_ARRAY_REGEX, string):
            temp =""
            flag = False
            save_i = 0
            ans_list = []
            balance = 0
            balance1 = 0
            for i in range(8, len(string)):
                if string[i] == '[' and not flag:
                    balance1 += 1
                elif string[i] == ']' and not flag:
                    balance1 -= 1
                if string[i] == '[' and not flag and balance1 <= 2:
                    continue
                elif string[i] == ']' and not flag and balance1 < 2:
                    continue
                elif string[i] == '{' and not flag:
                    balance += 1
                elif string[i] == '}' and not flag:
                    balance -= 1
                elif string[i] == '\"':
                    flag = not flag
                elif string[i] == ',' and not flag and balance == 0 and balance1 != 0:
                    if temp != "" and temp != "[]":
                        ans_list.append(from_json(temp))
                    else:
                        ans_list.append({})
                    temp = ""
                    continue
                elif string[i] == ' ' and not flag and balance == 0:
                    continue
                elif string[i] == "," and not flag and balance1 == 0:
                    if temp != "" and temp != "[]":
                        ans_list.append(from_json(temp))
                    else:
                        ans_list.append({})
                    save_i = i
                    temp = ""
                    break
                temp += string[i]  
            ans[VALUE] = {}

            ans_list = tuple(ans_list)

            for i in range(0, len(ans_list), 2):
                ans[VALUE][ans_list[i]] = ans_list[i + 1]
            temp = ""
            for i in range(save_i + 11, len(string)):
                if string[i] =='\"':
                    ans[TYPE] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]
        elif re.match(ARRAY_REGEX, string):
            temp = ""
            flag = False
            save_i = 0
            ans_list = []
            balance = 0
            for i in range(10, len(string)):
                if string[i] == '{' and not flag:
                    balance += 1
                elif string[i] == '}' and not flag:
                    balance -= 1
                if string[i] == '\"':
                    flag = not flag
                elif string[i] == ',' and not flag and balance == 0:
                    ans_list.append(from_json(temp))
                    temp = ""
                    continue
                elif string[i] == ' ' and not flag and balance == 0:
                    continue
                elif string[i] == "]" and not flag and balance == 0:
                    if temp != "":
                        ans_list.append(from_json(temp))
                    save_i = i
                    temp = ""
                    break
                temp += string[i]
            ans_list = tuple(ans_list)
            ans[VALUE] = ans_list

            for i in range(save_i + 12, len(string)):
                if string[i] == '\"':
                    ans[TYPE] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]

        elif re.match(VALUE_REGEX, string):
            temp = ""
            flag = False
            save_i = 0
            balance = 0
            for i in range(9, len(string)):
                if string[i] == '{' and not flag:
                    balance += 1
                elif string[i] == '}' and not flag:
                    balance -= 1
                elif string[i] == '\"':
                    flag = not flag
                elif string[i] == "," and not flag and balance == 0:
                    if temp != "":
                        ans[VALUE] = from_json(temp)
                    save_i = i
                    temp = ""
                    break
                temp += string[i]
            for i in range(save_i + 11, len(string)):
                if string[i] == '\"':
                    ans[TYPE] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]

        else:
            temp = ""
            flag = False
            i = 10
            while i < len(string):
                if string[i] == '\"' and not flag:
                    ans[TYPE] = temp
                    temp = ""
                    flag = True
                    i += 11
                elif string[i] == '\"' and flag:
                    ans[TYPE] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]
                i += 1
            return frozendict(ans)