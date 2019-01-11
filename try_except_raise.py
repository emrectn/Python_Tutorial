'''
    throws exception
'''


def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen string gönderin.")
    else:
        return s[::-1]


try:
    print(terscevir("ABCD"))
    print(terscevir(123123))
except ValueError as error:
    print("Hata Verdi : ", error)