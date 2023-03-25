dnaExample1 = "GCCGAAATTAGCGTAGT"

def dnaReplication(n):
    result = ""
    for i in n:
        if i == "A":
            result+="T"
        elif i == "T":
            result+="A"
        elif i == "G":
            result+="C"
        elif i =="C":
            result+="G"
    return result

print(dnaReplication(dnaExample1))