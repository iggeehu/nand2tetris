// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

	// Put your code here.
	// 
	// int b=M[R1]
	// int sum=0
	// while(b>0)
	//{
	//      sum+=R[0];
        //	b--;
	//	}
	
	//set R2, or the sum, to 0
	@R2
	M=0
	//      M[R1]=M[R3], use R3 as iterator
	@R1
	D=M
	@R3
	M=D
(LOOP)
	//if D <= 0, go to END
	@R3
	D=M
	@END
	D			;JLE
	//Set D to store M[R0]
	@R0
	D=M
	//Add D's stored value to M[R2], or sum
	@R2
	M=M+D
	//decrease R3, or b, by 1, then go to loop.
	@R3
	M=M-1
	@LOOP
	0			;JMP
(END)
	@END
	0			; JMP
	

