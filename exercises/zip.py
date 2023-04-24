"""Challenge Question 04 - Dict Function Writing"""

def zip(input1: list[str], input2: list[int]) -> dict[str,int]:
    dictionary: dict[str,int] = {}
    if len(input1) != len(input2):
        return dictionary
    for idx in range(0,len(input1)):
        dictionary[input1[idx]] = input2[idx]
    return dictionary