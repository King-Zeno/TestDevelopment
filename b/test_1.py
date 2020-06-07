import os

print(os.path.exists(""))
if not os.path.exists(""):
    os.mkdir("")
if not os.path.exists(("b/test.txt")):
    f = open("test.txt", "w")
    f.write("hello, os using")
    f.close()