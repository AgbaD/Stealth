#!/usr/bin/python
# Author:   @BlankGodd

from subprocess import call
import os
from platform import system


class Stealth:
    """
    A script to hide and unhide files or folders
    The complete path to the file must be given
    Functions for only Linux and Windows OS for now
    """

    def __init__(self):
        self.path = input("Enter the file path\n:")
        command = input("Enter command to 'hide' or unhide\n:").lower()
        if command == 'hide':
            self.hide()
        elif command == 'unhide':
            self.unhide()
        else:
            print("Invalid command!")
            self.__init__()

    def hide(self):
        opsys = system()
        if opsys == 'Windows':
            call(['attrib', "+H", self.path])
        elif opsys == 'Linux':
            lst = []
            try:
                lst = [i for i in self.path.split('/')]
            except:
                print("Invalid file path for linux")
            f = lst[-1]
            lst[-1] = '.{0}'.format(f)
            for i in range(len(lst)):
                c = lst[i]
                lst[i] = '/{0}'.format(c)
            lst.remove('/')
            new_path = ''.join(lst)
            os.rename(self.path, new_path)

        print("File hidden")
    
    def unhide(self):
        opsys = system()
        if opsys == 'Windows':
            call(['attrib', "-H", self.path])
        elif opsys == 'Linux':
            lst = []
            try:
                lst = [i for i in self.path.split('/')]
            except:
                print("Invalid file path for linux")
            f = lst[-1]
            lst[-1] = '.{0}'.format(f)
            val = lst[-1]
            for i in range(len(lst)):
                c = lst[i]
                lst[i] = '/{0}'.format(c)
            lst.remove('/')
            new_path = ''.join(lst)

            files = os.system('ls -a')
            for var in files:
                if var == val:
                    os.rename(new_path, self.path)

        print("File unhidden")
       
    
    
