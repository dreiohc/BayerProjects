echo Creating Roaming Folders... 

mkdir "D:\backup_users\%username%\AppData\Roaming\SAP" 

mkdir "D:\backup_users\%username%\AppData\Roaming\Microsoft\Signatures" 

mkdir "D:\backup_users\%username%\AppData\Roaming\Microsoft\Stationery" 

mkdir "D:\backup_users\%username%\AppData\Roaming\Microsoft\SystemCertificates" 

mkdir "D:\backup_users\%username%\AppData\Roaming\Microsoft\Sticky Notes" 

mkdir "D:\backup_users\%username%\AppData\Roaming\Mozilla\Firefox\Profiles" 

mkdir "D:\backup_users\%username%\AppData\Roaming\Microsoft\OneNote" 



echo Creating Local Folders... 

mkdir "D:\backup_users\%username%\AppData\Local\SAP" 

mkdir "D:\backup_users\%username%\AppData\Local\Lotus" 

mkdir "D:\backup_users\%username%\AppData\Local\Microsoft\OneNote" 

mkdir "D:\backup_users\%username%\AppData\Local\Microsoft\Windows\Themes" 

mkdir "D:\backup_users\%username%\AppData\Local\Microsoft\Windows\Caches" 

mkdir "D:\backup_users\%username%\AppData\Local\Microsoft\Windows Sidebar" 

mkdir "D:\backup_users\%username%\AppData\Local\Mozilla"



echo Creating C Temp Folder...

mkdir "D:\backup_users\%username%\CTemp"



echo Creating Documents Folder... 

mkdir "D:\backup_users\%username%\Documents" 




echo Creating Backup logs Folder...

mkdir "D:\backup_users\%username%\Backup_logs"



echo Copying Roaming Folders... 

robocopy %userprofile%\AppData\Roaming\SAP D:\backup_users\%username%\AppData\Roaming\SAP /z /r:1 /e /tee /mt:32 /log:"D:\backup_users\%username%\Backup_logs\Roaming_Backup_log.txt" 

robocopy %userprofile%\AppData\Roaming\Microsoft\Signatures D:\backup_users\%username%\AppData\Roaming\Microsoft\Signatures /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Roaming_Backup_log.txt"
 
robocopy %userprofile%\AppData\Roaming\Microsoft\Stationery D:\backup_users\%username%\AppData\Roaming\Microsoft\Stationery /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Roaming_Backup_log.txt"

robocopy %userprofile%\AppData\Roaming\Microsoft\SystemCertificates D:\backup_users\%username%\AppData\Roaming\Microsoft\SystemCertificates /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Roaming_Backup_log.txt"

robocopy "%userprofile%\AppData\Roaming\Microsoft\Sticky Notes" "D:\backup_users\%username%\AppData\Roaming\Microsoft\Sticky Notes" /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Roaming_Backup_log.txt"

robocopy "%userprofile%\AppData\Roaming\Mozilla\Firefox\Profiles" "D:\backup_users\%username%\AppData\Roaming\Mozilla\Firefox\Profiles" /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Roaming_Backup_log.txt"

robocopy "%userprofile%\AppData\Roaming\Microsoft\OneNote" "D:\backup_users\%username%\AppData\Roaming\Microsoft\OneNote" /z /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Roaming_Backup_log.txt"


echo Copying Local Folders... 


robocopy %userprofile%\AppData\Local\SAP D:\backup_users\%username%\AppData\Local\SAP /z /r:1 /e /tee /mt:32  /log:"D:\backup_users\%username%\Backup_logs\Local_Backup_log.txt"

robocopy %userprofile%\AppData\Local\Lotus D:\backup_users\%username%\AppData\Local\Lotus /z /r:1 /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Local_Backup_log.txt" 

robocopy %userprofile%\AppData\Local\Microsoft\OneNote D:\backup_users\%username%\AppData\Local\Microsoft\OneNote /z /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Local_Backup_log.txt"

robocopy %userprofile%\AppData\Local\Microsoft\Windows\Themes D:\backup_users\%username%\AppData\Local\Microsoft\Windows\Themes /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Local_Backup_log.txt"

robocopy %userprofile%\AppData\Local\Microsoft\Windows\Caches D:\backup_users\%username%\AppData\Local\Microsoft\Windows\Caches /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Local_Backup_log.txt"

robocopy "%userprofile%\AppData\Local\Microsoft\Windows Sidebar" "D:\backup_users\%username%\AppData\Local\Microsoft\Windows Sidebar" /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Local_Backup_log.txt"

robocopy "%userprofile%\AppData\Local\Mozilla" "D:\backup_users\%username%\AppData\Local\Mozilla" /z /r:1 /copy:dat /e /tee /mt:32 /log+:"D:\backup_users\%username%\Backup_logs\Local_Backup_log.txt"


echo Copying User Folders excluding AppData and Documents... 

robocopy "%userprofile%" "D:\backup_users\%username%" /xf ntuser.dat.LOG1 /xf ntuser.dat.LOG2 /xf NTUSER.dat /xd "%userprofile%\Music" /xd "%userprofile%\AppData" /xd %userprofile%\Documents /r:0 /z /copy:dat /xj /e /tee /mt:32 /log:"D:\backup_users\%username%\Backup_logs\UserProfile_Backup_log.txt" 


echo Copying Documents... 

robocopy "%userprofile%\Documents" "D:\backup_users\%username%\Documents" /z /copy:dat /xj /e /tee /mt:32 /log:"D:\backup_users\%username%\Backup_logs\Documents_Backup_log.txt"


echo Copying Music... 

robocopy "%userprofile%\Music" "D:\backup_users\%username%\Music" /xj /e /tee /mt:32  /r:0 /log:"D:\backup_users\%username%\Backup_logs\Music_Backup_log.txt"


echo Copying Temp Folder...

robocopy "C:\Temp" "D:\backup_users\%username%\CTemp" /xj /e /tee /mt:32  /r:0 /log:"D:\backup_users\%username%\Backup_logs\Temp_Backup_log.txt"




