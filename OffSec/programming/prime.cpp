#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>

using namespace std;

int recieve_num(){
    int num;
    cin >> num;
    return num;
}

void sieve(int n) {
    int root_n = (int)sqrt((double)n);
    bool *not_prime = new bool[n+1];
    memset(not_prime, 0,sizeof(bool) * (n + 1));
    for (int m =2; m <= root_n; m++){
        if (!not_prime[m]){
            cout << m << " ";
            for (int k = (m * m); k <=n; k += m)
                not_prime[k] = true;                
        }
    }

    for (int m=root_n; m<=n; m++)
        if (!not_prime[m])
            cout << m << " ";
    delete [] not_prime;
    cout << "\n";
}

int main(){
    int nth = recieve_num();
    sieve(nth);
}
