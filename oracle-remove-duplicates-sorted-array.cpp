#include <iostream>
using namespace std;

void remDup(int inArr[], int length) {
    int prev=0;
    for(int i=0;i<length;i++) {
      if(inArr[i]!=inArr[prev]) {
        inArr[++prev]=inArr[i];
      }
    }
    for(int i=prev+1;i<length;i++) {
      inArr[i]=-1;
    }
}

int main() {
  int intArr[] = {1,2,2,2,4,6,7,9};
  int arrLength = 8;
  int count=0;
  remDup(intArr, arrLength);
  for(int i=0;i<arrLength;i++) {
    cout << intArr[i] << endl;
  }
  return 0;
}
