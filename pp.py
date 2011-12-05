                 
#!/usr/bin/python

from os import system

def showoptions():
    print("SYSTEM ADMIN PANEL 3.0")
    print("BACK UP EVERYTHING BEFORE YOU LOSE EVERYTHING! ")
    print("RUN SCRIPT AS ROOT ")
    print("")
    print("1  - Quit\t\t2  - Show disk info")
    print("3  - List Dir\t\t4  - Delete a file")
    print("5  - uname\t\t6  - Update")
    print("7  - Gedit\t\t8  - Install")
    print("9  - Start Up\t\t10 - Add Repository")
    print("11 - Reboot\t\t12 - Top")
    print("13 - pwd\t\t14 - Wget")
    print("15 - whoami\t\t16 - Nano")
    print("17 - uptime\t\t18 - autoclean")
    print("19 - crontab\t\t20 - du")
    print("21 - free\t\t22 - ps")
    print("23 - kill\t\t24 - mount")
    print("25 - lsusb\t\t26 - ifconfig")
    print("27 - iwconfig\t\t28 - last")
    print("29 - macAddress\t\t100 - MSG")
    print("101 - Shutdown")
    print("")
   
#2  diskinfo
def diskinfo():
    system("df -h")
    print("Press Enter...")
    raw_input()

#3  deletefile   
def deletefile():
    filename = raw_input('Enter Filename: ')
    result = system('rm -vr ' + filename)
    if (result != 0):
        print('Error Deleting file!')
    else:
        print('File deleted OK')
        print('Press enter...')
        raw_input()

#4  listopt 
def listopt():
    system("ls -ltcshaF | less")
    print("Press Enter...")
    raw_input()

#5  update ch
def update():
    system("sudo apt-get update && sudo apt-get upgrade")
    print("Press Enter...")
    raw_input()
   
#6  cpuinfo 
def cpuinfo():
    system("uname -a")
    print("Press Enter...")
    raw_input()

#7  gedit     
def gedit():
    system("gedit&")
    print("Press Enter...")
    raw_input()

#8  install   
def install():
    filename = raw_input("Enter Filename: ")
    result = system("sudo apt-get install " + filename)
    if (result == 0):
        print("Application not found")
    else:
        print("File Downloaded")
        print("Press Enter...")
        raw_input()

#9  startup
def startup():
    system("gnome-session-properties&")
    print("Press Enter...")
    raw_input()

#10 repo
def repo():
    repolist = raw_input("Please Enter Repository: ")
    result = system("sudo add-apt-repository ppa:" + repolist)
    if (result != 0):
        print("Repository Not added")
        system("sleep 2")
    else:
        print("Repository Added")
        system("sleep 2")
        print("Press Enter...")
        raw_input()

#11 reboot
def reboot():
    system("sudo reboot")
   
#12 top     
def top():
    system("top")
    print("Press Enter...")
    raw_input()

#13 pwd
def pwd():
    system("pwd")
    print("Press Enter...")
    raw_input()   

#14 wget
def wget():
    web = raw_input("Enter Website: ")
    result = system("wget " + web)
    if (result != 0):
        print("Website Not Downloaded")
    else:
        print("Website Downloaded")
        print("Press Enter...")
        raw_input()   

   
#15 who
def who():
    system('who am i')
    print("Press Enter...")
    raw_input()
   
#16 nano
def nano():
    system("nano")
    print("Press Enter...")
    raw_input()

#17 uptime
def uptime():   
    system("uptime")
    print("Press Enter...")
    raw_input()

#18 autoclean
def autoclean():
    system("sudo apt-get autoclean")
    print("Press Enter...")
    raw_input()

#19 crontab
def crontab():
    system("crontab -e")
    print("Press Enter...")
    raw_input()
   
#20 du
def du():
    system("du -sh")
    print("Press Enter...")
    raw_input()
   
#21 free
def free():
    system('free -m')
    print("Press Enter...")
    raw_input()

#22 ps   
def ps():
    system("ps -e")
    print("Press Enter...")
    raw_input()

#23 kill
def kill():
    system("echo Enter PID to KILL: ; read id ; ps -e | grep $id; kill $id > /dev/null 2>&1;")
    print("Press Enter...")
    raw_input()
   
#24 mount   
def mount():
    system("mount")
    print("Press Enter...")
    raw_input()
   
#25 usb
def usb():
    system("lsusb")
    print("Press Enter...")
    raw_input()
   
   
#26 iwconfig
def iwconfig():
    system("iwconfig")
    print("Press Enter...")
    raw_input()
   

#27 if
def ifconfig():
    system("ifconfig")
    print("Press Enter...")
    raw_input()
   
#28 last
def last():
    system("last")
    print("Press Enter...")
    raw_input()

#29 macAddress
def macAddress():
    system("cat /sys/class/net/*/address | sort -u")
    print("Press Enter...")
    raw_input()

#100 
def msg():
    print("BACK UP EVERYTHING BEFORE YOU LOSE EVERYTHING")
    raw_input()

#101 shutdown
def shutdown():
    system("sudo init 0")

#200 sudo
def sudo():
    system("sudo python codeprez.py")
       
x = 0

while (x != 1):
    system("clear")
    showoptions()
    x = input("Enter your choice: ")
   
    if (x == 2):
        diskinfo()
    if (x == 3):
        listopt()
    if (x == 4):
        deletefile()
    if (x == 5):
        cpuinfo()
    if (x == 6):
        update()
    if (x == 7):
        gedit()
    if (x == 8):
        install()
    if (x == 9):
        startup()
    if (x == 10):
        repo()
    if (x == 11):
        reboot()
    if (x == 12):
        top()
    if (x == 13):
        pwd()
    if (x == 14):
        wget()
    if (x == 15):
        who()
    if (x == 16):
        nano()
    if (x == 17):   
        uptime()
    if (x == 18):
        autoclean()
    if (x == 19):
        crontab()
    if (x == 20):
        du()
    if (x == 21):
        free()
    if (x == 22):
        ps()
    if (x == 23):
        kill()
    if (x == 24):
        mount()
    if (x == 25):
        usb()
    if (x == 26):
        ifconfig()
    if (x == 27):
        iwconfig()
    
    if (x == 28):
        last()
    if (x == 29):
        macAddress()           
    if (x == 100):
        msg()
    if (x == 101):
        shutdown()
    if (x == 200):
       sudo()
         
print "Program ended."

