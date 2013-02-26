/*******************************
    project: StudentVM_beta
    author: Alex Semin
    place: SPbU MM171
    date:  2013
*******************************/

#ifndef COMMANDS_H
#define COMMANDS_H

#include <stdlib.h>
#include <stdio.h>

typedef enum
{
    LDC, // load const to stack
    LD,  // load to stack from address
    ST,  // store from stack to address
    SWP, // exchange places of two stack's elements
    DUP, // double push top of stack
    POP,
    ADD, // add two stack's elements
    SUB, // x - y. x under y in stack
    MUL,
    DIV,
    MOD,
    CMP, // compare two stack's elements. Result [(-1) if (x < y)] [(0) if (x == y)] [(1) if (x > y)]. x under y in stack
    JMP, // unconditional jump to label
    BR,  // conditional jump to label (branch). Result: if there's 0 on stack then next command, else jump to label
    HLT, // correct ending of program
    LBL,
    ERR
} Opcode;

typedef struct Command *pCommand;
typedef struct Commands *pCommands;

typedef union
{
    int number;
    unsigned int address;
    char *label;
    pCommand jump;
} CommandArg;

pCommands createCommands(void);
pCommand createCommand(void);
CommandArg createCommandArg(void);
void deleteCommands(pCommands commands);
void pushCommand(pCommands commands, pCommand command);
void freeCommand(pCommand command);

pCommand getCommandsHead(pCommands commands);
void eraseCommand(pCommands commands, pCommand command, pCommand previous);
void setNextCommand(pCommand command, pCommand next);
pCommand getNextCommand(pCommand command);
int getCommandID(pCommand command);
Opcode getOpcode(pCommand command);
CommandArg getArg(pCommand command);
void setOpcode(pCommand command, Opcode opcode);
void setCommandArg(pCommand command, CommandArg arg);

void printCommands(FILE *output, pCommands commands);
void printCommand(FILE *output, pCommand command);


#endif // COMMANDS_H
