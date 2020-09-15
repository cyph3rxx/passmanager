def list():
    f=open("userinfo.txt")
    f.seek(0)
    print(f.read())
