'''
Created on 2017/09/04

'''
from ctypes import cdll

msvcrt = cdll.msvcrt
message_string = "hello world\n"
msvcrt.printf("Testing: %s", message_string)