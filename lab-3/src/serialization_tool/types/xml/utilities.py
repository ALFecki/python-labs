def to_xml(obj):
    if type(obj) == tuple:
        serialized = ""
        for i in obj:
            serialized += (f"<{type(i).__name__}>{to_xml(i)}<{type(i).__name__}/>\n")
        return f"<{serialized}>"
    else:
        return f"{str(obj)}"