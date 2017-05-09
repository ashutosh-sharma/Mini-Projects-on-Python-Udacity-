import os
def Rfile():
    Flist=os.listdir(r"C:\Users\ashu-PC\Downloads\Compressed\prank\prank")
    os.chdir(r"C:\Users\ashu-PC\Downloads\Compressed\prank\prank");

    for temp_file in Flist:
        os.rename(temp_file,temp_file.translate(None,"0123456789"))
        print(temp_file+" changed to "+temp_file.translate(None,"0123456789"))

Rfile()
 
