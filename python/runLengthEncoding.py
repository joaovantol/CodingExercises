def run_length_encode(data):
    if not data:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            if count == 1:
                encoded.append(data[i - 1])
            else:
                encoded.append(f"{count}{data[i - 1]}")
            count = 1

    # handle the last run
    if count == 1:
        encoded.append(data[-1])
    else:
        encoded.append(f"{count}{data[-1]}")

    return ''.join(encoded)

import re

def run_length_decode(data):
    decoded = []
    # Find all (optional number)(letter/whitespace) groups
    parts = re.findall(r'(\d*)([A-Za-z\s])', data)

    for count, char in parts:
        repeat = int(count) if count else 1
        decoded.append(char * repeat)

    return ''.join(decoded)

original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
encoded = run_length_encode(original)
decoded = run_length_decode(encoded)

print("Original:", original)
print("Encoded :", encoded)
print("Decoded :", decoded)