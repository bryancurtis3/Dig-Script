
#file = str(input("file: "))
file = "answers.txt"
f = open(file, "r")

line = f.read()
line = line.split("\n")


length = len(line)
n = 0
i = 0
y = 0
x = 0
tabs = 0

# For as many times as there are domains...

for n in range(length-1):
    domain = []
    ip = []

    # Extracts domain line by line
    while line[n][i] != "\t":
        domain += line[n][i]
        i += 1

    # Extracts IP line by line
    for x in range(len(line[n])):
        y = x + 2

        if line[n][x] == 'A':
            while y < len(line[n]):
                ip += line[n][y]
                y += 1

    # Prints domain with matching IP
    domain = "".join(domain)
    domain = domain.lower()
    print(domain, end = "\t")

    ip = "".join(ip)
    print(ip)

    n += 1
    i = 0
