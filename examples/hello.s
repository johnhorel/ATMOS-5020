# Simple 'Hello World' program.
# Tested on MacOS 10.12.5
# Compiled with Apple Inc version cctools-895, GNU assembler version 1.38

# To compile:
#    as -arch x86_64  -o hello.o hello.s
#    ld -o hello hello.o
#    ./hello

.data
    HelloWorldString:
    .ascii "Hello World!\n"

.text

.globl start

start:
    # load all the arguments for write()
    movl $0x2000004, %eax
    movl $1, %ebx
    movq HelloWorldString@GOTPCREL(%rip), %rsi
    movq $100, %rdx
    # raises software interrupt to call write()
    syscall

    # call exit()
    movl $0x2000001, %eax
    movl $0, %ebx
    syscall
