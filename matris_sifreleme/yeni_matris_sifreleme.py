import numpy as np

translater = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
    'a': 27,
    'b': 28,
    'c': 29,
    'd': 30,
    'e': 31,
    'f': 32,
    'g': 33,
    'h': 34,
    'i': 35,
    'j': 36,
    'k': 37,
    'l': 38,
    'm': 39,
    'n': 40,
    'o': 41,
    'p': 42,
    'q': 43,
    'r': 44,
    's': 45,
    't': 46,
    'u': 47,
    'v': 48,
    'w': 49,
    'x': 50,
    'y': 51,
    'z': 52,
    '\n': 53,
    '.': 54,
    ',': 55,
    '+': 56,
    '-': 57,
    '!': 58,
    '/': 59,
    '[': 60,
    ']': 61,
    '(': 62,
    ')': 63,
    '=': 64,
    '?': 65,
    '_': 66,
    '&': 67,
    '%': 68,
    '*': 69,
    ';': 70,
    ':': 71,
    '@': 72,
    ' ': 73,
    '#': 74,
    '$': 75,
    '|': 76,
    '^': 77,
    '{': 78,
    '}': 79,
    '"': 80,
    "'": 81,
    'ß': 82,
    '€': 83,
    '~': 84,
    'æ': 85,
    'Æ': 86,
    '₺': 87,
    '¨': 88,
    '`': 89,
    'ş': 90,
    'Ş': 91,
    'ö': 92,
    'Ö': 93,
    'ğ': 94,
    'Ğ': 95,
    'ü': 96,
    'Ü': 97,
    'Ç': 98,
    'ç': 99,
    'İ': 100,
    'ı': 101,
    '0': 200,
    '1': 201,
    '2': 202,
    '3': 203,
    '4': 204,
    '5': 205,
    '6': 206,
    '7': 207,
    '8': 208,
    '9': 209,
}


def matrix(text):   #asıl metin'i matrise çeviren fonksiyon
    sol = []
    sag = []

    if text.__len__() % 2 != 0:
        text = text + ' '
    bol = len(text) // 2
    for i in range(0, bol):
        sol.append(translater['{}'.format(text[i])])
    for j in range(bol, len(text)):
        sag.append(translater['{}'.format(text[j])])

    array = np.array([sol, sag])

    print("\n{}\n".format(text))
    print("\nSifrelenmeden önce \n", array)

    return array


def txttomatris():       #sifreli mesajı numpy matrisine çeviren fonksiyon
    with open("sifrelimetin.txt", "r+", encoding="utf-8") as file:
        c = file.read()
        c = c.replace("\n", ",")
        c = c.split(",")
        c.pop()
        c = list(map(int,c))
        bol = (len(c)+1) // 2
        sol = list(map(int, c[0:bol]))
        sag = list(map(int, c[bol:len(c)]))
        array = np.array([sol, sag])
        return array


def encrypt(array):     #sifrenin alındığı ve matris işlemlerinin yapıldığı fonksiyon
    sifre = input("4 haneli Şifrenizi giriniz: ")

    sol = list(map(int, sifre[0:2]))
    sag = list(map(int, sifre[2:4]))

    passarr = np.array([sol, sag])

    array = np.matmul(passarr, array)
    print("Sifrelendikten sonra \n", array)

    for i in range(len(array[:])):
        for j in range(len(array[0, :])):
            array[i][j] = round(array[i][j])

    np.savetxt('sifrelimetin.txt', array, delimiter=',', fmt='%d')

    return array

def decrypt():      #şifrenin alındığı ve matris işlemlerinin yapıldığı fonksiyon
    sifre = input("Dosyayı açmak için şifrenizi giriniz: ")
    sol = list(map(int, sifre[0:2]))
    sag = list(map(int, sifre[2:4]))
    array = txttomatris()
    passarr = np.array([sol, sag])
    passarr = np.linalg.inv(passarr)
    array = np.matmul(passarr, array)
    print("\n{}".format(array))
    text = ""
    for i in range(len(array[:])):
        for j in range(len(array[0, :])):
            new = array[i][j]
            new = round(new)
            for x, y in translater.items():
                if y == new:
                    text = text + x
    with open("sifresicozulmusmetin.txt","w",encoding="utf-8") as file:
        file.write(text)
    return array

def kriptet():    #son kripte etme fonksiyonu
    with open("asilmetin.txt", "r+", encoding="utf-8") as file:
        icerik = file.read()
        txt = matrix(icerik)
        encrypt(txt)


kriptet()
decrypt()