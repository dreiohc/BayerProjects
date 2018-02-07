import datetime
import os
import ctypes
from ctypes.wintypes import HWND, LPWSTR, UINT
import sys


#path

temporary_path = ("C:\Temp")

LDMS_name = "LDMS Software"


    
#tools_folder = ("Tools")
#tools_path = os.path.join(temporary_path, tools_folder)

LDMS_name = "LDMS Software"


LDMS_tool = os.path.join(temporary_path, LDMS_name+'.txt')


today = datetime.date.today()

# myron = "Myron"
# IT_path = "//wphtags0001//Temporary//Backup//backup_log//IT"
# myron_path = os.path.join(IT_path, myron + ".txt")
# IT_folder = os.path.join(IT_path, LDMS_name + '.txt')

# edmond = "Edmond"
# IT_path = "//wphtags0001//Temporary//Backup//backup_log//IT"
# edmond_path = os.path.join(IT_path, edmond + ".txt")
# IT_folder = os.path.join(IT_path, LDMS_name + '.txt')

# adam = "Adam"
# IT_path = "//wphtags0001//Temporary//Backup//backup_log//IT"
# adam_path = os.path.join(IT_path, adam + ".txt")
# IT_folder = os.path.join(IT_path, LDMS_name + '.txt')

# gab = "Gab"
# IT_path = "//wphtags0001//Temporary//Backup//backup_log//IT"
# gab_path = os.path.join(IT_path, gab + ".txt")
# IT_folder = os.path.join(IT_path, LDMS_name + '.txt')

# roger = "Roger"
# IT_path = "//wphtags0001//Temporary//Backup//backup_log//IT"
# roger_path = os.path.join(IT_path, roger + ".txt")
# IT_folder = os.path.join(IT_path, LDMS_name + '.txt')



if str(today) in open(myron_path).read():

    _user32 = ctypes.WinDLL('user32', use_last_error=True)

    _MessageBoxW = _user32.MessageBoxW
    _MessageBoxW.restype = UINT  # default return type is c_int, this is not required
    _MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

    MB_OK = 0
    MB_OKCANCEL = 1
    MB_YESNOCANCEL = 3
    MB_YESNO = 4

    IDOK = 0
    IDCANCEL = 2
    IDABORT = 3
    IDYES = 6
    IDNO = 7


    def MessageBoxW(hwnd, text, caption, utype):
        result = _MessageBoxW(hwnd, text, caption, utype)
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return result


    def main():
        try:
            result = MessageBoxW(None, "Please install the following in respective hostnames:\n" + " " + open(LDMS_tool).read() + "\n\nClick YES if you already push it in LDMS\nNO if not yet", "Software Request", MB_YESNO)
            if result == IDYES:
                open(LDMS_tool, "w").close()   
                #open(IT_folder, "w").close()
                
                
                #print("user pressed ok")
            elif result == IDNO:
                sys.exit()
            #elif result == IDCANCEL:
                #print("user pressed cancel")
            else:
                print("unknown return code")
        except WindowsError as win_err:
            print("An error occurred:\n{}".format(win_err))

    if __name__ == "__main__":
        main()