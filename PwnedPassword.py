from urllib.request import Request, urlopen
import hashlib

def hashpassword(plaintext_password):
    sha1 = hashlib.sha1(plaintext_password.encode())
    return(sha1.hexdigest())


def check_password(plaintext_password):
    validhash = hashpassword(plaintext_password).upper()
    url = "https://api.pwnedpasswords.com/range/" + validhash[:5]
    req = Request(url, headers= {'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    htmlstr = html.decode("utf8")
    hashes = htmlstr
    listhash = hashes.splitlines()
    for x in listhash:
        PwnedHash = validhash[:5] + x
        if validhash in PwnedHash:
            return(True)
    return(False)
if __name__ == "__main__":
    password = input("Please Enter Password To Test \n")
    if check_password(password) == True:
        print("Password was found in Troy Hunt's PwnedPassword Service")
    else:
        print("Password not found in Troy Hunt's Pwned Password Service")
