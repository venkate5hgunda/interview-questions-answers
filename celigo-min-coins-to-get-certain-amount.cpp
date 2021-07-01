#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <climits>
using namespace std;

vector<int> coins;
int amount;
int min_coins;

void add_coin(int temp,int num_coins,int coin_value) {
    if(temp==amount) {
        min_coins = min(min_coins,num_coins);
    }
    else if(temp<amount) {
        for(int i=0;i<coins.size();i++) {
            add_coin(temp+coin_value,num_coins+1,coins[i]);
        }
    }
}

int main() {
    // Write C++ code here
    coins = {5,7,11};
    amount = 0;
    min_coins=INT_MAX;
    for(int i=0;i<coins.size();i++) {
        add_coin(0,0,coins[i]);
    }
    if(min_coins==INT_MAX) {
        cout << -1 << endl;
    }
    else {
        cout << min_coins << endl;
    }
    return 0;
}
