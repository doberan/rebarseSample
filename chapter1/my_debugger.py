'''
Created on 2017/09/04

@author: doberan
'''

from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    
    def load(self, path_to_exe):

        creation_flags = DEBUG_PROCESS
        
        startupinfo         = STARTUPINFO()
        process_infomation  = PROCESS_INFOMATION()
        
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        
        startupinfo.cb = sizeof(startupinfo)
        
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_infomation)):
            print "[*] We have successfully launched the process!"
            print "[*] PID: %d" % process_infomation.dwProcessId
        
        else:
            print "[*] Error: 0x%08x." % kernel32.GetLastError()
    
        
        
        
        