area 	minmax,code
	entry
max 	rn 3
min 	rn 4
	adr r0,values
	ldr r1,=len
	
	mov max,#0
	mov min,#999

loop	subs r1,r1,#1
	beq go
	ldr r2,[r0],#4
	cmp max,r2
	bgt small
	mov max,r2
	b loop

small	cmp min,r2
	bgt less
	bx lr

less	mov min,r2
	b loop

go	b go



values dcd 1,2,3,4,5,6,7,8	