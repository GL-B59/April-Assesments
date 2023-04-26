def c_f_pin(user_input):
    a = user_input
    b = a.find("pin")
    print(b)
    output = a[b:b + len("pin")]
    return output
