#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	string x;
	int count = 0;
	fstream fcin;
	fcin.open("input", ios::in);
	fcin >> x;
	for (int i = 0; i < x.length(); i++) {
		if(x[i] == '(')
			count++;
		else 
			count--;
	}
	cout << count << "\n";
}
