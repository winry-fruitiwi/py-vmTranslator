# this class writes code into the console to be added to results.asm.
class CodeWriter:
    def __init__(self):
        pass

    # translates arithmetic code, with a command type of C_ARITHMETIC.
    def translate_arithmetic(self):
        pass

    # translates memory access code, with command types of C_PUSH and C_POP.
    def translate_mem_access(self):
        pass

    # the specs say that we need to close the output file, but I'm not writing
    # into it during this project because it's still just as fast to copy-paste!
