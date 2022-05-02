# noinspection PyMethodMayBeStatic

# this class writes code into the console to be added to SimpleAdd.asm.


class CodeWriter:
    def __init__(self):
        # keep track of the comparisons, which have labels
        self.comp_num = 0

    # translates arithmetic code, with a command type of C_ARITHMETIC.
    def translate_arithmetic(self, command):
        assembly = [f'// {command}']
        # if the command is negative:
        if command == "neg":
            assembly.extend([
                '@SP',    # goto register 0
                'A=M-1',  # select *[SP-1]
                'M=-M'    # negate the top of the stack
            ])

        elif command == "not":
            assembly.extend(['@SP',     # goto register 0
                             'A=M-1',   # select *(SP-1)
                             'M=!M'     # not the top of the stack
                             ])

        elif command == "and":
            assembly.extend([
                            '@SP',      # goto SP
                            'A=M-1',    # goto *(SP-1)
                            'D=M',      # D = *(SP-1)
                            '@SP',      # go back to SP
                            'A=M-1',    # goto *(SP-2)
                            'A=A-1',
                            'M=D&M',    # D&M produces a bitwise and of 16 bits
                            '@SP',      # increment SP
                            'M=M-1'
                            ])

        elif command == "or":
            assembly.extend([
                            '@SP',      # goto SP
                            'A=M-1',    # goto *(SP-1)
                            'D=M',      # D = *(SP-1)
                            '@SP',      # go back to SP
                            'A=M-1',    # goto *(SP-2)
                            'A=A-1',
                            'M=D|M',    # D|M produces a bitwise or of 16 bits
                            '@SP',      # increment SP
                            'M=M-1'
                            ])

        elif command == "add":
            assembly.extend([
                        '@SP',          # goto SP
                        'A=M-1',        # goto *(SP-1)
                        'D=M',          # D = *(SP-1)
                        '@SP',          # go back to SP
                        'A=M-1',        # goto *(SP-2)
                        'A=A-1',
                        'M=D+M',        # D+M produces addition of 16 bits
                        '@SP',          # increment SP
                        'M=M-1'
            ])

        elif command == "sub":
            assembly.extend([
                        '@SP',          # goto SP
                        'A=M-1',        # goto *(SP-1)
                        'D=M',          # D = *(SP-1)
                        '@SP',          # go back to SP
                        'A=M-1',        # goto *(SP-2)
                        'A=A-1',
                        'M=M-D',        # subtract D from M
                        '@SP',          # increment SP
                        'M=M-1'
            ])
        elif command == "eq":
            assembly.extend([
                '@SP',                           # goto sp
                'AM=M-1',                        # decrement sp, select *(SP)
                'D=M',                           # D=*(SP)
                '@SP',                           # goto SP
                'A=M-1',                         # select *(SP-1)
                'D=M-D',                         # D=*(SP-1)-*(SP)
                f'@JUMP{self.comp_num}.TRUE',    # if D=0, jump to JUMP.TRUE
                'D;JEQ',
                f'@JUMP{self.comp_num}.FALSE',   # else, jump to JUMP.FALSE
                '0;JMP',
                f'(JUMP{self.comp_num}.TRUE)',   # set SP-1 to true (-1)
                '@SP',
                'A=M-1',
                'M=-1',
                f'@EN{self.comp_num}D',          # don't set SP-1 to false (0)
                '0;JMP',
                f'(JUMP{self.comp_num}.FALSE)',  # set SP-1 to false (0)
                '@SP',
                'A=M-1',
                'M=0',
                f'(EN{self.comp_num}D)'          # end of command
            ]
            )
            self.comp_num += 1

        elif command == "lt":
            assembly.extend([
                "@SP"                            # goto sp
                "AM=M-1"                         # decrement sp, select *(SP)
                "D=M"                            # D=*(SP)
                "@SP"                            # goto SP
                "A=M-1"                          # select *(SP-1)
                "D=M-D"                          # D=*(SP-1)-*(SP)
                f"@JUMP{self.comp_num}.TRUE"     # if D<0, jump to JUMP.TRUE
                "D;JLT"                          
                f"@JUMP{self.comp_num}.FALSE"    # else, jump to JUMP.FALSE
                "0;JMP"                          
                f"(JUMP{self.comp_num}.TRUE)"    # set SP-1 to true (-1)
                "@SP"                            
                "A=M-1"                         
                "M=-1"                           
                f"@EN{self.comp_num}D"           # don't set SP-1 to false (0)
                "0;JMP"                          
                f"(JUMP{self.comp_num}.FALSE)"   # set SP-1 to false (0)
                "@SP"                            
                "A=M-1"                          
                "M=0"                            
                f"(EN{self.comp_num}D)\n"        # end of command
                ])
            self.comp_num += 1

        elif command == "gt":
            assembly.extend([
                "@SP"                            # goto sp
                "AM=M-1"                         # decrement sp, select *(SP)
                "D=M"                            # D=*(SP)
                "@SP"                            # goto SP
                "A=M-1"                          # select *(SP-1)
                "D=M-D"                          # D=*(SP-1)-*(SP)
                f"@JUMP{self.comp_num}.TRUE"     # if D>0, jump to JUMP.TRUE
                "D;JGT"
                f"@JUMP{self.comp_num}.FALSE"    # else, jump to JUMP.FALSE
                "0;JMP"
                f"(JUMP{self.comp_num}.TRUE)"    # set SP-1 to true (-1)
                "@SP"
                "A=M-1"
                "M=-1"
                f"@EN{self.comp_num}D"           # don't set SP-1 to false (0)
                "0;JMP"
                f"(JUMP{self.comp_num}.FALSE)"   # set SP-1 to false (0)
                "@SP"
                "A=M-1"
                "M=0"
                f"(EN{self.comp_num}D)\n"        # end of command
            ])
            self.comp_num += 1

        for assembly_command in assembly:
            print(assembly_command)

    # translates memory access code, with command types of C_PUSH and C_POP.
    def translate_mem_access(self, command):
        command_breakdown = command.split(" ")
        assembly = [f'// {command}']

        # print(command_breakdown)

        # a shorter name for command_breakdown[2]
        i = command_breakdown[2]

        if command_breakdown[0] == "push":
            if command_breakdown[1] == "argument":
                assembly.extend([
                                f'@{i}',    # put i in the D register
                                'D=A',
                                '@ARG',     # goto *(ARG)
                                'A=M',
                                'D=D+A',    # return... this should be A=D+A
                                # 'D=M',
                                '@SP',      # goto *SP
                                'A=M',
                                'M=D',      # M = whatever D is
                                '@SP',      # SP++
                                'M=M+1'
                                ])

            elif command_breakdown[1] == "this":
                assembly.extend([
                                f"@{i}",    # put i in the D register
                                "D=A",
                                "@THIS",    # goto *(THIS)
                                "A=M",
                                "D=D+A",    # return... this should be A=D+A
                                # 'D=M',
                                "@SP",      # goto *SP
                                "A=M",
                                "M=D",      # M = whatever D is
                                "@SP",      # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "that":
                assembly.extend([
                                f"@{i}",    # put i in the D register
                                "D=A",
                                "@THAT",    # goto *(THAT)
                                "A=M",
                                "D=D+A",    # return... this should be A=D+A
                                # 'D=M',
                                "@SP",      # goto *SP
                                "A=M",
                                "M=D",      # M = whatever D is
                                "@SP",      # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "local":
                assembly.extend([
                                f"@{i}",    # put i in the D register
                                "D=A",
                                "@LCL",     # goto *(THAT)
                                "A=M",
                                "D=D+A",    # return... this should be A=D+A
                                # 'D=M',
                                "@SP",      # goto *SP
                                "A=M",
                                "M=D",      # M = whatever D is
                                "@SP",      # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "temp":
                assembly.extend([
                                f"@{i}"     # put i in the D register
                                "D=A"       
                                "@5"        # 
                                "A=D+A"     # 
                                "D=M"       # 
                                "@SP"       # 
                                "A=M"       # 
                                "M=D"       # 
                                "@SP"       # 
                                "M=M+1"     #
                                ])

            elif command_breakdown[1] == "static":
                assembly += f"@file.{i}\n" \
                            "D=M\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
                            "M=M+1"

            elif command_breakdown[1] == "constant":
                assembly += f"@{i}\n" \
                            "D=A\n" \
                            "@SP\n" \
                            "A=M\n" \
                            "M=D\n" \
                            "@SP\n" \
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
