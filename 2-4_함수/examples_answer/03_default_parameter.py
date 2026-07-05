def make_welcome_message(name="고객"):
    return f"안녕하세요, {name}님!"


default_message = make_welcome_message()
Julie_message = make_welcome_message("Julie")

print(default_message)
print(Julie_message)
