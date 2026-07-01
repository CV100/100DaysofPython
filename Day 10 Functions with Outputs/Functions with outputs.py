name = input("say name: ")
last_ = input("say last name: ")

def format_name(f_name, l_name):
    f_name = list(f_name)
    l_name = list(l_name)

    final_name = ""
    last_name = ""
    for n in f_name:
        if n == f_name[0]:
            final_name = n.upper()
        else:
            final_name += n


    for n in l_name:
        if n == l_name[0]:
            last_name = n.upper()
        else:
            last_name += n


    return final_name, last_name



print(format_name(name, last_))