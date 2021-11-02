#include<iostream>
#include<stack>
#include<string>

bool CheckBalance(std::string st, int l) {
	std::stack<char> k;
	for(int i = 0; i < l; i++) {
		if(st[i] == '(' || st[i] == '{') {
			k.push(st[i]);
			std::cout << st[i] << std::endl;
		}
		else if(st[i] == ')' || st[i] == '}') {
			if(k.empty()) {
				return false;
			}
			else if(st[i] == ')' && k.top() != '(') {
				return false;
			}
			else if(st[i] == '}' && k.top() != '{') {
				return false;
			}
			else {
				k.pop();
			}
		}
	}
	return k.empty();
}


int main() {
	int l = 8;
	std::string st ("()(()){}");
	std::cout << CheckBalance(st, l) << std::endl;
}