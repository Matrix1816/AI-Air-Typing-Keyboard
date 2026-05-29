typed_text = ""


def update_text(key):

    global typed_text

    if key == "SPACE":
        typed_text += " "

    elif key == "BACK":
        typed_text = typed_text[:-1]

    else:
        typed_text += key


def get_text():
    return typed_text