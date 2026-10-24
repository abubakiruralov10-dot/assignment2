def first_tool_position(tools, wanted):
    for i in range(len(tools)):
        if tools[i] == wanted:
            return i
    return -1

def all_tool_places(tools, wanted):
    target = []
    for a in range(len(tools)):
        if tools[a] == wanted:
            target.append(a)
          
    return target

    
tools = ["hammer", "drill", "saw", "drill", "wrench"]

for name in ["drill", "tape"]:
    fp = first_tool_position(tools, name)
    ap = all_tool_places(tools,name)
    print(f"{name}: first position = {fp}, all positions = {ap}")