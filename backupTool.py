import time
from subprocess import call
import os
import subprocess
import sys
import os.path
import ctypes
import csv
import pyaudio  
import wave 
import shutil 
import datetime 
import socket
#from datetime import datetime







print ('                    \n                       BACKUP TOOL')
time.sleep(1)
print ('\nREAD CAREFULLY: Please close all applications')

print ('\n                Make sure  PC is connected to Bayer network')

print ("\n                A single file that exceeds 500MB will not be backed up\n                unless you choose Full Backup Mode\n")

print ('\n                Make sure you remove any USB or wireless mouse dongle')


def myCWID(): 
    #time.sleep(6)
    #path

    CWID = os.environ['USERNAME']                                                                                               #assign CWID based on Userprofile path
    c_path = ('C://')
    userprofile_path = os.environ['USERPROFILE']
      

      
    pathtoD = ("D:/backup_users/")
    pathtoE = ("E:/backup_users/")
    pathtoI = ("I:/backup_users/")
    pathtoF = ("F:/backup_users/")
    
    
    CWID = os.environ["USERNAME"]
    backupLogsFolder = "Backup_logs"
    roaming = "Roaming_Backup_log"

        
    
    if os.path.exists(pathtoD):
        temporary_path = ("D:/backup_users/" + CWID)
        IT_path = ("D:/IT Backup logs")
        
        
    if os.path.exists(pathtoE):
        temporary_path = ("E:/backup_users/" + CWID)
        IT_path = ("E:/IT Backup logs")
        
        
    if os.path.exists(pathtoI):
        temporary_path = ("I:/backup_users/" + CWID)
        IT_path = ("I:/IT Backup logs")
        
        
    if os.path.exists(pathtoF):
        temporary_path = ("F:/backup_users/" + CWID)
        IT_path = ("F:/IT Backup logs")
        
        
    tools_folder = ("Tools")
    tools_path = os.path.join(temporary_path, tools_folder)                         
    programs_path = ('//AppData//Roaming//Microsoft//Windows//Start Menu//Programs')
    desktop = 'Desktop'
    start_menu_path = os.path.join(userprofile_path + programs_path)
    desktop_path = os.path.join(userprofile_path, desktop)
    hostname = socket.gethostname()
    
    #tools
    if os.path.exists(tools_path):
        shutil.rmtree(tools_path)
        
    #if not os.path.exists(tools_path):
    os.makedirs(tools_path)
    

    
    #roipe
    roipe_path = ('BIapps//PortletEngine//')
    roipe_name = "roiPE"
    roipe_exe = os.path.join(c_path, roipe_path + 'PortletEngine.exe')
    roipe_tool = os.path.join(tools_path, roipe_name)
    
    #aspect
    aspect_shortcut = 'Unified Agent Desktop.appref-ms'
    aspect_path = os.path.join(desktop_path, aspect_shortcut)
    aspect_name = "Aspect UAD"
    aspect_tool = os.path.join(tools_path, aspect_name)
    
    #globe tattoo
    globe_shortcut = 'Globe Tattoo Broadband.lnk'
    globe_path = os.path.join(desktop_path, globe_shortcut)
    globe_name = "Globe Tattoo"
    globe_tool = os.path.join(tools_path, globe_name)
    
    #dro2
    dro2_folder = ("//10.50.157.51//users$//"+ CWID)
    dro2_name = "Part of DRO2"
    dro2_tool = os.path.join(tools_path, dro2_name)
    
    #cycles
    cycles_folder86 = "Program Files (x86)//Kern//Design"
    cycles_folder = "Program Files//Kern//Design"
    cycles_path86 = os.path.join(c_path, cycles_folder86)
    cycles_path = os.path.join(c_path, cycles_folder)
    cycles_name = "Cycles Client"
    cycles_tool = os.path.join(tools_path, cycles_name)
    
    
    #global order tool
    got_shortcut = 'Global Order Tool.appref-ms'
    got_path = os.path.join(desktop_path, got_shortcut)
    got_name = "Global Order Tool"
    got_tool = os.path.join(tools_path, got_name)
    
    
    #powerBI
    
    powerBI_folder = "Program Files//Microsoft Power BI Desktop//bin"
    powerBI_folder86 = "Program Files (x86)//Microsoft Power BI Desktop//bin"
    powerBI_path86 = os.path.join(c_path, powerBI_folder86)
    powerBI_path = os.path.join(c_path, powerBI_folder)
    powerBI_name = "powerBI"
    powerBI_tool = os.path.join(tools_path, powerBI_name)

    
    
    #LDMS Tools
    
    #SAP Analysis
    
    SAP_folder = "Program Files//SAP BusinessObjects"
    SAP_folder86 = "Program Files (x86)//SAP BusinessObjects"
    SAP_path86 = os.path.join(c_path, SAP_folder86)
    SAP_path = os.path.join(c_path, SAP_folder)
    LDMS_name = "LDMS Software"
    SAP_name = "SAP Analysis\n"
    
    #LDMS tool
    LDMS_tool = os.path.join(IT_path, LDMS_name+'.txt')
    
    #MSVisio
    
    Visio_folder = "C://ProgramData//Microsoft//Windows//Start Menu//Programs//Bayer Software//Microsoft Office"
    Visio_name = "Microsoft Visio 2010\n"
    Visio_shortcut = "Microsoft Visio 2010.lnk"
    Visio_path = os.path.join(Visio_folder, Visio_shortcut)
    
    #inStep
    
    instep_folder = "Program Files//microTOOL//in-STEP BLUE"
    instep_folder86 = "Program Files (x86)//in-STEP BLUE"
    instep_path86 = os.path.join(c_path, instep_folder86)
    instep_path = os.path.join(c_path, instep_folder)
    LDMS_name = "LDMS Software"
    instep_name = "inSTEP BLUE\n"
    
    #Citrix Receiver
    
    citrixReceiver_folder = "Program Files//Citrix//Receiver"
    citrixReceiver_folder86 = "Program Files (x86)//Citrix//Receiver"
    citrixReceiver_path86 = os.path.join(c_path, citrixReceiver_folder86)
    citrixReceiver_path = os.path.join(c_path, citrixReceiver_folder)
    LDMS_name = "LDMS Software"
    citrixReceiver_name = "Citrix Receiver\n"
    

        
    #aspect log
    
    if os.path.exists(aspect_path):

        write_to_tools = open(aspect_tool, "w")
        write_to_tools.close()  
    
    #roipe log
    
    if os.path.exists(roipe_exe):

        write_to_tools = open(roipe_tool, "w")
        write_to_tools.close()                
               
    #globe log
    
    if os.path.exists(globe_path):
        write_to_tools = open(globe_tool, "w")
        write_to_tools.close()
        
    #dro2 log
    
    if os.path.exists(dro2_folder):
    
        write_to_tools = open(dro2_tool, "w")
        write_to_tools.close()
        
    #cycles    
    
    if os.path.exists(cycles_path or cycles_path86):
    
        write_to_tools = open(cycles_tool, "w")
        write_to_tools.close()
        
    #powerBI
    
    if os.path.exists(powerBI_path or powerBI_path86):
    
        write_to_tools = open(powerBI_tool, "w")
        write_to_tools.close()
        
    
    #global order tool
    if os.path.exists(got_path):
    
        write_to_tools = open(got_tool, "w")
        write_to_tools.close()
        
    #LDMS Tools
    
    # if os.path.exists(SAP_path or SAP_path86):
    
        # write_to_tools = open(LDMS_tool, "w")
        # write_to_tools.write(SAP_name)
        # write_to_tools.close()
        
