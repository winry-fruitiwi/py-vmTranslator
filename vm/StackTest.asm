// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP0.TRUE
D;JEQ
@JUMP0.FALSE
0;JMP
(JUMP0.TRUE)
@SP
A=M-1
M=-1
@EN0D
0;JMP
(JUMP0.FALSE)
@SP
A=M-1
M=0
(EN0D)


// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP1.TRUE
D;JEQ
@JUMP1.FALSE
0;JMP
(JUMP1.TRUE)
@SP
A=M-1
M=-1
@EN1D
0;JMP
(JUMP1.FALSE)
@SP
A=M-1
M=0
(EN1D)


// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP2.TRUE
D;JEQ
@JUMP2.FALSE
0;JMP
(JUMP2.TRUE)
@SP
A=M-1
M=-1
@EN2D
0;JMP
(JUMP2.FALSE)
@SP
A=M-1
M=0
(EN2D)


// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP3.TRUE
D;JLT
@JUMP3.FALSE
0;JMP
(JUMP3.TRUE)
@SP
A=M-1
M=-1
@EN3D
0;JMP
(JUMP3.FALSE)
@SP
A=M-1
M=0
(EN3D)


// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP4.TRUE
D;JLT
@JUMP4.FALSE
0;JMP
(JUMP4.TRUE)
@SP
A=M-1
M=-1
@EN4D
0;JMP
(JUMP4.FALSE)
@SP
A=M-1
M=0
(EN4D)


// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP5.TRUE
D;JLT
@JUMP5.FALSE
0;JMP
(JUMP5.TRUE)
@SP
A=M-1
M=-1
@EN5D
0;JMP
(JUMP5.FALSE)
@SP
A=M-1
M=0
(EN5D)


// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP6.TRUE
D;JGT
@JUMP6.FALSE
0;JMP
(JUMP6.TRUE)
@SP
A=M-1
M=-1
@EN6D
0;JMP
(JUMP6.FALSE)
@SP
A=M-1
M=0
(EN6D)


// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP7.TRUE
D;JGT
@JUMP7.FALSE
0;JMP
(JUMP7.TRUE)
@SP
A=M-1
M=-1
@EN7D
0;JMP
(JUMP7.FALSE)
@SP
A=M-1
M=0
(EN7D)


// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@JUMP8.TRUE
D;JGT
@JUMP8.FALSE
0;JMP
(JUMP8.TRUE)
@SP
A=M-1
M=-1
@EN8D
0;JMP
(JUMP8.FALSE)
@SP
A=M-1
M=0
(EN8D)


// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
@SP
M=M-1


// push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1

// neg
@SP
A=M-1
M=-M

// and
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D&M
@SP
M=M-1


// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D|M
@SP
M=M-1

// not
@SP
A=M-1
M=!M
