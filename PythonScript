#file = str(input("file: "))
file = "answers.txt"
f = open(file, "r")

line = f.read()
line = line.split("\n")

length = len(line)
n = 0
i = 0
#p = 0

print(length)

for n in range(length):
    domain = []

    while line[n][i] != "\t":
        domain += line[n][i]
        i += 1

    domain = "".join(domain)
    print(domain)
    n += 1
    i = 0

"""
    if line[n].contains(domain):
        print(domain)
    else:
"""
