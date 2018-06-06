import sys
files=sys.argv[1:]
#file_name=files[0]
length=len(sys.argv)
i=0
try:
    for j in files:
        if j.find('cr-')>=0:
            #creating a new file
            fname=j.replace('cr-',"")
            f=open(fname,'w')
            while(True):
                data=input()
                f.write(data+"\n")

        else:
            #opening a file to display its file_content
            while i<length-1:
                f=open(files[i],'r')
                file_content=f.read()
                sys.stdout.write(file_content)
                f.close()
                i=i+1

except FileNotFoundError:
    print("File not found")
except:
    print("")
