import os
def Rfile():
    Flist=os.listdir(r"C:\Users\ashu-PC\Downloads\Compressed\prank\prank")
    os.chdir(r"C:\Users\ashu-PC\Downloads\Compressed\prank\prank");
    temp_file="elhi.jpg";
    temp="bangalore.jpg"
    os.rename(temp,temp_file)
      
Rfile()
 
