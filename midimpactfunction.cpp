#include<iostream>
using namespace std;

float ReactMult(char attack, char type);


int main() {
	char input1, input2;
	char choice = 'a';
	while (choice != 'q') {
		cout << "enter two parameters:" << endl;
		cin >> input1;
		cin >> input2;
		//if input1 or input2 is 'q' then print goodbye and return 0
		if (input1=='q' || input2 == 'q') {
			cout << "Goodbye!" << endl;
			return 0;
		}
		cout << "function returns " << ReactMult(input1, input2) << endl<<endl;//function call
	}
}

float ReactMult(char attack, char type) {
	
	if ((attack != 'm') && (attack != 'v')) {
		cout << "Incorrect parameters for attack..." << endl;
		return -1;
	}
	else if (attack == 'm' || attack == 'v') {
		
	}

	if (type != 'p' && type != 'c' && type != 'h') {
		cout << "Incorrect parameters for type of attack..." << endl;
		return -1;
	}

	if (type == 'p' && attack == 'm') {
		return 2.0;
	}

	else if (type == 'c' && attack == 'm') {
		return 1.5;
	}

	else if (type == 'h' && attack == 'v') {
		return 2.0;
	}

	else if (type == 'p' && attack == 'v') {
		return 1.5;
	}

}
