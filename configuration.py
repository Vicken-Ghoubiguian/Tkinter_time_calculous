# Import all necessary Python built-in modules
from ctypes import *
from os import path, system

# Definition of all needed colors and typographic styles
red = "\033[91m"
green = "\033[92m"
cyan = "\033[96m"
underline = "\033[4m"
bold = "\033[1m"
reset = "\033[0m"

# Definition of the function 'isAvailableGitRepos' which determine if the 'directory' repos is an available Git repos
def isAvailableGitRepos(directory):

    # Definition of all needed variables
    git_folder = ".git"
    git_folder_structure = ["config", "HEAD", "hooks", "index", "packed-refs", "objects", "objects/info", "objects/pack", "refs", "refs/remotes", "refs/heads", "refs/tags"]
    result = True

    # 
    if not path.exists(directory + "/" + git_folder):

        # Assign the 'False' boolean value to the 'result' boolean variable
        result = False

    #
    else :

        #
        for fgs in git_folder_structure:

            #
            if not path.exists(directory + "/" + git_folder + "/" + fgs):

                # Assign the 'False' boolean value to the 'result' boolean variable
                result = False

                # Quit the loop
                break

    # Return the 'result' boolean variable
    return result

# Definition of the function 'configurationTimeCalculous' which configure the 'time_calculous_with_Flask_restx' project to be ready to run
def configurationTimeCalculous():

    # Definition of all needed variables
    the_GitHub_repos_time_calculous = "https://github.com/Vicken-Ghoubiguian/time_calculous"
    repos_time_calculous = "time_calculous"
    so_time_calculous_file = "time_calculous.so"

    # In the case where the 'time_calculous.so' file does not exist
    if not path.exists(so_time_calculous_file):

        #
        try:

            # Clone the 'time_calculous' repository from the GitHub official repository (here : https://github.com/Vicken-Ghoubiguian/time_calculous)
            system("git clone " + the_GitHub_repos_time_calculous)
        
        #
        except Exception as exception:

            #
            pass

        #
        if not path.isdir(repos_time_calculous) or not isAvailableGitRepos(repos_time_calculous):

            #
            print("\n" + red + bold + "Error : the C library time_calculous' is not available ! Quitting the app !" + reset + "\n")
        
            # Quit the current web application
            quit()

        #
        system("cc -fPIC -shared -o " + so_time_calculous_file + " time_calculous/time_calculous/time_calculous.c")

        #
        print("\n" + green + bold + "Well done : the C library time_calculous' is now downloaded and installed ! It's now time to play !" + reset + "\n")

    # Otherwise 
    else:

        #
        print("\n" + cyan + bold + "Information : the C library time_calculous' is already downloaded and installed ! Starting the app !" + reset + "\n")

    # Generate the CDLL and return it to be used in the app
    return CDLL(so_time_calculous_file)