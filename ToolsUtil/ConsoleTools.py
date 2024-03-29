class ConsoleTools:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERSE = '\033[07m'

    @classmethod
    def print_main(cls, param):
        print(ConsoleTools.GREEN + ConsoleTools.BOLD + param + ConsoleTools.END)
        pass

    @classmethod
    def print_sub(cls, param):
        print(ConsoleTools.GREEN + param + ConsoleTools.END)
        pass

