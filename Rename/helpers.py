# Helper functions

import os

def clearConsole() : 
    """Clears the console.

    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    """

    try :
       os.system('cls') #clears console on Windows

    except :
       os.system('clear') #clears console on Linux
