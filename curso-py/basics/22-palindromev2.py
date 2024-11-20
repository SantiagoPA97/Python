def remove_empty_spaces(text: str):
    return text.replace(" ", "")


def is_palindrome(text: str):
    text = remove_empty_spaces(text)
    reverse_text = text[::-1]
    return text.lower() == reverse_text.lower()


is_palindrome("Amo la paloma")

print("Hola mundo", is_palindrome("Hola mundo"))
