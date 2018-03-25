import os,shutil,subprocess
#show all screen shot on my desktop
#create new file for screenShot
#print file_list
###############

home = os.getenv("HOME")
path = home +"/Desktop"
file_list = os.listdir(path)
def creatFolder():
    newDirctor = r'/Users/al_heji/documents/screenShot'
    if not os.path.exists(newDirctor):
        os.makedirs(newDirctor)
        print "new dirctory mack..."
    else:
        print "dirctory befor exists"
def moveScreenShotToFoledr():
    index = 0
    creatFolder()
    for file_name in file_list:
        if file_name.find("Screen Shot") == 0 and file_name.endswith(".png"):
            path2 = home +"/documents/screenShot/"
            print "path ====>"+path2
            #if not os.path.exists(path2):
            shutil.move(path +"/"+ file_name,path2)
            #subprocess.Popen("mv" + " " + path + " " + path2,shell=True)
            index +=1
            print " \033[1"
            print str(index) +" " " files is move to folder"
            print "\033[0m"
            print file_name
moveScreenShotToFoledr()
