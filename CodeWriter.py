# noinspection PyMethodMayBeStatic

# this class writes code into the console to be added to results.asm.
class CodeWriter:
    def __init__(self):
        pass

    # translates arithmetic code, with a command type of C_ARITHMETIC.
    def translate_arithmetic(self, command):
        assembly = f"// {command}\n"
        # if the command is negative:
        if command == "neg":
            assembly += "@SP\n" \
                        "A=M-1\n" \
                        "D=M\n"

        elif command == "not":
            assembly += "@SP\n" \
                        "A=M-1\n" \
                        "M=!M\n"

        elif command == "and":
            assembly += "@SP\n" \
                        "A=M-1\n" \
                        "D=M\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "A=A-1\n" \
                        "M=D&M\n" \
                        "@SP\n" \
                        "M=M-1\n"

        elif command == "or":
            assembly += "@SP\n" \
                        "A=M-1\n" \
                        "D=M\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "A=A-1\n" \
                        "M=D|M\n" \
                        "@SP\n" \
                        "M=M-1\n"

        elif command == "add":
            assembly += "@SP\n" \
                        "A=M-1\n" \
                        "D=M\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "A=A-1\n" \
                        "M=D+M\n" \
                        "@SP\n" \
                        "M=M-1\n"

        elif command == "sub":
            assembly += "@SP\n" \
                        "A=M-1\n" \
                        "D=M\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "A=A-1\n" \
                        "M=D-M\n" \
                        "@SP\n" \
                        "M=M-1\n"

        elif command == "eq":
            assembly += "@SP\n" \
                        "AM=M-1\n" \
                        "D=M\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "D=M-D\n" \
                        "@JUMP.TRUE\n" \
                        "D;JEQ\n" \
                        "@JUMP.FALSE\n" \
                        "0;JMP\n" \
                        "(JUMP.TRUE)\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "M=-1\n" \
                        "@END\n" \
                        "0;JMP\n" \
                        "(JUMP.FALSE)\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "M=0\n" \
                        "(END)\n"

        elif command == "lt":
            assembly += "@SP\n" \
                        "AM=M-1\n" \
                        "D=M\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "D=M-D\n" \
                        "@JUMP.TRUE\n" \
                        "D;JLT\n" \
                        "@JUMP.FALSE\n" \
                        "0;JMP\n" \
                        "(JUMP.TRUE)\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "M=-1\n" \
                        "@END\n" \
                        "0;JMP\n" \
                        "(JUMP.FALSE)\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "M=0\n" \
                        "(END)\n"

        elif command == "gt":
            assembly += "@SP\n" \
                        "AM=M-1\n" \
                        "D=M\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "D=M-D\n" \
                        "@JUMP.TRUE\n" \
                        "D;JGT\n" \
                        "@JUMP.FALSE\n" \
                        "0;JMP\n" \
                        "(JUMP.TRUE)\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "M=-1\n" \
                        "@END\n" \
                        "0;JMP\n" \
                        "(JUMP.FALSE)\n" \
                        "@SP\n" \
                        "A=M-1\n" \
                        "M=0\n" \
                        "(END)\n"

        print(assembly)

    # translates memory access code, with command types of C_PUSH and C_POP.
    def translate_mem_access(self):
        pass

    # the specs say that we need to close the output file, but I'm not writing
    # into it during this project because I'm not opening the output file!


code_writer = CodeWriter()
code_writer.translate_arithmetic("eq")
