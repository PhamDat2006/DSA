#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int num;
    cout << "Nhap so: ";
    cin >> num;
    if (isPrime(num))
        cout << num << " la so nguyen to" << endl;
    else
        cout << num << " khong phai so nguyen to" << endl;
    return 0;
}
