#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void tutorial(){
    cout << "gdb is a tool used to dynamically analyze binaries as I'm sure you know;" << endl << "it makes stepping through the stack frame and looking into memory addresses a little less worse." << endl << " It's useful for understanding why a program has segfaulted. It's greatly useful for general exploitation analysis as well." << endl;
}

void basics(){
    cout << "* gdb" << " is what to execute to enter the program through the command line" << endl;
    cout << "* gdb takes an executable as an argument" << endl;
    cout << "* gdb <executable>" << endl;
    cout << "* file <executable>-  " << "is also valid after you are in gdb" << endl;
}

void breakpoints() {
    cout << "* b <function_name> -will set a breakpoint at the start of the stack frame for that function" << endl <<  "b *<memory address>" << "- will show you what is in a particular address" << endl;

    cout << "* n - steps through the stack frame an address at a time" << endl;

    cout << "* i stack - allows for a visual representation of the stack frame" << endl;

    cout << "* x/x <element> -displays elements in hex" << endl;
    cout << "* x/d <element> -display elements as decimals" << endl;
    cout << "* x/c <element> -displays elements as chars " << "MAYBE  USEFUL FOR CONVERTING ELEMENTS INTO HEX"<< endl;
}

void some_tricks(){
    cout << "* strings" << "- prints all the strings used throughout the program, and can be useful for a place to start while exploiting or debugging" << endl;
}

void more_tricks(){
    
    cout << "* backtrace full- Complete backtrace with local variables" << endl << endl;
    cout << "* up, down, frame- Move through frames" << endl << endl;
    cout << "* watch: Suspend the process when a certain condition is met" << endl << endl;
    cout << "* set print pretty on- Prints out prettily formatted C source code" << endl << endl;
    cout << "* set logging on- Log debugging session to show to others for support" << endl << endl;
    cout << "* set print array on- Pretty array printing" << endl << endl;
    cout << "* finish- Continue till end of function" << endl << endl;
    cout << "* enable and disable- Enable/disable breakpoints" << endl << endl;
    cout << "* tbreak- Break once, and then remove the breakpoint" << endl << endl;
    cout << "* where- Line number currently being executed" << endl << endl;
    cout << "* info locals- View all local variables" << endl << endl;
    cout << "* info args- View all function arguments" << endl << endl;
    cout << "* list- view source" << endl << endl;
    cout << "* rbreak- break on function matching regular expression" << endl << endl;
}

void extra(){
    cout << "* extra info at 'man gdb' in terminal" << endl;
    cout << "* And when gdb gets to easy try out pwn debug !!" << endl;
}

int main(){
    string input_line;
    cout << endl << endl;
    cout << "**************************************************************" << endl;
    cout << endl;
    tutorial();
    cout << "**************************************************************" << endl;
    cout << "ENTER TO CONTINUE!" << endl;
    getline(cin,input_line);
    cout << endl;
    basics();
    cout << "**************************************************************" << endl;
    cout << "ENTER TO CONTINUE!" << endl;
    getline(cin,input_line);
        cout << "**************************************************************" << endl;
    cout << endl;
    breakpoints();
    cout << "**************************************************************" << endl; 
    cout << "ENTER TO CONTINUE!" << endl;
    getline(cin,input_line);
    cout << "**************************************************************" << endl; 
    cout << endl;
    some_tricks();
    cout << endl;
    cout << "ENTER TO CONTINUE!" << endl;
    getline(cin,input_line);
    cout << "**************************************************************" << endl;
    more_tricks();
    cout << endl;
    cout << "**************************************************************" << endl;
    cout << "ENTER TO CONTINUE!" << endl;
    getline(cin,input_line);
    extra();
    cout << endl;
    cout << "**************************************************************" << endl;
}
