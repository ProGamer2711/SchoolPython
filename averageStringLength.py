strings = [
    "Hello, World!",
    "This is a test string",
    "Lorem ipsum dolor sit amet"
]

averageLength = 0

for string in strings:
    averageLength += len(string)

averageLength /= len(strings)

print(f"Average length of strings: {round(averageLength)}")
