import chatwrap
from os import system
system("")
class style:
    """
    class made for styling using ansii, not implemented but used for devs who want to
    use a color + "" + RESET
    """
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

api_key="ENTER API KEY HERE"

inputPrompt="Enter a request: "
c=chatwrap.Code(api_key=api_key,model=chatwrap.Code.davinci_code_engine)
def handle(answer):return c.getCode(answer)
while True:
    a=input(inputPrompt)
    b=handle(a)
    print("The answer given: "+b)
    