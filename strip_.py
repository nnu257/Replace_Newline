inp_list = []

inp = input("input string with newline：\n")
while inp != "":
    inp_list.append(inp)
    inp = input("input string with newline：\n")

inp_list = [inp.strip() for inp in inp_list]

outp = " ".join(inp_list)

print(outp)