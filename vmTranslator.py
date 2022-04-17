# this parses the input file and hands it to a currently nonexistent CodeWriter
class Parser:
    def __init__(self):
        # opens an input file.
        lines = open("vm/SimpleAdd.vm", "r")
        self.lines = lines.readlines()
        self.currentLineIndex = 0
        # the current line is whatever is at the current line index.
        self.currentLine = self.lines[self.currentLineIndex]

        # we only need the file array, not the file itself, so we can close it.
        lines.close()

    # read the input file.
    def read_file(self):
        for line in self.lines:
            stripped_line = line.strip("\n")
            print(f'{stripped_line}')

    # reads the current line
    def read_current_line(self):
        stripped_line = self.currentLine.strip("\n")
        print(f'{stripped_line}')
        self.advance()

    # advances to the next line
    def advance(self):
        self.currentLineIndex += 1
        self.currentLine = self.lines[self.currentLineIndex]

    # check if there are more lines to read.
    def has_more_commands(self):
        return self.currentLineIndex < len(self.lines) - 1


parser = Parser()
while parser.has_more_commands():
    parser.read_current_line()
