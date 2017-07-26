# Program to rename files
# Created by https://github.com/somestrhere

import os
from helpers import clearConsole

def menu() :
    """Displays the program menu."""

    # Show current working directory
    path = os.getcwd()
    print('\nYour working directory is:\n{0}'.format(path))

    # Menu
    print('')
    print('1) Change working directory')
    print('2) Rename files in working directory')

    menuChoice = input('\nWhat would you like to do? ')

    if menuChoice == '1' :
        changeDirectory()

    elif menuChoice == '2' :
        renameFiles()
    else :
        menu()

def changeDirectory() :
    """Changes the current working directory."""

    print('\nPlease enter new working directory path:')
    inputPath = input()

    try :
        os.chdir(inputPath)
        newPath = os.getcwd()
        print('\nWorking directory sucessfully changed to:\n{0}\n'.format(newPath))
        menu()

    except :
        print('Sorry, there was an error')
        print('Unable to change path to :\n{0}\n'.format(inputPath))
        input('Press Enter to return to the menu')
        clearConsole()
        menu()

def renameFiles() :
    """Rename files in current working directory.
    
    Displays a list of files in the current working directory
    and requests confirmation. User is then either returned to 
    the menu or or asked to choose the type of rename operation
    to be carried out.
    
    """

    clearConsole()
    print('\nThe following files are present in your working directory:\n')
    displayFiles()

    confirmation = input('\nPress \'Y\' to continue... ').upper()

    while confirmation == 'Y' :
        break

    else :
        clearConsole()
        print('Returning you to the menu...')
        menu()

    def removeWhiteSpace(file) :
        """Removes white space from file names."""

        try :
            # Remove white space from file names
            newFile = file.replace(" ","")

            if( newFile != file) :
                os.rename(file,newFile)

        except :
              print('\nSorry, there was an error')
              input('Press Enter to return to the menu')
              menu()

        clearConsole()
        print('\nFilenames successfully renamed')
        menu()
    
    for file in os.listdir() :

        print('\nEnter \'W\' to remove white space')
        renameType = input().upper()

        if renameType == 'W' :
            removeWhiteSpace(file)

        else :
            clearConsole()
            print('Returning you to the menu...')
            menu()

def displayFiles() :
    """Displays a list of files in the current working directory."""

    for file in os.listdir() :
       print(file)

def main() : 
    
    menu()


if __name__ == "__main__" :
    main()
