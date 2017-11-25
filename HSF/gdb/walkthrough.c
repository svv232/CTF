#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void begin(){
    printf("---------------------------------------\n");
    printf("Here is a quick gdb tutorial\n");
    printf("let's try and solve this basic crack me\n\n");
    printf("A good place to start is find all function names\n");
    printf("This will give us a general sense of control flow and functionality\n");
    printf("---------------------------------------\n");
}

void explanation1(){
    printf("---------------------------------------\n");
    printf("let's open up this executable in gdb and run\n");
    printf("gdb <filename>");
    printf("\n");
    printf("---------------------------------------\n");
}

void explanation2(){
    printf("---------------------------------------\n");
    printf("*info functions -will list out all function names!!\n");
    printf("you can place a break point like so on any function where you want to analyze the stack frame\n");
    printf("b <function_name>\n");
    printf("b phase1 - will set a break on the first challenge\n");
    printf("b *<memory address> - will break on addresses when we analyze phase 1\n");
    printf("placing a breakpoint on all the phases would be ideal for the tutorial\n");
    printf("---------------------------------------\n");
}

bool phase1(unsigned long guess){
    unsigned long num1 = 0xf010240;
    unsigned long num2 = 0x0404003;
    unsigned long num3 = num1 ^ num2;
    return (guess == num3);
}

char* hexify(char* string){
      char letter[100];
      char* word = malloc(sizeof(1919));
      int i;
      for (i=0; i<strlen(string); i++) {
          sprintf(letter, "%x",string[i]);
          strcat(word,letter);
       }
      return word;
}

bool phase2(char*  guess) {
    int i;

    if ((strlen(guess)) == 7){
        for (i=0;i<6;i++){
            if (guess[i] == '6'){
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
    return false;
}

bool phase3(char* guess) {
    if (strlen(guess) != 8){
        return false;
    }
    if ((guess[1] == 'Y') && (guess[4] == 'S')){
        return ((guess[0] == 'r') && (guess[2] == 'a') && (guess[3] == 'n') &&
                (guess[5] == 'u') && (guess[6] == 'x'));
    }

}

char* enter_flag(char* message){
    printf("-------------------------\n");
    printf("%s\n", message);
    char* flag;
    flag = malloc(sizeof(17568));
    fgets(flag,17658,stdin);
    return flag;
  }

int main(){
    char* message = "What string will make phase one true??\n";
    char* message2 = "What number will make phase two true??\n";
    char* message3 = "What string will make phase three true??\n";
    begin();
    explanation1();
    printf("ENTER TO CONTINUE\n");
    char* flag = malloc(sizeof(17568));
    fgets(flag,17658,stdin);
    explanation2();
    printf("Start of phase1\n");
    char* number = enter_flag(message);
    unsigned long num = strtoll(number,NULL,16);
    printf("info locals -will allow you to see the local variables\n");
    printf("i stack -will allow you to view the local stack frame\n");
    printf("anything interesting??\n");
    while (!(phase1(num))){
        printf("up, down, frame will help traversing the stack");
        number = enter_flag(message);
        num = strtoll(number,NULL,16);
        printf("x/d <element> will allow you to convert an element into decimal\n");
        printf("x/c <element> -displays char versions of elements\n");
    }
    printf("yaay you have 1/3 of the flag!!\n");
    printf("---------------------------------------\n");
    printf("start of phase2!!\n");
    printf("let's use what we already know and step through the stack frame\n");
    printf("n - steps through the stack frame an address at a time\n");
    printf("it seems like phase2 is converting your input into hex\n");
    char* number2 = enter_flag(message2);
    while (!(phase2(number2))){
        printf("b *<memory_address> will get you the value in an address\n");
        printf("info args -will help you view function arguments");
        printf("tbreak - will set a temporary breakpoint\n");
        number2 = enter_flag(message2);
    }
    printf("yaaaay you have 2/3 of the flag\n");
    char* number3 = enter_flag(message3);
    printf("ENTER TO CONTINUE\n");
    char* flag2 = malloc(sizeof(17568));
    fgets(flag2,17658,stdin);
    printf("this is the start of phase3\n");
    printf("---------------------------------------\n");
    printf("strings -literally prints out strings\n");
    while (!(phase3(number3))){
        printf("using strings,and i stack, along with a breakpoint should help you\n");
        printf("man gdb is also a great resource in terminal\n");
        number3 = enter_flag(message3);
    }
    printf("you have the flag!!!!!");
    printf("---------------------------------------\n");
    char* number1_s = malloc(sizeof("                       "));
    strncpy(number1_s,number,strlen(number)-1);
    char* number2_s = malloc(sizeof"                   ");
    strncpy(number2_s,number2,strlen(number2)-1);
    char* number3_s = malloc(sizeof("                     "));
    strncpy(number3_s,number3,strlen(number3)-1);
    printf("a format example would be flag{%s%s%s}",number1_s,number2_s,number3_s);
    printf("\n");
    return 0;
}
