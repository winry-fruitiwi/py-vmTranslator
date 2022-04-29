from CodeWriter import CodeWriter
from Parser import Parser

code_writer = CodeWriter()
parser = Parser("vm/BasicTest.vm")

while parser.has_more_commands():
    current_line = parser.currentLine
    # print(current_line)

    # find the command type of the parser
    command_type = parser.command_type()

    # if the command type was push or pop, print memory access translation.
    if command_type == "C_PUSH" or command_type == "C_POP":
        code_writer.translate_mem_access(current_line)

    # if the command type was arithmetic, print arithmetic translation.
    elif command_type == "C_ARITHMETIC":
        code_writer.translate_arithmetic(current_line)

    # advance to avoid an infinite loop
    parser.advance()
