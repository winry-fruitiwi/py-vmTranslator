# noinspection PyMethodMayBeStatic

# this class writes code into the console to be added to SimpleAdd.asm.


class CodeWriter:
    def __init__(self):
        # keep track of the comparisons, which have labels
        self.comparison_number = 0

    # translates arithmetic code, with a command type of C_ARITHMETIC.
    def translate_arithmetic(self, command):
        assembly = f"// {command}\n"
        # if the command is negative:
        if command == "neg":
            assembly += "@SP\n" \
                        "A=M-1\n" \
                        "M=-M\n"

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
                        "M=M-D\n" \
                        "@SP\n" \
                        "M=M-1\n"

        elif command == "eq":
            assembly += f"@SP\n" \
                        f"AM=M-1\n" \
                        f"D=M\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"D=M-D\n" \
                        f"@JUMP{self.comparison_number}.TRUE\n" \
                        f"D;JEQ\n" \
                        f"@JUMP{self.comparison_number}.FALSE\n" \
                        f"0;JMP\n" \
                        f"(JUMP{self.comparison_number}.TRUE)\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"M=-1\n" \
                        f"@EN{self.comparison_number}D\n" \
                        f"0;JMP\n" \
                        f"(JUMP{self.comparison_number}.FALSE)\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"M=0\n" \
                        f"(EN{self.comparison_number}D)\n"
            self.comparison_number += 1

        elif command == "lt":
            assembly += f"@SP\n" \
                        f"AM=M-1\n" \
                        f"D=M\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"D=M-D\n" \
                        f"@JUMP{self.comparison_number}.TRUE\n" \
                        f"D;JLT\n" \
                        f"@JUMP{self.comparison_number}.FALSE\n" \
                        f"0;JMP\n" \
                        f"(JUMP{self.comparison_number}.TRUE)\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"M=-1\n" \
                        f"@EN{self.comparison_number}D\n" \
                        f"0;JMP\n" \
                        f"(JUMP{self.comparison_number}.FALSE)\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"M=0\n" \
                        f"(EN{self.comparison_number}D)\n"
            self.comparison_number += 1

        elif command == "gt":
            assembly += f"@SP\n" \
                        f"AM=M-1\n" \
                        f"D=M\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"D=M-D\n" \
                        f"@JUMP{self.comparison_number}.TRUE\n" \
                        f"D;JGT\n" \
                        f"@JUMP{self.comparison_number}.FALSE\n" \
                        f"0;JMP\n" \
                        f"(JUMP{self.comparison_number}.TRUE)\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"M=-1\n" \
                        f"@EN{self.comparison_number}D\n" \
                        f"0;JMP\n" \
                        f"(JUMP{self.comparison_number}.FALSE)\n" \
                        f"@SP\n" \
                        f"A=M-1\n" \
                        f"M=0\n" \
                        f"(EN{self.comparison_number}D)\n"
            self.comparison_number += 1

        print(assembly)

    # translates memory access code, with command types of C_PUSH and C_POP.
    def translate_mem_access(self, command):
        command_breakdown = command.split(" ")
        assembly = f"\n// {command}\n"

        # print(command_breakdown)

        # a shorter name for command_breakdown[2]
        i = command_breakdown[2]

        if command_breakdown[0] == "push":
            if command_breakdown[1] == "argument":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@ARG\n" \
                            "A=M\n" \
                            "D=D+A\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M+1\n"

            elif command_breakdown[1] == "this":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@THIS\n" \
                            "A=M\n" \
                            "D=D+A\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M+1\n"

            elif command_breakdown[1] == "that":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@THAT\n" \
                            "A=M\n" \
                            "D=D+A\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M+1\n"

            elif command_breakdown[1] == "local":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@LCL\n" \
                            "A=M\n" \
                            "D=D+A\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M+1\n"

            elif command_breakdown[1] == "temp":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@5\n" \
                            "A=D+A\n" \
                            "D=M\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M+1\n"

            elif command_breakdown[1] == "static":
                assembly += f"@file.{i}\n" \
                            "D=M\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M+1"

            elif command_breakdown[1] == "constant":
                assembly += f"@{i}\n"   \
                            "D=A\n"   \
                            "@SP\n"   \
                            "A=M\n"   \
                            "M=D\n"   \
                            "@SP\n"   \
                            "M=M+1\n"

            elif command_breakdown[1] == "pointer":
                if command_breakdown[2] == "0":
                    assembly += "@THIS\n" \
                                "D=M\n" \
                                "@SP\n" \
                                "A=M\n" \
                                "M=D\n" \
                                "@SP\n" \
                                "M=M+1\n"
                else:
                    assembly += "@THAT\n" \
                                "D=M\n" \
                                "@SP\n" \
                                "A=M\n" \
                                "M=D\n" \
                                "@SP\n" \
                                "M=M+1\n"

        elif command_breakdown[0] == "pop":
            if command_breakdown[1] == "argument":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@ARG\n" \
                            "D=M+D\n" \
                            "@R13\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M-1\n" \
                            "A=M\n" \
                            "D=M\n" \
                            "@R13\n" \
                            "A=M\n" \
                            "M=D\n"

            elif command_breakdown[1] == "local":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@LCL\n" \
                            "D=M+D\n" \
                            "@R13\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M-1\n" \
                            "A=M\n" \
                            "D=M\n" \
                            "@R13\n" \
                            "A=M\n" \
                            "M=D\n"

            elif command_breakdown[1] == "this":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@THIS\n" \
                            "D=M+D\n" \
                            "@R13\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M-1\n" \
                            "A=M\n" \
                            "D=M\n" \
                            "@R13\n" \
                            "A=M\n" \
                            "M=D\n"

            elif command_breakdown[1] == "that":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@THAT\n" \
                            "D=M+D\n" \
                            "@R13\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M-1\n" \
                            "A=M\n" \
                            "D=M\n" \
                            "@R13\n" \
                            "A=M\n" \
                            "M=D\n"

            elif command_breakdown[1] == "temp":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@5\n" \
                            "D=A+D\n" \
                            "@R13\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M-1\n" \
                            "A=M\n" \
                            "D=M\n" \
                            "@R13\n" \
                            "A=M\n" \
                            "M=D\n"

            elif command_breakdown[1] == "static":
                assembly += "@SP\n" \
                            "AM=M-1\n" \
                            "D=M\n" \
                            f"@file.{i}\n" \
                            "M=D\n"

            elif command_breakdown[1] == "pointer":
                if i == "0":
                    assembly += "@SP\n" \
                                "AM=M-1\n" \
                                "D=M\n" \
                                "@THIS\n" \
                                "M=D\n"
                else:
                    assembly += "@SP\n" \
                                "AM=M-1\n" \
                                "D=M\n" \
                                "@THAT\n" \
                                "M=D\n"

        print(assembly)

    # the specs say that we need to close the output file, but I'm not writing
    # into it during this project because I'm not opening the output file!
