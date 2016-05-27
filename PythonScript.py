

import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS ip(Domain TEXT, IP TEXT, pastIP TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS mx(Domain TEXT, MX TEXT, pastMX TEXT)''')


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
lastIP = 'N/A'
lastMX = 'N/A'

same = 0
ipList = []
mxList = []




# For as many times as there are lines...

for n in range(lengthA - 1):


    #domainA2 = domainA


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
    ipList.append(ip)
    i = 0


    #c.execute("INSERT INTO ip VALUES(?, ?, ?)", (domainA, ip, lastIP))


##########################################################
##########################################################
##                                                      ##
##  Switch from domains with IP's to domains with MX's  ##
##                                                      ##
##########################################################
##########################################################

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
    mxList.append(mx)
    q = 0



    #c.execute("INSERT INTO mx VALUES(?, ?, ?)", (domainMX, mx, lastMX))

conn.commit()

###########################################################
###########################################################
##                                                       ##
##  Switch from gathering current data to comparing all  ##
##                                                       ##
###########################################################
###########################################################

c.execute("SELECT * FROM ip")

rows = c.fetchall()

domainNum = 0
domainLow = 0

rowTotal = 0
pool = False

# Sudo variable for rowTotal determination
for bow in rows:
    rowTotal += 1


listed = []

rowNum = 0

# Querys stored IP's
for row in rows:
    rowNum += 1


    if rowNum == rowTotal:
        rowNum = rowTotal - 1
        pool = True

    # Slowly forms a complete list using queries to database
    listed.append(row[1])


    if rows[rowNum-1][0] == rows[rowNum][0] and rowNum != rowTotal - 1:
        domainNum += 1
    else:
        domainNum += 1

        if pool == True:
           rowNum = rowTotal



        # Check each location in new list against each location wiht cooresponding domain in stored data
        for k in range(domainLow, domainNum):
            change = 1
            for j in range(domainLow, domainNum):

                if ipList[k] == listed[j]:
                    same += 1
                    change = 0
                    break

            # Informs the user if there is a change and updates database to show change
            if change == 1:
                print(rows[k][0], "\t", rows[k][1])
                c.execute("UPDATE ip SET pastIP = ? WHERE ip = ?", (listed[k], rows[k][1]))
                c.execute("UPDATE ip SET ip = ? WHERE ip = ?", (ipList[k], rows[k][1]))
                conn.commit()

        domainLow = domainNum

different = 0
different = rowTotal - same
print("There have been", different, "IP address changes.")



#---------------------------------Change-from-ip-to-mx---------------------------------------

same = 0

c.execute("SELECT * FROM mx")

rows = c.fetchall()

domainNum = 0
domainLow = 0

rowTotal = 0
pool = False

for bow in rows:
    rowTotal += 1


listed = []

rowNum = 0

for row in rows:
    rowNum += 1


    if rowNum == rowTotal:
        rowNum = rowTotal - 1
        pool = True


    listed.append(row[1])


    if rows[rowNum-1][0] == rows[rowNum][0] and rowNum != rowTotal - 1:
        domainNum += 1
    else:
        domainNum += 1

        if pool == True:
           rowNum = rowTotal


        for k in range(domainLow, domainNum):
            change = 1
            for j in range(domainLow, domainNum):

                if mxList[k] == listed[j]:
                    same += 1
                    change = 0
                    break

            if change == 1:
                print(rows[k][0], "\t", rows[k][1])
                c.execute("UPDATE mx SET pastMX = ? WHERE mx = ?", (mxList[k], rows[k][1]))
                c.execute("UPDATE mx SET mx = ? WHERE mx = ?", (mxList[k], rows[k][1]))
                conn.commit()

        domainLow = domainNum

different = 0
different = rowTotal - same
print("There have been", different, "MX address changes.")
