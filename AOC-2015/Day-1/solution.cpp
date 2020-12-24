#include <bits/stdc++.h>
using namespace std;

class Day1 {
	private:
		string floors;
		int count;

	public:
		Day1(string x) {
			floors = x;
		}

		void partOne() {
			count = 0;
			for(int i = 0; i < floors.length(); i++) {
				if(floors[i] == '(') {
					count++;
				} else {
					count--;
				}
			}

			cout << count << '\n';	
		}

		void partTwo() {
			count = 0;
			for(int i = 0; i < floors.length(); i++) {
				if(floors[i] == '(') {
					count++;
				} else {
					count--;
				}

				if(count == -1) {
					cout << i + 1 << '\n';
					break;
				}
			}
		}
};

int main()
{
	string x;
	fstream fcin;
	fcin.open("input", ios::in);
	fcin >> x;

	Day1 one(x);
	
	//Output the solution
	cout << "2015 Day 1 Part 1 Solution:" << '\n';
	one.partOne();
	cout << "2015 Day 1 Part 2 Solution:" << '\n';
	one.partTwo();
}
