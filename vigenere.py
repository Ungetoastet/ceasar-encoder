import string, math
letters = string.ascii_uppercase
vocals = ["E", "I", "A", "U", "O"]
rarecons = ["Q", "X", "Y", "J", "V"]
text = "BYURUHZKBYQDXUKJUMQHUYDRUIEDTUHUHJQWVKUHCYSXMUYBYSXUYDUVQXHIJKDTURUYCZKUHWUDXQJJU" # HIER GEGEBENEN TEXT IN GROSSBUCHSTABEN ANGEBEN
decrkey = "L" # HIER SCHLÜSSEL ANGEBEN
encrypt =  True # ENT ODER VERSCHLÜSSELN
bruteforce = True
bruteres = []

def crypt(ori, key, enc):
    msg = ""
    for i in range(len(ori)):
        n1 = letters.index(ori[i])
        n2 = letters.index(key[i%len(key)])
        if (enc):
            n3 = n1+n2
        else:
            n3 = n1-n2
        msg += letters[n3%len(letters)]
    return msg
    
if (not bruteforce):
    print(crypt(text, decrkey, encrypt))

else:
    for key in letters:
        decr = crypt(text, key, False)
        prob = 0
        for i in range(len(decr)): # VOKALE UND SELTENE BUCHSTABEN ZÄHLEN
            s = decr[i]
            for v in range(len(vocals)):
                if s == vocals[v]:
                    prob += 20-v
                if s == rarecons[v]:
                    prob -= 10-v
                
        # LANGE KONSONANTENKETTEN FINDEN
        chainlen = 0
        for i in range(len(decr)):
            s = decr[i]
            if s in vocals:
                prob -= chainlen * 2
                chainlen = 0
            else:
                chainlen += 1
        # PROB FORMATIEREN
        prob = str(max(prob, 0))
        if len(prob) == 1:
            prob = "00" + prob
        if len(prob) == 2:
            prob = "0" + prob
        bruteres.append("[" + str(prob) + "]-[" + key + "] " + decr)
    
    bruteres.sort()
    bruteres = bruteres[::-1]
    for res in bruteres:
        print(res)

    