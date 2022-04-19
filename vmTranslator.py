# add a blank line between the file path and new prints!
print()


# this parses the input file and hands it to a currently nonexistent CodeWriter
class Parser:
    def __init__(self):
        # opens an input file.
        lines = open("vm/Test.vm", "r")
        line_array = lines.readlines()
        self.currentLineIndex = 0
        self.lines = []

        # now it's time to clean up self.lines!
        for line in line_array:
            try:
                # if the line is a comment or whitespace, move on.
                if (line[0] == "/" and line[1] == "/") or len(line) == 0:
                    continue
            except IndexError:
                pass
            stripped_line = line.strip(" ").strip("\n")
            self.lines.append(stripped_line)

        # the current line is whatever is at the current line index.
        self.currentLine = self.lines[self.currentLineIndex]

        # we only need the file array, not the file itself, so we can close it.
        lines.close()

    # read the input file.
    def read_file(self):
        for line in self.lines:
            stripped_line = line.strip(" ").strip("\n")
            print(f'{stripped_line}')

    # reads the current line
    def read_current_line(self):
        stripped_line = self.currentLine.strip(" ").strip("\n")
        print(f'{stripped_line}')
        self.advance()

    # advances to the next line
    def advance(self):
        try:
            self.currentLineIndex += 1
            self.currentLine = self.lines[self.currentLineIndex]
        except IndexError:
            pass

    # check if there are more lines to read.
    def has_more_commands(self):
        return self.currentLineIndex <= len(self.lines) - 1

    # determines type of command
    def command_type(self):
        stripped_line = self.currentLine.strip(" ").strip("\n")
        arithmetic_strings = [
            "add",
            "sub",
            "neg",
            "eq",
            "gt",
            "lt",
            "and",
            "or",
            "not"
        ]
        # C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL are handled later

        # we don't need this line because if we're not doing arithmetic,
        # we must be doing memory access. We will need this later.
        # memory_access_strings = ["push", "pop"]

        # arithmetic
        math = [ele for ele in arithmetic_strings if (ele in stripped_line)]
        push = [ele for ele in ["push"] if (ele in stripped_line)]

        if math:
            return "C_ARITHMETIC"
        elif push:
            return "C_PUSH"
        else:
            return "C_POP"

    # find the first argument of the current line
    def arg1(self):
        line_components = self.currentLine.split(" ")
        return line_components[0]

    # find the first argument of the current line
    def arg2(self):
        try:
            # this should work for memory access, function, and call statements.
            line_components = self.currentLine.split(" ")
            return line_components[1]
        except IndexError as e:
            # if I have incorrect logic in my code, I can return the error.
            # then, I can check the error message and see what I should do with
            # my error. If it's an index error, then I terminate the program.
            return str(e)


parser = Parser()
parser.read_file()
print()

while parser.has_more_commands():
    print(parser.arg1() + " " + parser.arg2())
    parser.advance()
