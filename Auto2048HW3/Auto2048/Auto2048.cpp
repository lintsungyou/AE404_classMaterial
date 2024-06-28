// Auto2048.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<iomanip>
#include<fstream>
#include <stack>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
using namespace std;

const bool MANUAL_CONTROL = false;
const bool DEBUG_DISPLAY = true;
const bool DEBUG_SHOW_CHOICE = true;
const bool DEBUG_RECORD_PYOUTPUT = true;
const int ITERATION = 1;
const int DELAY_MS = 500;

const string MAP_FILE_NAME = "MAPFILE.txt";

//total score
int score = 0;
//to set max limit on no. of times undo can be performed
int undo_limit = 0;
//variable which stores score made in previous move, used to reduce the total score
//in case undo choice is selected
int undo_score = 0;
class play {
	stack<vector<vector<int> > > undo_stack;
	stack<int> score_stack;  
	std::vector<int> score_record;

	int g[4][4];
	int g_copy[4][4];
	void initialize();
	void display();
	void writeMapScoreToFile(const string& _fileName);
	void move_up();
	void move_down();
	void move_left();
	void move_right();
	int check_full();
	int random_index(int x);
	void sum_up();
	void sum_down();
	void sum_left();
	void sum_right();
	void generate_new_index();
	int calculate_max();
	void instructions();
	int game_ends();
	void end_display();
	void win_display(int&);
	void lose_display(int&);
	void restart();
	void readStepFromFile(const string& strategyPy, const string& stepsFile, char& choice);

public:
	void play_game();
	play() {
		// intialize undo stack

	}
};

void play::instructions() {
	cout << "\nInstructions for playing 2048 are:: \n" << endl;
	cout << "For moving tiles enter \nw-move up\na-move left\nd-move right\ns-move down\n" << endl;
	cout << "When two tiles with same number touch, they merge into one. \nWhen 2048 is created, the player wins!\n" << endl;
	// cout<<"please don't try to undo consecutively\n\n";
	cout << "maximum 5 undo operations are supported\n";
}

int play::random_index(int x) {
	int index;
	index = rand() % x + 0;
	return index;
}

void play::lose_display(int& iter_remain) {
	cout << "\t\t\tGAME OVER\n\n";
	cout << "Your final score is " << score << "\n\n";
	score_record.push_back(score);
	cout << "Thanks for trying!!!\n\n";
	if ((!MANUAL_CONTROL) && iter_remain > 0)
	{
		iter_remain--;
		restart();
	}
	else
		exit(0);
}

void play::restart() {
	char ch;
	if (MANUAL_CONTROL) {
		cout << "\nAre you sure to restart the game??\n\n";
		cout << "enter y to restart and n to continue.\n\n";
		cin >> ch;
		if (!(ch == 'y')) {
			return;
		}
	}
	score = 0;
	undo_score = 0;
	undo_stack = stack<vector<vector<int> > >();
	score_stack = stack<int>();
	initialize();
	
}

int play::check_full() {
	int full_flag = 1;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (g[i][j] == 0) {
				full_flag = 0;
				break;
			}
		}
	}
	return full_flag;
}

void play::win_display(int& iter_remain) {
	char ch;
	cout << "\t\t\tYOU WON!!!\n\n";
	cout << "Your total score is " << score << "\n\n";
	score_record.push_back(score);
	if ((!MANUAL_CONTROL) && iter_remain > 0)
	{
		iter_remain--;
		restart();
	}
	else if(MANUAL_CONTROL) {
		cout << "Do you wish to continue???\n";
		cout << "Enter y to continue and n to quit\n\n";
		cin >> ch;
		if (ch == 'n') {
			end_display();
		}
	}
	else {

	}
	
}

int play::calculate_max() {
	int i, j;
	int max = 0;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (g[i][j] > max) {
				max = g[i][j];
			}
		}
	}
	return max;
}

void play::end_display() {
	cout << "\nYour final score is :: " << score << endl << endl;
	cout << "Thanks for trying!!!\n\n";
	cout << "Good Bye!!!\n" << endl;
	exit(0);
}

int play::game_ends() {
	int i, j, flag = 1;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 3; j++) {
			if (g[i][j] == g[i][j + 1]) {
				flag = 0;
				break;
			}
		}
		if (flag == 0) {
			break;
		}
	}
	if (flag == 1) {
		for (i = 0; i < 3; i++) {
			for (j = 0; j < 4; j++) {
				if (g[i][j] == g[i + 1][j]) {
					flag = 0;
					break;
				}
			}
			if (flag == 0) {
				break;
			}
		}
	}
	return flag;
}


