def is_palindrome(text: str):
    if not text:
        return False

    text = remove_empty_spaces(text)
    reverse_text = reverse(text)

    return reverse_text.lower() == text.lower()


def remove_empty_spaces(text: str) -> str:
    return text.replace(" ", "")


def reverse(text: str):
    reverse_text = ""
    for i in range(len(text) - 1, -1, -1):
        reverse_text += text[i]
    return reverse_text

print("Amo la paloma", is_palindrome("Amo la paloma"))
print("Civic", is_palindrome("civic"))
print("Reconocer", is_palindrome("Reconocer"))