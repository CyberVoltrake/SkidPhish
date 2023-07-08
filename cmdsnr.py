import subprocess

def cmdsnr():
    print(Colors.RED + """ 
░██████╗██╗░░██╗██╗██████╗░██████╗░██╗░░██╗██╗░██████╗██╗░░██╗
██╔════╝██║░██╔╝██║██╔══██╗██╔══██╗██║░░██║██║██╔════╝██║░░██║
╚█████╗░█████═╝░██║██║░░██║██████╔╝███████║██║╚█████╗░███████║
░╚═══██╗██╔═██╗░██║██║░░██║██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║
██████╔╝██║░╚██╗██║██████╔╝██║░░░░░██║░░██║██║██████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝
    """ + Colors.RESET)
    print("")
    l33t_inp4t = input("Type '1' to continue [instagram]: ")
    if (l33t_inp4t == "1"):
       subprocess.run(["python", "instagram/instagram.py"]) 
    else:
        print("No valid option selected")

class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'


cmdsnr()