void play::generate_new_index() {
	int flag = 1;
	if (!check_full()) {
		while (flag) {
			int i = random_index(4);
			int j = random_index(4);
			if (g[i][j] == 0) {
				int y = rand() % 10 + 0;
				if (y < 6) {
					g[i][j] = 2;
				}
				else {
					g[i][j] = 4;
				}
				flag = 0;
			}
		}
	}
}

/*
	* initialize the matrices g and g_copy
	* two of the indices to value = 2 and other values to 0
*/
void play::initialize() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			g[i][j] = 0;
			g_copy[i][j] = 0;
		}
	}
	int i = random_index(4);
	int j = random_index(4);
	g[i][j] = 2;
	i = random_index(4);
	j = random_index(4);
	g[i][j] = 2;
	display();
}


void play::move_up() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (!g[j][i]) {
				for (int k = j + 1; k < 4; k++) {
					if (g[k][i]) {
						g[j][i] = g[k][i];
						g[k][i] = 0;
						break;
					}
				}
			}
		}
	}
}

void play::move_down() {
	for (int i = 0; i < 4; i++) {
		for (int j = 3; j >= 0; j--) {
			if (!g[j][i]) {
				for (int k = j - 1; k >= 0; k--) {
					if (g[k][i]) {
						g[j][i] = g[k][i];
						g[k][i] = 0;
						break;
					}
				}
			}
		}
	}
}

void play::move_left() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (!g[i][j]) {
				for (int k = j + 1; k < 4; k++) {
					if (g[i][k]) {
						g[i][j] = g[i][k];
						g[i][k] = 0;
						break;
					}
				}
			}
		}
	}
}

void play::move_right() {
	for (int i = 0; i < 4; i++) {
		for (int j = 3; j >= 0; j--) {
			if (!g[i][j]) {
				for (int k = j - 1; k >= 0; k--) {
					if (g[i][k]) {
						g[i][j] = g[i][k];
						g[i][k] = 0;
						break;
					}
				}
			}
		}
	}
}

void play::sum_up() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 3; j++) {
			if (g[j][i] && g[j][i] == g[j + 1][i]) {
				g[j][i] = g[j][i] + g[j + 1][i];
				g[j + 1][i] = 0;
				score += g[j][i];
				//undo_score += g[j][i];
			}
		}
	}
}

void play::sum_down() {
	for (int i = 0; i < 4; i++) {
		for (int j = 3; j > 0; j--) {
			if (g[j][i] && g[j][i] == g[j - 1][i]) {
				g[j][i] = g[j][i] + g[j - 1][i];
				g[j - 1][i] = 0;
				score += g[j][i];
				//undo_score += g[j][i];
			}
		}
	}
}

void play::sum_left() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 3; j++) {
			if (g[i][j] && g[i][j] == g[i][j + 1]) {
				g[i][j] = g[i][j] + g[i][j + 1];
				g[i][j + 1] = 0;
				score += g[i][j];
				//undo_score += g[i][j];
			}
		}
	}
}

void play::sum_right() {
	for (int i = 0; i < 4; i++) {
		for (int j = 3; j > 0; j--) {
			if (g[i][j] && g[i][j] == g[i][j - 1]) {
				g[i][j] = g[i][j] + g[i][j - 1];
				g[i][j - 1] = 0;
				score = score + g[i][j];
				//undo_score += g[i][j];
			}
		}
	}
}


void play::readStepFromFile(const string& strategyPy, const string& stepsFile, char& choice)
{
	string pyStr = "python ";
	string straStr = pyStr + strategyPy;
	if (DEBUG_RECORD_PYOUTPUT)
		straStr = straStr + " > " + "py_DEBUG.temp";
	int result = system(straStr.c_str());
	if(DEBUG_DISPLAY)
		cout << "result:" << result << std::endl;
	if (DEBUG_RECORD_PYOUTPUT)
	{
		std::ifstream ifPyDebug("py_DEBUG.temp", std::ifstream::binary);
		std::string pyDebugStr = "";
		cout << "**From strategy.py **\n";
		while (std::getline(ifPyDebug, pyDebugStr))
		{
			cout << pyDebugStr << "\n";
		}
		cout << "**End of strategy.py **\n";
	}
	bool strategyFinish = false;
	std::ifstream ifSteps(stepsFile, std::ifstream::binary);


	while (!strategyFinish)
	{
		if (ifSteps)
		{
			ifSteps >> choice;
			if (DEBUG_SHOW_CHOICE)
				cout << "choice: " << choice << std::endl;
			ifSteps.close();
			std::ofstream clearSteps(stepsFile, std::ios::out | std::ios::trunc);
			clearSteps.close();

			strategyFinish = true;
		}

	}


}

