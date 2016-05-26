

import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()

c.execute('''CREATE TABLE ip(Domain TEXT, IP TEXT)''')
#c.execute("INSERT INTO ip VALUES(?, ?)", (a, b))

c.execute('''CREATE TABLE mx(Domain TEXT, MX TEXT)''')
#c.execute("INSERT INTO mx VALUES(?, ?)", (c, d))




#file = str(input("file: "))
file = "answers.txt"
f = open(file, "r")

line = f.read()
lineA = line.split("\n")

file = "mailexchange.txt"
f = open(file, "r")

line = f.read()
lineMX = line.split("\n")


lengthA = len(lineA)
lengthMX = len(lineMX)
n = 0
i = 0
q = 0
y = 0
t = 0

# For as many times as there are lines...

for n in range(lengthA - 1):
    domainA = []
    ip = []

    # Extracts domain line by line
    while lineA[n][i] != "\t":
        domainA += lineA[n][i]
        i += 1

    # Extracts IP's
    for x in range(len(lineA[n])):
        y = x + 2

        if lineA[n][x] == 'A':
            while y < len(lineA[n]):
                ip += lineA[n][y]
                y += 1



    # Prints domain with matching IP
    domainA = "".join(domainA)
    domainA = domainA.lower()
    print(domainA, end = "\t\t")

    ip = "".join(ip)
    print(ip)
    i = 0




    c.execute("INSERT INTO ip VALUES(?, ?)", (domainA, ip))



#####################################################
#####################################################

# Switch from domains with IP's to domains with XP's

#####################################################
#####################################################

print("\n\n")


for m in range(lengthMX - 1):
    domainMX = []
    mx = []

    # Extracts domain line by line
    while lineMX[m][q] != "\t":
        domainMX += lineMX[m][q]
        q += 1

    # Extracts MX's
    for r in range(len(lineMX[m])):
        t = r + 1
        #print(lineMX[m][t])

        if lineMX[m][r] == "X":
            while t < len(lineMX[m]):
                mx += lineMX[m][t]
                t += 1


    # Prints domain with matching MX
    domainMX = "".join(domainMX)
    domainMX = domainMX.lower()
    print(domainMX, end = "\t")

    mx = "".join(mx)
    print(mx)
    q = 0




    c.execute("INSERT INTO mx VALUES(?, ?)", (domainMX, mx))

conn.commit()
