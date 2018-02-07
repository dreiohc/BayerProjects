rem Roaming

mkdir "%userprofile%\AppData\Roaming\SAP"

mkdir "%userprofile%\AppData\Roaming\Microsoft\Signatures"

mkdir "%userprofile%\AppData\Roaming\Microsoft\Speech"

mkdir "%userprofile%\AppData\Roaming\Microsoft\Spelling"

mkdir "%userprofile%\AppData\Roaming\Microsoft\Stationery"

mkdir "%userprofile%\AppData\Roaming\Microsoft\SystemCertificates"

mkdir "%userprofile%\AppData\Roaming\Microsoft\Sticky Notes"

mkdir "%userprofile%\AppData\Roaming\Mozilla\Firefox\Profiles"


rem Local

mkdir "%userprofile%\AppData\Local\SAP"

mkdir "%userprofile%\AppData\Local\Lotus"

mkdir "%userprofile%\AppData\Local\Microsoft\OneNote"

mkdir "%userprofile%\AppData\Local\Microsoft\Windows\Themes"

mkdir "%userprofile%\AppData\Local\Microsoft\Windows\Caches"

mkdir "%userprofile%\AppData\Local\Microsoft\Windows Sidebar"


rem Documents

mkdir "%userprofile%\Documents"


rem Roaming robo

robocopy "D:\backup_users\%username%\AppData\Roaming\SAP" %userprofile%\AppData\Roaming\SAP /z /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Roaming\Microsoft\Signatures" %userprofile%\AppData\Roaming\Microsoft\Signatures /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Roaming\Microsoft\Speech" %userprofile%\AppData\Roaming\Microsoft\Speech /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Roaming\Microsoft\Spelling" %userprofile%\AppData\Roaming\Microsoft\Spelling /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Roaming\Microsoft\Stationery" %userprofile%\AppData\Roaming\Microsoft\Stationery /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Roaming\Microsoft\SystemCertificates" %userprofile%\AppData\Roaming\Microsoft\SystemCertificates /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Roaming\Microsoft\Sticky Notes" "%userprofile%\AppData\Roaming\Microsoft\Sticky Notes" /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Roaming\Mozilla\Firefox\Profiles" "%userprofile%\AppData\Roaming\Mozilla\Firefox\Profiles" /z /copy:dat /e /tee /mt:32


rem Local robo

robocopy "D:\backup_users\%username%\AppData\Local\SAP" %userprofile%\AppData\Local\SAP /z /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Local\Lotus" %userprofile%\AppData\Local\Lotus /z /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Local\Microsoft\OneNote" %userprofile%\AppData\Local\Microsoft\OneNote /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Local\Microsoft\Windows\Themes" %userprofile%\AppData\Local\Microsoft\Windows\Themes /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Local\Microsoft\Windows\Caches" %userprofile%\AppData\Local\Microsoft\Windows\Caches /z /copy:dat /e /tee /mt:32

robocopy "D:\backup_users\%username%\AppData\Local\Microsoft\Windows Sidebar" "%userprofile%\AppData\Local\Microsoft\Windows Sidebar" /z /copy:dat /e /tee /mt:32



rem User robo

robocopy "D:\backup_users\%username%" %userprofile% /xf NTUSER.DAT /xf ntuser.dat.LOG1 /xf ntuser.dat.LOG2 /xd "%userprofile%\AppData" /xd "%userprofile%\Documents" /r:0 /xj /sec /copy:dat /e /tee /mt:32



rem Documents robo

robocopy "D:\backup_users\%username%\Documents" "%userprofile%\Documents" /xj /copy:dat /e /tee /mt:32



rem Music robo

robocopy "D:\backup_users\%username%\Music" "%userprofile%\Music" /xj /copy:dat /e /tee /mt:32


rem Temp in C robo

robocopy "D:\backup_users\%username%\CTemp" "C:\Temp" /xj /copy:dat /e /tee /mt:32

