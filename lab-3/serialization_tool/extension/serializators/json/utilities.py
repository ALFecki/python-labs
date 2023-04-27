from frozendict import frozendict
from constants import VALUE, TYPE

def to_json(obj):
    ans = ""
    ans_list = []
    float
    if type(obj) == frozendict or type(obj) == dict:
        for key, value in obj.items():
            if key == VALUE or key == TYPE:
                ans_list.append("" + to_json(obj) + ": " + to_json(value) + "")
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
    pass