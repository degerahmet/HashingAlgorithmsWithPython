"""

Caesar Cipher Encrypt & Decrypt Algorithm


ABCDEFGHIJKLMNOPRSTUVWXYZ
XYZABCDEFGHIJKLMNOPRSTUVW



"""

def ceaser_encrypt(text):
    upper_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T",
                      "U","V","W","X","Y","Z"]
    text = text.upper()
    new=[]
    encrypt = ""

    for i in range(len(upper_alphabet)-1,len(upper_alphabet)-4,-1):
        new.append(upper_alphabet[i])

    for j in range(0,len(upper_alphabet)-3):
        new.append(upper_alphabet[j])

    for x in range(len(text)):
        if text[x] == " ":
            encrypt = encrypt + " "
        elif text[x] == "\n" :
            encrypt = encrypt + "\n"
        else :
            for y in range(len(upper_alphabet)):
                if text[x] == upper_alphabet[y]:
                    encrypt = encrypt + new[y]

    return encrypt

def ceaser_decryp(text):
    upper_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T",
                      "U", "V", "W", "X", "Y", "Z"]
    text = text.upper()
    new = []
    decryp = ""
    for i in range(len(upper_alphabet) - 1, len(upper_alphabet) - 4, -1):
        new.append(upper_alphabet[i])
    for j in range(0, len(upper_alphabet) - 3):
        new.append(upper_alphabet[j])

    for x in range(len(text)):
        if text[x] == " ":
            decryp = decryp + " "
        elif text[x] == "\n":
            decryp = decryp + "\n"
        else:
            for y in range(len(upper_alphabet)):
                if text[x] == new[y]:
                    decryp = decryp + upper_alphabet[y]

    return decryp

with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    lines_ex = file.readlines()
    lastline=lines_ex[-1]
    file.close()
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    icerik = file.read()

    if lastline == "sifre acik\n" or "SIFRE ACIK\n":
        enc = ceaser_encrypt(icerik)
        file.seek(0)
        file.write(enc)
        print("Mesajınız şifrelenmiştir!")
    elif lastline == "OFCNB ZXFH\n":
        dec = ceaser_decryp(icerik)
        file.seek(0)
        file.write(dec)
        print("Mesajınızın şifresi çözülmüştür!")
    else :
        print("Şifreleme durumu belirtilmedi ! Şifrelemek istediğiniz içeriğinizin son satırına\nsifre acik\nyaziniz !")

    file.close()








