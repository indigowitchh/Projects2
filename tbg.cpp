#include<iostream>
using namespace std;

int main() {
	int room = 1;
	char choice;

	cout << "Welcome to the text based game!" << endl;
	do {
		switch (room) {
		case 1:
			cout << "You are in room 1. You can go (n)orth." << endl;
			cin >> choice;
			if (choice == 'n')
				room = 2;
			else
				cout << "I don't understand that." << endl;
			break;
		case 2:
			cout << "You are in room 2. You can go (n)orth, (e)ast, (w)est, (s)outh." << endl;
			cin >> choice;
			if (choice == 'n')
				room = 5;
			else if (choice == 'e')
				room = 4;
			else if (choice == 'w')
				room = 3;
			else if (choice == 's')
				room = 1;
			else
				cout << "I don't understand that." << endl;
			break;
		case 3:
			cout << "You are in room 3. You can go (e)ast." << endl;
			cin >> choice;
			if (choice == 'e')
				room = 2;
			else
				cout << "I don't understand that." << endl;
			break;
		case 4:
			cout << "You are in room 4. You can go (w)est." << endl;
			cin >> choice;
			if (choice == 'w')
				room = 2;
			else
				cout << "I don't understand that." << endl;
			break;
		case 5:
			cout << "You are in room 5. You can go (s)outh." << endl;
			cin >> choice;
			if (choice == 's')
				room = 2;
			else
				cout << "I don't understand that." << endl;
			break;
		}
	} while (choice != 'q');
}
