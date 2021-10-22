"""
Author: Jacob Hampton
Date Last Modified: 4/3/20
Purpose: Rename multiple files in a folder
"""
import os
from colorama import Fore, Back, Style



def get_path():
    correct = ''
    while correct != '1': 
        user_direct = input('Enter folder path of files to be renamed\nIf you don\'t enter a path, the default path will be selected\n')
    
        if user_direct == '':
            default = True
            print('Default path selected')
            user_direct = "C:/Users/User/Desktop/rename_me"
        else:
            default = False
        
        os.chdir(user_direct)
        for f in os.listdir():
            print('\nName of first file in folder:')
            print(f)
            break
        
        if not default:
            correct = input('You entered: '+ user_direct + '\nIf this is correct enter 1\n')
        else:
            correct = '1'
    
    return user_direct
    

def manual():
    os.chdir(get_path())
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        print('Current file name: ', f_name)
        new_name = input('Enter a new name for this file\n')
        os.rename(f, new_name + f_ext)
        
def auto():
    os.chdir(get_path())
    replace = input('Enter the phrase to be removed\n')
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_name = f_name.replace(replace, '')
        print('f_name: ', f_name)
        os.rename(f, f_name + f_ext)

def menu():
    select = input('Options:\n1: Manual renaming\n2: Automatic renaming\n')
    
    while select != '1' and select != '2':
        print('Enter 1 or 2')
        select = input('Options:\n1: Manual renaming\n2: Automatic renaming\n')
    if select == '1':
        manual()
    if select == '2':
        auto()
    print('Renaming Complete')
        
    
    
    
    
if __name__ == '__main__':
    menu()