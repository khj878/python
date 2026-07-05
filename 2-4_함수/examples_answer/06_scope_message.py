message = "덧셈 결과: "


def add_with_message(a, b):
    result = a + b
    return message + str(result)


output = add_with_message(10, 20)
print(output)
