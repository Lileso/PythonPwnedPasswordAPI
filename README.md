# PythonPwnedPasswordAPI
Definition you can call to test if a password is in Troy Hunt's Pwned Password API

The way that I wrote this was so I can pass a password from another script and it will test it via Troy's API

eg: 
(Make sure that my PwnedPassword.py script is in the same directory as your script)
```
from PwnedPassword import PwnedPassword
if PwnedPassword("ExamplePassword").answer == True:
  print("Password is pwned")
```
You can also run it stand alone in which case it will ask you to enter a password do a check and print out the result