#def IT():
    timenow = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    today = datetime.date.today() + datetime.timedelta(days=2)
    tomorrow = datetime.date.today() + datetime.timedelta(days=5)
    next = datetime.date.today() + datetime.timedelta(days=8)
    myron = "Myron"
    edmond = "Edmond"
    roger = "Roger"
    gab = "Gab"
    adam = "Adam"
    rickson = "Rickson"
    #IT_path = "//wphtags0001//Temporary//Backup//backup_log//IT"
    myron_path = os.path.join(IT_path, myron)
    edmond_path = os.path.join(IT_path, edmond)
    gab_path = os.path.join(IT_path, gab)
    adam_path = os.path.join(IT_path, adam)
    roger_path = os.path.join(IT_path, roger)
    rickson_path = os.path.join(IT_path, rickson)
    LDMS_name = "LDMS Software"
    IT_folder = os.path.join(IT_path, LDMS_name + '.txt')
    IT_name = int(input("1-Edmond\n2-Roger\n3-Gab\n4-Myron\n5-Adam\n6-Rickson\n\nEnter your number:\n->"))
    if IT_name == 4:
        print "\nWelcome Myron!"
        
        #SAP Analysis
        if os.path.exists(SAP_path or SAP_path86):
            write_to_tools = open(LDMS_tool, "a") # LDMS_tool = os.path.join(IT_path, LDMS_name+'.txt')
            write_to_tools.write(SAP_name)
            write_to_tools.close()

            write_to_IT = open(myron_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

            
        #Citrix Receiver
        if os.path.exists(citrixReceiver_path or citrixReceiver_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(citrixReceiver_name)
            write_to_tools.close()

            write_to_IT = open(myron_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
        #Visio
        if os.path.exists(Visio_path):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(Visio_name)
            write_to_tools.close()
        
            write_to_IT = open(myron_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
         
         #instep
        if os.path.exists(instep_path or instep_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(instep_name)
            write_to_tools.close()

            write_to_IT = open(myron_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            

        
        #LDMS Software                
        # if os.path.exists(LDMS_tool):
             # with open(LDMS_tool) as f:
                # with open(IT_folder, "a") as f1:
                    # for line in f:
                        # f1.write(line)
         #taskscheduler               
        if os.path.exists(LDMS_tool):
        
            write_to_tools = open(IT_folder, "a")
            write_to_tools.write("->" + "Distribute to current hostname of" + " " + CWID + "\n" + "     " + "Backup done by Myron at" + " " + str(timenow) + "\n\n")
            write_to_tools.close()

        
    if IT_name == 1:
        print "\nWelcome Edmond!"
        
        #SAP Analysis
        if os.path.exists(SAP_path or SAP_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(SAP_name)
            write_to_tools.close()

            write_to_IT = open(edmond_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

        #Citrix Receiver
        if os.path.exists(citrixReceiver_path or citrixReceiver_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(citrixReceiver_name)
            write_to_tools.close()

            write_to_IT = open(edmond_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
        #Visio
        if os.path.exists(Visio_path):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(Visio_name)
            write_to_tools.close()
        
            write_to_IT = open(edmond_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

         #instep
        if os.path.exists(instep_path or instep_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(instep_name)
            write_to_tools.close()

            write_to_IT = open(edmond_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
            
        #LDMS Software 
        # if os.path.exists(LDMS_tool):
             # with open(LDMS_tool) as f:
                # with open(IT_folder, "a") as f1:
                    # for line in f:
                        # f1.write(line)
        
        #taskscheduler
        if os.path.exists(LDMS_tool):
        
            write_to_tools = open(IT_folder, "a")
            write_to_tools.write("->" + "Distribute to current hostname of" + " " + CWID + "\n" + "     " + "Backup done by Edmond at" + " " + str(timenow) + "\n\n")
            write_to_tools.close()
            


    if IT_name == 2:
        print "\nWelcome Roger!"
        
        #SAP Analysis
        if os.path.exists(SAP_path or SAP_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(SAP_name)
            write_to_tools.close()

            write_to_IT = open(roger_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

        #Citrix Receiver
        if os.path.exists(citrixReceiver_path or citrixReceiver_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(citrixReceiver_name)
            write_to_tools.close()

            write_to_IT = open(roger_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
        
        #Visio
        if os.path.exists(Visio_path):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(Visio_name)
            write_to_tools.close()
        
            write_to_IT = open(roger_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

         #instep
        if os.path.exists(instep_path or instep_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(instep_name)
            write_to_tools.close()

            write_to_IT = open(roger_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
            

        # if os.path.exists(LDMS_tool):
             # with open(LDMS_tool) as f:
                # with open(IT_folder, "a") as f1:
                    # for line in f:
                        # f1.write(line)
         
        #taskscheduler         
        if os.path.exists(LDMS_tool):
        
            write_to_tools = open(IT_folder, "a")
            write_to_tools.write("->" + "Distribute to current hostname of" + " " + CWID + "\n" + "     " + "Backup done by Roger at" + " " + str(timenow) + "\n\n")
            write_to_tools.close()

    if IT_name == 3:
        print "\nWelcome Gab!"

        #SAP Analysis
        if os.path.exists(SAP_path or SAP_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(SAP_name)
            write_to_tools.close()

            write_to_IT = open(gab_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

        #Citrix Receiver
        if os.path.exists(citrixReceiver_path or citrixReceiver_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(citrixReceiver_name)
            write_to_tools.close()

            write_to_IT = open(gab_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
        #Visio
        if os.path.exists(Visio_path):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(Visio_name)
            write_to_tools.close()
        
            write_to_IT = open(gab_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()


         #instep
        if os.path.exists(instep_path or instep_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(instep_name)
            write_to_tools.close()

            write_to_IT = open(gab_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
            
        # #LDMS Software 
        # if os.path.exists(LDMS_tool):
             # with open(LDMS_tool) as f:
                # with open(IT_folder, "a") as f1:
                    # for line in f:
                        # f1.write(line)            

        #taskscheduler
        if os.path.exists(LDMS_tool):
        
            write_to_tools = open(IT_folder, "a")
            write_to_tools.write("->" + "Distribute to current hostname of" + " " + CWID + "\n" + "     " + "Backup done by Gab at" + " " + str(timenow) + "\n\n")
            write_to_tools.close()

        

    if IT_name == 5:
        print "\nWelcome Adam!"

        #SAP Analysis
        if os.path.exists(SAP_path or SAP_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(SAP_name)
            write_to_tools.close()

            write_to_IT = open(adam_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

        #Citrix Receiver
        if os.path.exists(citrixReceiver_path or citrixReceiver_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(citrixReceiver_name)
            write_to_tools.close()

            write_to_IT = open(adam_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
            
        #Visio
        if os.path.exists(Visio_path):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(Visio_name)
            write_to_tools.close()
        
            write_to_IT = open(adam_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

         #instep
        if os.path.exists(instep_path or instep_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(instep_name)
            write_to_tools.close()

            write_to_IT = open(adam_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
            

        # #LDMS Software         
        # if os.path.exists(LDMS_tool):
             # with open(LDMS_tool) as f:
                # with open(IT_folder, "a") as f1:
                    # for line in f:
                        # f1.write(line)
        
         #taskscheduler
        if os.path.exists(LDMS_tool):
        
            write_to_tools = open(IT_folder, "a")
            write_to_tools.write("->" + "Distribute to current hostname of" + " " + CWID + "\n" + "     " + "Backup done by Adam at" + " " + str(timenow) + "\n\n")
            write_to_tools.close()
            
            
    if IT_name == 6:
        print "\nWelcome Rickson!"
        
        #SAP Analysis
        if os.path.exists(SAP_path or SAP_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(SAP_name)
            write_to_tools.close()

            write_to_IT = open(rickson_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

        #Citrix Receiver
        if os.path.exists(citrixReceiver_path or citrixReceiver_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(citrixReceiver_name)
            write_to_tools.close()

            write_to_IT = open(rickson_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
        
        #Visio
        if os.path.exists(Visio_path):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(Visio_name)
            write_to_tools.close()
        
            write_to_IT = open(rickson_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()

         #instep
        if os.path.exists(instep_path or instep_path86):
            write_to_tools = open(LDMS_tool, "a")
            write_to_tools.write(instep_name)
            write_to_tools.close()

            write_to_IT = open(rickson_path+".txt", "w")
            write_to_IT.write(str(today) + "\n" + str(tomorrow) + "\n" + str(next))
            write_to_IT.close()
            
            

        # if os.path.exists(LDMS_tool):
             # with open(LDMS_tool) as f:
                # with open(IT_folder, "a") as f1:
                    # for line in f:
                        # f1.write(line)
         
        #taskscheduler         
        if os.path.exists(LDMS_tool):
        
            write_to_tools = open(IT_folder, "a")
            write_to_tools.write("->" + "Distribute to current hostname of" + " " + CWID + "\n" + "     " + "Backup done by Rickson at" + " " + str(timenow) + "\n\n")
            write_to_tools.close()

    
def Finished():
    print ('                    \n\n                               FINISHED!\n\n\n')
 
    time.sleep(2)
    print ('                               THANK YOU!\n\n                       You may close this program\n\n\n')  

def MsgBox():
        
    
    pathtoD = ('D:/backup_users/')
    pathtoE = ('E:/backup_users/')
    pathtoI = ('I:/backup_users/')
    pathtoF = ('F:/backup_users/')
        
        
    if os.path.exists(pathtoD):
        audioPath = ("D:/Tools/Source/warning.wav")
        
                
        #define stream chunk   
        chunk = 1024  

        #open a wav format music  
        f = wave.open(audioPath,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()
        
        ctypes.windll.user32.MessageBoxA(None, "Please check if there are no saved files outside User folder", "                            W    A   R   N   I   N   G!", 0)
               
            
            

    elif os.path.exists(pathtoE):
        
        
        audioPath = ("E:/Tools/Source/warning.wav")
        
                #define stream chunk   
        chunk = 1024  

        #open a wav format music  
        f = wave.open(audioPath,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()
        
        ctypes.windll.user32.MessageBoxA(None, "Please check if there are no saved files outside User folder", "                            W    A   R   N   I   N   G!", 0)
               
            


    elif os.path.exists(pathtoI):
        
        
        audioPath = ("I:/Tools/Source/warning.wav")
        
        #define stream chunk   
        chunk = 1024  

        #open a wav format music  
        f = wave.open(audioPath,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()
        
        ctypes.windll.user32.MessageBoxA(None, "Please check if there are no saved files outside User folder", "                            W    A   R   N   I   N   G!", 0)
               
            

        
    elif os.path.exists(pathtoF):


        audioPath = ("F:/Tools/Source/warning.wav")

    
        #define stream chunk   
        chunk = 1024  

        #open a wav format music  
        f = wave.open(audioPath,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()
        
        ctypes.windll.user32.MessageBoxA(None, "Please check if there are no saved files outside User folder", "                            W    A   R   N   I   N   G!", 0)
           

   
def HDD():
    
    #os.system('TASKKILL /F /IM Firefox.exe')
    while True: 
        pathtoD = ('D:/backup_users/')
        pathtoE = ('E:/backup_users/')
        pathtoI = ('I:/backup_users/')
        pathtoF = ('F:/backup_users/')
        CWID = os.environ["USERNAME"]
        backupLogsFolder = "Backup_logs"
        roaming = "Roaming_Backup_log"
        answerYes = ["yes" ,"Y" ,"y", "YES"]
        answerNo = ["No", "N" ,"n", "NO"]
        
        if os.path.exists(pathtoD):
            pathToCWID = pathtoD + CWID
            roaming_log = os.path.join(pathToCWID, backupLogsFolder + "Roaming_Backup_log.txt")
            documents_log =  os.path.join(pathToCWID, backupLogsFolder + "Documents_Backup_log.txt")
            local_log = os.path.join(pathToCWID, backupLogsFolder + "Local_Backup_log.txt")
            user_log = os.path.join(pathToCWID, backupLogsFolder + "UserProfile_Backup_log.txt")
            music_log = os.path.join(pathToCWID, backupLogsFolder + "Music_Backup_log.txt")
            
            
           
            isFull = raw_input("\nFull Backup Mode?(y/n):\n")
            
            if isFull in answerYes:
                print ('\nTransferring Files in D...')
                time.sleep(2)
                call('D:/Tools/Bats/backup_HDD_D_Drive_full.bat')
                
                print("\n\n             ROAMING FOLDER LOG:\n\n")
                with open(roaming_log) as f:
                    data = f.readlines()
                 
                break
            
            if isFull in answerNo:
                print ('\nTransferring Files in D...')
                time.sleep(2) 
                call('D:/Tools/Bats/backup_HDD_D_Drive.bat')
            
                print("\n\n             ROAMING FOLDER LOG:\n\n")
                with open(roaming_log) as f:
                    data = f.readlines()
                
            
                break
            
            
        if os.path.exists(pathtoF):
            pathToCWID = pathtoF + CWID
            roaming_log = os.path.join(pathToCWID, backupLogsFolder + "Roaming_Backup_log.txt")
            documents_log =  os.path.join(pathToCWID, backupLogsFolder + "Documents_Backup_log.txt")
            local_log = os.path.join(pathToCWID, backupLogsFolder + "Local_Backup_log.txt")
            user_log = os.path.join(pathToCWID, backupLogsFolder + "UserProfile_Backup_log.txt")
            music_log = os.path.join(pathToCWID, backupLogsFolder + "Music_Backup_log.txt")
            
            isFull = raw_input("Full Backup?(y/n):")
            
            if isFull in answerYes:
                print ('\nTransferring Files in F...')
                time.sleep(5)
                call('F:/Tools/Bats/backup_HDD_F_Drive_full.bat')
            
            if isFull in answerNo:
                print ('\nTransferring Files in F...')
                time.sleep(5) 
                call('F:/Tools/Bats/backup_HDD_F_Drive.bat')
            
            print("\n\n             ROAMING FOLDER LOG:\n\n")
            with open(roaming_log) as f:
                data = f.readlines()
            break
        
        if os.path.exists(pathtoE):
            pathToCWID = pathtoE + CWID
            roaming_log = os.path.join(pathToCWID, backupLogsFolder + "Roaming_Backup_log.txt")
            documents_log =  os.path.join(pathToCWID, backupLogsFolder + "Documents_Backup_log.txt")
            local_log = os.path.join(pathToCWID, backupLogsFolder + "Local_Backup_log.txt")
            user_log = os.path.join(pathToCWID, backupLogsFolder + "UserProfile_Backup_log.txt")
            music_log = os.path.join(pathToCWID, backupLogsFolder + "Music_Backup_log.txt")
        
            isFull = raw_input("Full Backup?(y/n):")
            
            if isFull in answerYes:
                print ('\nTransferring Files in E...')
                time.sleep(5)
                call('E:/Tools/Bats/backup_HDD_E_Drive_full.bat')
            
            if isFull in answerNo:
                print ('\nTransferring Files in E...')
                time.sleep(5) 
                call('E:/Tools/Bats/backup_HDD_E_Drive.bat')
            
            print("\n\n             ROAMING FOLDER LOG:\n\n")
            with open(roaming_log) as f:
                data = f.readlines()
            
            
            break
            
        
        if os.path.exists(pathtoI):
            pathToCWID = pathtoI + CWID
            roaming_log = os.path.join(pathToCWID, backupLogsFolder, roaming + ".txt")
            documents_log =  os.path.join(pathToCWID, backupLogsFolder + "Documents_Backup_log.txt")
            local_log = os.path.join(pathToCWID, backupLogsFolder + "Local_Backup_log.txt")
            user_log = os.path.join(pathToCWID, backupLogsFolder + "UserProfile_Backup_log.txt")
            music_log = os.path.join(pathToCWID, backupLogsFolder + "Music_Backup_log.txt")
            
            isFull = raw_input("Full Backup?(y/n):")
            
            if isFull in answerYes:
                print ('\nTransferring Files in I...')
                time.sleep(5)
                call('I:/Tools/Bats/backup_HDD_I_Drive_full.bat')
            
            if isFull in answerNo:
                print ('\nTransferring Files in I...')
                time.sleep(5) 
                call('I:/Tools/Bats/backup_HDD_I_Drive.bat')
            
            print("\n\n             ROAMING FOLDER LOG:\n\n")
            with open(roaming_log) as f:
                data = f.readlines()
            
            
            
myCWID()
HDD()
MsgBox()
Finished()

 