void play::writeMapScoreToFile(const string& _fileName) {
	
	fstream fWrite;
	fWrite.open(_fileName, ios::trunc | ios::out);
	for (int i = 0; i < 4; i++) {
		if(i > 0)
			fWrite << "\n";
		for (int j = 0; j < 4; j++) {
			fWrite << g[i][j];
			if (j < 3)
				fWrite << "\t";
		}
	}
	fWrite << "\n" <<score;

	fWrite.flush();
	fWrite.close();
}

/*
	* function to take choice from user
	* and call functions accordingly
*/
void play::play_game() {
	int flag = 0;
	char choice, ch;
	int iter_remain = ITERATION;
	initialize();
	instructions();
	if(MANUAL_CONTROL)
		cin>>choice;
	else {
		writeMapScoreToFile(MAP_FILE_NAME);
		readStepFromFile("strategy1.py", "steps.txt", choice);
	}
		


	while ((choice == 'w' || choice == 'a' || choice == 's' || choice == 'd' || choice == 'q' || choice == 'i' || choice == 'r')) {
		
		vector<vector <int> > current_copy;
		current_copy.resize(4);
		for (int m = 0; m < 4; m++) {
			for (int n = 0; n < 4; n++) {
				current_copy[m].push_back(g[m][n]);
			}
		}
		

		// if(choice!='u'){
		// 	for(int m=0;m<4;m++){
		// 		for(int n=0;n<4;n++){
		// 			g_copy[m][n]=g[m][n];
		// 		}
		// 	}
		// }

		switch (choice) {
			//move up
		case 'w':
			//undo_score = 0;
			move_up();
			sum_up();
			move_up();
			generate_new_index();
			display();
			//score_stack.push(undo_score);
			break;
			//move down
		case 's':
			//undo_score = 0;
			move_down();
			sum_down();
			move_down();
			generate_new_index();
			display();
			//score_stack.push(undo_score);
			break;
			//move left
		case 'a':
			//undo_score = 0;
			move_left();
			sum_left();
			move_left();
			generate_new_index();
			display();
			//score_stack.push(undo_score);
			break;
			//move right
		case 'd':
			//undo_score = 0;
			move_right();
			sum_right();
			move_right();
			generate_new_index();
			display();
			//score_stack.push(undo_score);
			break;
			//quit
		case 'q':
			cout << "Are you sure you want to quit??\nEnter y to quit and n to continue!\n" << endl;
			cin >> ch;
			if (ch == 'y' || ch == 'Y') {
				end_display();
			}
			display();
			break;
			//display instructions
		case 'i':
			instructions();
			break;
			//restart 2048
		case 'r':
			restart();
			break;
			//undo move

		}
		std::this_thread::sleep_for(std::chrono::milliseconds(DELAY_MS));
		//check if any block of matrix reached to value = 2048
		int find_max = calculate_max();
		if (find_max == 2048) {
			win_display(iter_remain);
		}
		/*
			* check_full() checks if grid is full
			* game_ends() perform a check if continuous block in up-down or
			  right-left direction has same values
			* if no continuous block has same value, then no further move can be made
			  and game ends
		*/
		if (check_full()) {
			if (game_ends()) {
				lose_display(iter_remain);
				std::cout << "iter_remain" << iter_remain << std::endl;
			}
		}

		
		if (MANUAL_CONTROL)
			cin >> choice;
		else {
			writeMapScoreToFile(MAP_FILE_NAME);
			readStepFromFile("strategy1.py", "steps.txt", choice);
		}
			
		if(MANUAL_CONTROL || DEBUG_SHOW_CHOICE)
			cout << "enter choice: " << choice << endl;
		while (choice != 'w' && choice != 's' && choice != 'd' && choice != 'a' && choice != 'q' && choice != 'i' && choice != 'u' && choice != 'r') {
			cout << "\nYou had entered the wrong choice!\nPlease enter correct choice to continue!" << endl;
			cin >> choice;
		}
	}
}

/*
	* display function
	* called after every move
*/
void play::display() {

	if ((!DEBUG_DISPLAY) && (!MANUAL_CONTROL)) return;
	cout << "  score :: " << score << endl << endl;
	for (int i = 0; i < 4; i++) {
		cout << "                       ";
		for (int j = 0; j < 4; j++) {
			cout << setw(8) << g[i][j] << setw(8) << "|" << setw(8);
		}
		cout << endl << endl << endl;
	}

}



int main() {
	play p;
	srand(time(NULL));
	p.play_game();
	return 0;
}




// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file


