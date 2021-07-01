#include <iostream>
#include <vector>
#include <list>
using namespace std;

int main() {
    // Write C++ code here
    vector<int> arr = {3,4,5,6,1,2};
    int pivot = arr[0];
    
    for(int i=1;i<arr.size();i++) {
        if(arr[i]<pivot) {
            int temp = arr[i];
            arr.erase(arr.begin()+i);
            arr.insert(arr.begin(),temp);
        }
    }
    
    for(int i=0;i<arr.size();i++) {
        cout << arr[i] << endl;
    }
    return 0;
}
