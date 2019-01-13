from urllib.request import Request, urlopen
import hashlib
class PwnedPassword:
    def __init__(self, ptp):
        self.plaintext_password = ptp
        self.answer = self.check_password()
    def hashpassword(self):
        sha1 = hashlib.sha1(self.plaintext_password.encode())
        return(sha1.hexdigest())
    def check_password(self):
        validhash = self.hashpassword().upper()
        url = "https://api.pwnedpasswords.com/range/" + validhash[:5]
        req = Request(url, headers= {'User-Agent': 'Mozilla/5.0'})
        hashes = urlopen(req).read().decode("utf8")
        if validhash[5:] in hashes:
            return True
        else:
            return False
if __name__ == "__main__":
    password = input("Please Enter Password To Test \n")
    if PwnedPassword(password).answer == True:
        print("Password was found in Troy Hunt's PwnedPassword Service")
    else:
        print("Password not found in Troy Hunt's Pwned Password Service")