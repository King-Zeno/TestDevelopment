have_girl = False

def send():
    print("发女朋友了..")
    global have_girl
    have_girl = True
    print(f"have_girl = {have_girl}")

def show():
    if have_girl == True:
        print("有女朋友， 好开心~")
    else:
        print("单身贵族 *_*")
