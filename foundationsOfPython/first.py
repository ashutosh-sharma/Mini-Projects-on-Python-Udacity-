import webbrowser
import time
t=3;

while(t>0):
    print("This is current time:"+time.ctime())
    time.sleep(2)
    webbrowser.open("www.youtube.com")
    t=t-1
