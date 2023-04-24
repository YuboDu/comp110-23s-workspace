def short_words(input1: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    output: list[str] = []
    for item in input1:
        if len(item) >= 5:
            print(f"{item} is too long!")
        if len(item) < 5:
            output.append(item)
    return output
