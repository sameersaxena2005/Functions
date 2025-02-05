# File Reading Generator:
def read_lines(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line.strip()

for line in read_lines("sample.txt"):
    print(line)

