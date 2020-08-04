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
        self.boardwin = curses.newwin(11, 21, 1, curses.COLS // 2 - (21 // 2))
        self.msgwin = curses.newwin(5, 40, 12, curses.COLS // 2 - (40 // 2))
        self.inputwin = curses.newwin(3, 30, 18, curses.COLS // 2 - (30 // 2))


    def set_board(self, inputstr):
        self.boardwin.addstr(1, 2, inputstr)
        self.boardwin.box()
        self.boardwin.refresh()

    def set_msg(self, inputstr):
        self.msgwin.addstr(0, 1,inputstr)
        self.msgwin.box()
        self.msgwin.refresh()

    def get_player_input(self, msg):
        self.inputwin.addstr(1, 1, msg)
        self.inputwin.box()
        self.inputwin.refresh()
        value = self.inputwin.getstr().decode("utf-8")
        self.inputwin.erase()
        self.msgwin.erase()
        return value
