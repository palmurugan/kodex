def kebab_to_pascal_case(s: str) -> str:
    # Split the string by hyphens, capitalize each part, and join them together
    return ''.join(word.capitalize() for word in s.split('-'))
