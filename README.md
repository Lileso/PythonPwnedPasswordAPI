# PythonPwnedPasswordAPI
Definition you can call to test if a password is in Troy Hunt's Pwned Password API

The way that I wrote this was so I can pass a password from another script and it will test it via Troy's API

eg: 

```
import PwnedPassword
password = "Password"
check = PwnedPassword.check_password(password)
if check = "PwnedPassword":
  print("Password is pwned")
elif check = "Fine":
  print("Password isn't pwned")
```
You can also run it stand alone in which case it will ask you to enter a password do a check and print out the result

