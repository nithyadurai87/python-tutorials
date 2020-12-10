"""Basic software instalation use python"""
import os
os.system('clear');
def basic_sw():
    print "\n\n***************************BASIC SOFTWARE LIST******************************\n\n"
    print "\t1.VLC -media player\n\t2.GIMP - photo editing\n\t3.LIBRE OFFICE - Office works\n\t4.UGET - downloder\n\t5.JAVA \n\t6.Unity-twiktool\n\t7.VIM - text editor\n\t8.MYSQL - DBMS\n\t9.Inkscape "

basic_sw()
def update():
    print "\n\tYou Want UPDATE your system"
    x=int(input('1 for yes \n2 for no\nEnter your choice'))
    if x==1:
        os.system('sudo apt-get update')
        print "Your system Now updated"
    elif x==2:
        print "Not Update your System"
    else:
        print "\n\t****Invalid selection****"
        update()


ch = int(input('Enter your choice:'))
if ch==1:
    update() 
    os.system('sudo apt-get install vlc')
    print "Vlc install successful"
elif ch==2:
    update()
    os.system('sudo apt-get install gimp')
elif ch==3:
     update()
     os.system('sudo add-apt-repository ppa:libreoffice/libreoffice-4-4')
     os.system('sudo apt-get update')
     os.system('sudo apt-get dist-upgrade')
     os.system('sudo apt-get install libreoffice')
elif ch==4:
     update()
     os.system('sudo apt-get instal Uget')
elif ch==5:
     update()
     os.system('sudo apt-get install default-jdk')
elif ch==6:
     update()
     os.system('sudo apt-get install unity-tweak-tool')
elif ch==7:
     update()
     os.system('sudo apt-get install vim')
elif ch==8:
     update()
     os.system('sudo apt-get install mysql-server')
elif ch==9:
     update()
     os.system('sudo apt-get install inkscape')
else:
     print "\n\t****Invalid selection****"
     basic_sw()
