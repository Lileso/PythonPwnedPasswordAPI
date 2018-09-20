from urllib.request import Request, urlopen
import hashlib

def hashpassword(plaintext_password):
    sha1 = hashlib.sha1(plaintext_password.encode())
    return(sha1.hexdigest())


def check_password(plaintext_password):
    plaintext_password = plaintext_password
    password = hashpassword(plaintext_password)
    hashedpassword = password.upper()
    validhash = hashedpassword[:5]
    pwnedpasswordapi = "https://api.pwnedpasswords.com/range/"
    url = pwnedpasswordapi + validhash
    req = Request(url, headers= {'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    htmlstr = html.decode("utf8")
    hashes = htmlstr
    listhash = hashes.splitlines()
    for x in listhash:
        PwnedHash = validhash + x
        if hashedpassword in PwnedHash:
            print("Password was found in Troy Hunt's PwnedPassword Service")
            return("PwnedPassword")
    print("Password not found in Troy Hunt's Pwned Password Service")
    return("Fine")

password = input("Please Enter Password To Test \n")
check_password(password)