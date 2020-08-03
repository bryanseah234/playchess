import curses


class ConsoleInterface:
    def __init__(self):
        pass

    def set_board(self, inputstr):
        """
        Takes board info as an input string and prints it to the console
        """
        print(inputstr)

    def set_msg(self, inputstr):
        """
        Takes an inputstr and prints it to the console
        """
        print(inputstr)

    def get_player_input(self, msgstr):
        """
        Prints a msgstr and prompt player fpr input and retrive as a string
        """
        value = input(msgstr)
        return value


class TextInterface:
    def __init__(self):
        stdscr = curses.initscr()
        self.boardwin = curses.newwin(11, 18, 1, 1)
        self.msgwin = curses.newwin(5, 40, 11, 1)
        self.inputwin = curses.newwin(3, 40, 16, 1)

    def set_board(self, inputstr):
        self.boardwin.addstr(0, 0, inputstr)
        self.boardwin.refresh()

    def set_msg(self, inputstr):
        self.msgwin.addstr(0, 0, inputstr)
        self.msgwin.refresh()

    def get_player_input(self, msg):
        self.inputwin.addstr(0, 0, msg)
        self.inputwin.refresh()
        value = self.inputwin.getstr().decode("utf-8")
        self.inputwin.erase()
        self.msgwin.erase()
        return value
