def show_items(list, name):
    x = []
    for i in range(len(list)):
        if name == list[i][0]:
            x = list[i]
    y = ""
    for i in range(len(x)-1):
        if x[i] != name:
            y = x[i]+", "+y
    y += x[len(x)-1]
    if y == "":
        return "Item could not be found. Please enter a different item."
    else:
        return y