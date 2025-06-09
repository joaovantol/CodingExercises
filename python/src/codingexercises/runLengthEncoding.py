import re

def runLengthEncoding(string):
    string = string.replace(" ","")

    encoded = []
    count = 1

    for i in range(0, len(string)-1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            if count == 1:
                encoded.append(string[i])
            else:
                encoded.append(f"{count}{string[i]}")
            count = 1

    if count == 1:
        encoded.append(string[-1])
    else:
        encoded.append(f"{count}{string[-1]}")

    return "".join(encoded)

def runLengthDecoding(string):
    decoded = []

    parts = re.findall(r"(\d*)([A-Za-z])", string)

    for count, char in parts:
        repeat = int(count) if count else 1
        decoded.append(char * repeat)

    return "".join(decoded)


runLengthEncoding("AABCCCDEEEE")
runLengthDecoding(runLengthEncoding("AABCCCDEEEE"))

runLengthEncoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
runLengthDecoding(runLengthEncoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))
