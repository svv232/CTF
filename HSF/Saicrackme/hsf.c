#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void print_art(){
    FILE* file = fopen("header.txt", "r");
    char line[300];

    while (fgets(line, sizeof(line), file)) {
        printf("%s",line);
    }
    printf("\n");
    fclose(file);
}

void YEEEEEEEEEEEEEEEEEEEEEHAAAAAAAAAAAA(){
    printf("YEEEEEEEEEEEEEEEEEHAAAAAAAAAAAAA\n");
    printf("ENTER THE STRING IN FLAG FORMAT!!!!!!!\n");
    printf("EXAMPLE: flag{password}\n");
    exit(0);
}


void incorrect_password(){
    printf("************************************\n\n\n");
    printf("Sorry fam give it another go!!!!!!!\n");
    printf("\n\n\n************************************\n");
    exit(0);
}

char* enter_flag(){
    printf("-------------------------\n");
    printf("PLEASE ENTER THE PASSWORD: \n");
    char* flag;
    flag = malloc(sizeof(17568));
    fgets(flag,17658,stdin);
    return flag;
}

int test1(const char* flag){
    int value;
    int* special;
    special = &value;
    char* special_size = "902876702156f";
    (*special) = strlen(special_size);
    if (strlen(flag)  == value) {
        return 1;
    }
    else {
        return 0;
    }
}

int test2(char* string_hex){
    int key = 0x746974;
    unsigned long special_num = strtoll(string_hex,NULL,16);
    if ((special_num ^ key) == 0x3665745815f40) {
        return 1;
    }
    else {
        incorrect_password();
    }
}

char* string_to_hex(char* string){
    char letter[100];
    char* word = malloc(sizeof(1919));
    int i;
    for (i=0; i<strlen(string); i++) {
        sprintf(letter, "%x",string[i]);
        strcat(word,letter);
     }
    return word;
}

int test3(char* hex){
    int key =  0x72696b;
    unsigned long special_num = strtoll(hex,NULL,16);
    if ((special_num & key) == 0x626049){
        return 1;
    }
    else {
        return 0;
    }
}

int test4(char* hex){
    int key =  0x72696b;
    unsigned long special_num = strtoll(hex,NULL,16);
    if ((special_num || key) == 0x6786732){
        return 1;
    }
    else {
        return 0;
    }

}
int main() {
    print_art();
    char* flag = enter_flag();
    char* hex = string_to_hex(flag); //string splitting of pointer??
    char* hex_9 = malloc(sizeof("12345678910111213"));
    char* hex_end = malloc(sizeof("2ewewiie3453543"));
    strncpy(hex_9,hex,13);
    strcpy(hex_end,hex+13);

    if ((test1(flag)) || test4(hex)){
        if (test3(hex_9)){
            return test2(hex_9);
        }
        else {
            if (test2(hex_9) && test3(hex_end)){
                YEEEEEEEEEEEEEEEEEEEEEHAAAAAAAAAAAA();    
            }
            
        }
    }
    else if (test3(hex_9)) {
        incorrect_password();
    }
    else {
        printf("WHAAA\n");
        incorrect_password();
        }
    return 0;
}
