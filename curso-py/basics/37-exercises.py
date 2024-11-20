from typing import Dict, List, Tuple

string = "Hello World"

def remove_empty_spaces(text: str) -> List :
    # sanitized = ""
    # for char in text:
    #     if char != " ":
    #         sanitized += char
    # return sanitized
    
    # Teacher solution
    return [char for char in text if char != " "]

def count_duplicates(list: List) -> Dict[str, int] :
    duplicated: Dict[str, int] = {}
    for char in list:
        if char in duplicated:
            duplicated[char] += 1
        else:
            duplicated[char] = 1    
    return duplicated

def sort_dict(dictionary: Dict[str, int]) -> List[Tuple[str, int]]:
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

def greater(sorted_elements: List) -> Dict[str, int]:
    maximum = sorted_elements[0][1]
    dictionary = {}
    for item in sorted_elements:
        if maximum > item[1]:
            break
        dictionary[item[0]] = item[1]
    return dictionary

def create_message(dictionary: Dict[str, int]) -> str:
    message = "The most repeated are: \n"
    for key, value in dictionary.items():
        message += f"- {key} with {value} repetitions \n"
    return message

sanitized_text = remove_empty_spaces(string)
duplicates = count_duplicates(sanitized_text)
sorted_duplicates = sort_dict(duplicates)
greater_values = greater(sorted_duplicates)
formed_message = create_message(greater_values)
print(sanitized_text)
print(duplicates)
print(greater_values)
print(formed_message)
