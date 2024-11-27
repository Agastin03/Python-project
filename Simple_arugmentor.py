import sys
def Cli_parser(command):
    switcher={
            'start':"Starting the program....",
            'stop':"Stopping the program.....",
            'restart':"Restarting the program....",
            }
    return switcher.get(command,"Unknown Command")
if len(sys.argv)>1:
    print(Cli_parser(sys.argv[1]))
else:
    print("No command Provider")
    
print(Cli_parser("start"))
    