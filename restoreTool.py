import time
from subprocess import call
import os
import smtplib
import subprocess
import sys
import ctypes
import glob
import msvcrt as m
import csv
import webbrowser
import socket 
import shutil, errno


def intro():

    print ('                    \n                       Welcome to RESTORE TOOL')
  
def Outlook():
    print("\nLaunching Outlook...\n")
    os.startfile('outlook')
    time.sleep(3)
    print("NOTE: Please renew digital signature ID by clicking Import Certificate in Outlook\n")                                 # Open Outlook
                                              
def Printers():
    time.sleep(5)
    print ('\nInstalling HP Printer...')
    time.sleep(7)
    if os.path.exists("E:/Installers"):
        call("E:/Installers/install_HP_printer_new.bat")
    if os.path.exists("D:/Installers"):
        call("D:/Installers/install_HP_printer_new.bat")
    if os.path.exists("I:/install_HP_printer_new.bat"):
        call("I:/Installers/install_HP_printer_new.bat")
    if os.path.exists("F:/install_HP_printer_new.bat"):
        call("F:/Installers/install_HP_printer_new.bat")
    time.sleep(2)
    print ('\nPrinter installed')
    
def restore():
    
    CWID = os.environ['USERNAME']
    
    
    pathtoD = ("D:/backup_users/")
    pathtoE = ("E:/backup_users/")
    pathtoI = ("I:/backup_users/")
    pathtoF = ("F:/backup_users/")
    
   
    if os.path.exists(pathtoD):
        path = ("D:/backup_users/")
        installer = ("D:/Installers/")
       
        
    if os.path.exists(pathtoE):
        path = ("E:/backup_users/")
        installer = ("E:/Installers/")
        
        
    if os.path.exists(pathtoI):
        path = ("I:/backup_users/")
        installer = ("I:/Installers/")
        
    
    if os.path.exists(pathtoF):
        path = ("F:/backup_users/")
        installer = ("F:/Installers/")
        
    
    
    
    
   #path = '//10.50.157.51//Temporary//backup//backup_log//'
    hostname = socket.gethostname()
    #Tools
    roipe = os.path.join(path + CWID + '//Tools//' + 'roiPE')
    aspect = os.path.join(path + CWID + '//Tools//' + 'Aspect UAD')
    globe = os.path.join(path + CWID + '//Tools//' + 'Globe Tattoo')
    dro2 = os.path.join(path + CWID + '//Tools//' + 'Part of DRO2')
    cycles = os.path.join(path + CWID + '//Tools//' + 'Cycles Client')
    got = os.path.join(path + CWID + '//Tools//' + 'Global Order Tool')
    powerBI = os.path.join(path + CWID + "//Tools//" + "PowerBI")
    citrixReceiver = os.path.join(path + CWID + "//Tools//" + "Citrix Receiver")
    
    #Answers
    tools_yes = ['yes', 'Yes', 'YES','yES','YeS','yEs','y','Y','Yes.','yes.','YES.']
    tools_no  = ['N','NO','n','no','No','nO','no.','No.','NO.'] 
    filename3 = os.path.join(path + CWID, 'I Have GMB.txt')

     
        
    if os.path.exists(roipe):
        while True:
            answer_roipe = raw_input('\n' + CWID + ' has roiPE\nWould you like to proceed with installation?(y/n):\n->')  #roiPE
            if answer_roipe in tools_yes:
            
                print ("Redirecting to bi.intranet.cnb...")
                time.sleep(2)
                webbrowser.open('http://bi.intranet.cnb/')
                break
            if answer_roipe in tools_no:
                break
            else:
                print 'Invalid input'

            print '\n-----------------------------\n'
            
    if os.path.exists(aspect):
        while True:
            answer_aspect = raw_input('\n' + CWID + ' has Aspect UAD\nProceed with installation?(y/n):\n->')      #Aspect
            if answer_aspect in tools_yes:
            
                print ("Installing Aspect Certificate...")
                time.sleep(2)
                aspectInstall = os.path.join(installer + "Aspect Link & Certificate//AspectCertInstall72_32bit.EXE")
                subprocess.call(aspectInstall)
                print "Redirecting to Aspect website..."
                time.sleep(2)
                webbrowser.open("http://by-cs262001/UADInstall/UADPresentationLayer.application")
                break
            if answer_aspect in tools_no:
                break
            else:
                print 'Invalid input'

            print '\n-----------------------------\n'
            
    if os.path.exists(globe):
        while True:
            answer_globe = raw_input('\n' + CWID + ' has Globe Tattoo Broadband\nProceed with installation?(y/n):\n->')  #Globe
            if answer_globe in tools_yes:
            
                raw_input ("Please generate the admin password of " + hostname + " before you press Enter...")
                
                
                if os.path.exists("C://Temp//Globe"):
                    subprocess.call('C://Temp//Globe//Globe Tattoo Broadband//Setup.exe', shell=True)
                    break
                if not os.path.exists("C://Temp//Globe"):
                    print ("\nWait...\n")
                    globeInstall = os.path.join(installer + "Globe Broadband original Installer")
            
                    shutil.copytree(globeInstall, "C://Temp//Globe")
                    subprocess.call('C://Temp//Globe//Globe Tattoo Broadband//Setup.exe', shell=True)
                    break
            if answer_globe in tools_no:
                break
            else:
                print 'Invalid input'

            print '\n-----------------------------\n'
            
    # if os.path.exists(dro2):
    
        # while True:
            # answer_dro2 = raw_input('\n' + CWID + ' is part of DRO2\nWould you like to import backup profile XML in Task Scheduler?(y/n):\n->')  #dro2
            # if answer_dro2 in tools_yes:
                # print ('\nBackup Profile is in ->\\wphtags0001\Temporary\BCP\Backup Profile.xml')
                # time.sleep(2)
                # print ("\nLaunching Task Scheduler...")
                # subprocess.call("Taskschd.msc", shell=True)
                # break
            # if answer_dro2 in tools_no:
                # break
            # else:
                # print 'Invalid input'

            # print '\n-----------------------------\n'
            
            
    if os.path.exists(cycles):
    
        while True:
            answer_cycles = raw_input('\n' + CWID + ' has Cycles Client\nProceed with installation?(y/n):\n->')  #kern
            if answer_cycles in tools_yes:
                raw_input ("Please generate the admin password of " + hostname + " before you press Enter...")
                
                if os.path.exists("C://Temp//Cycles//Kern Cycles 239f1"):
                    print ("\nLaunching Cycles Installer...")
                    
                    subprocess.call("C://Temp//Cycles//Kern Cycles 239f1//Cycles_239f1.msi", shell=True)
                    break
                
                if not os.path.exists("C://Temp//Cycles//Kern Cycles 239f1"):
                    print ("\nWait...\n")
                    kernInstall = os.path.join(installer + "Kern Design")
                    shutil.copytree(kernInstall, "C://Temp//Cycles")
                    print ("\nLaunching Cycles Installer...")
                    subprocess.call("C://Temp//Cycles//Kern Cycles 239f1//Cycles_239f1.msi", shell=True)
                    break

            if answer_cycles in tools_no:
                break
            else:
                print 'Invalid input'

            print '\n-----------------------------\n'    
            
            
            
    if os.path.exists(got):
        while True:
            answer_got = raw_input('\n' + CWID + ' has Global Order Tool\nProceed with installation?(y/n):\n->')  #Global Order Tool
            if answer_got in tools_yes:
            
                gotInstall = os.path.join(installer + "Global Order Tool.appref-ms")
                subprocess.call(gotInstall, shell=True)
                break
            if answer_got in tools_no:
                break
            else:   
                print 'Invalid input'

            print '\n-----------------------------\n'
            
    if os.path.exists(powerBI):
        while True:

            answer_powerBI = raw_input('\n' + CWID + ' has powerBI Desktop\nProceed with installation?(y/n):\n->')  #powerBI
            if answer_powerBI in tools_yes:
                raw_input ("Please generate the admin password of " + hostname + " before you press Enter...")
                
                if os.path.exists("C://Temp//powerBI"):
                    print ("\nLaunching powerBI Installer...")
                    subprocess.call("C://Temp//powerBI//powerBI.msi", shell=True)
                    break
                
                if not os.path.exists("C://Temp//powerBI//powerBI"):
                    print ("\nWait...\n")
                    powerBIInstall = os.path.join(installer + "powerBI")      
                    shutil.copytree(powerBIInstall, "C://Temp//powerBI")
                    print ("\nLaunching powerBI Installer...")
                    subprocess.call("C://Temp//powerBI//powerBI.msi", shell=True)
                    break
                    
            if answer_powerBI in tools_no:
                break
            else:
                print 'Invalid input'

            print '\n-----------------------------\n'    
            
                    
                    
                    
    
    raw_input('\nREADY!\nPress Enter to restore backup...')
    


    print '\nRestoring files...\n\nDo not close while restore is in progress'
    time.sleep(7)
    while True: 

        pathtoD = ('D:/backup_users')
        pathtoE = ('E:/backup_users')
        pathtoI = ('I:/backup_users')
        if os.path.exists(pathtoD):

            print ('\nRetrieving Files in D...')
            time.sleep(5) 
            call("D:/Tools/Bats/restore_HDD_D_Drive.bat")
            break
        if os.path.exists(pathtoE):

            print ('\nRetrieving Files in E...')
            time.sleep(5) 
            call("E:/Tools/Bats/restore_HDD_E_Drive.bat")
            break

        if os.path.exists(pathtoI):

            print ('\nRetrieving Files in I...')
            time.sleep(5) 
            call("I:/Tools/Bats/restore_HDD_I_Drive.bat")
            break

            
        if os.path.exists(pathtoF):

            print ('\nRetrieving Files in F...')
            time.sleep(5) 
            call("F:/Tools/Bats/restore_HDD_F_Drive.bat")
            break
            
            
        else:
            
            time.sleep(5)
            print ('\n\nCannot detect HDD in drive E or D\n\nRunning network mode instead...')
            time.sleep(2)
            print ('\nplease connect to LAN. restore will start in 30 seconds...\nPlease wait...')
            time.sleep(35)
            call('//10.50.157.51/Install App/Bats/restore_thru_network.bat')
            break

    

def Finished():
    
    print ('                    \n\n                               F I N I S H E D!\n\n\n')
    yes_sd = ['Y','y']
    time.sleep(1)
    answer_sd = raw_input ("                               THANK YOU!\n\n                       Don't forget to sign the Backup Request Form                       \n\n                     Enter y to enable Night Shift Mode\n\n\n")
    if answer_sd in yes_sd:
        subprocess.call(["shutdown", "-f", "-s", "-t", "7200"])
	
    
def MsgBox():
    ctypes.windll.user32.MessageBoxA(None, "                             \n\nAll files have been successfully restored\n\n\n                      Thank you!", "    F I N I S H E D!", 0)

    
    
    
#intro() 
#Outlook()
#restore()
Printers()
MsgBox()
Finished()          




