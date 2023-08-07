letter_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def romanum_check(string):
    prev_value = 0
    for char in string:
        if char not in letter_dict:
            return False
        current_value = letter_dict[char]
        if current_value > prev_value != 0:
            if current_value in [5, 10] and prev_value in [1]:
                pass
            elif current_value in [50, 100] and prev_value in [10]:
                pass
            elif current_value in [500, 1000] and prev_value in [100]:
                pass
            else:
                return False
        prev_value = current_value

    if any(string.count(letter) > 3 for letter in ["C", "X", "I", ]):
        return False
    elif any(string.count(letter) > 1 for letter in ["D", "L", "V"]):
        return False
    else:  # D C C C X L V
        for i in range(len(string) - 1):
            if string[i] == "V" or string[i] == "L" or string[i] == "D":
                if letter_dict[string[i]] < letter_dict[string[i + 1]]:
                    return False
    return True


def convert_roman_to_arabic_int(string):
    if not romanum_check(string):
        return "Invalid Roman Number"
    else:
        pass
    positive = 0
    negative = 0
    arr = []
    for i in string:
        arr.append(letter_dict[i])
    print(arr)
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            negative += arr[i]
        elif arr[i] >= arr[i + 1]:
            positive += arr[i]

    positive += arr[-1]

    sonuc = positive - negative
    print(positive)
    print(negative)
    return sonuc


print(convert_roman_to_arabic_int("XCCXXV"))
