#include<iostream>

#define MAX_SIZE 100

class Stack {
private:
	int A[MAX_SIZE];
	int top = -1;
public:
	void Push(int x);
	void Pop();
	int Top();
	char TopChar();
	void IsEmpty();
};

void Stack::Push(int x) {
	if(top == MAX_SIZE - 1) {
		std::cout << "error: stack overflow";
		return;
	}
	top = top + 1;
	A[top] = x;
}

void Stack::Pop() {
	top = top - 1;
}

int Stack::Top() {
	return A[top];
}

char Stack::TopChar() {
	return A[top];
}

void Stack::IsEmpty() {
	std::cout << (top == -1) << std::endl;
}

char* Reverse(char *C, int l) {
	Stack s;
	int temp;
	for(int i = 0; i < l; i++) {
		s.Push(C[i]);
	}
	for(int i = 0; i < l; i++) {
		C[i] = s.TopChar();
		s.Pop();
	}
	return C;
}

int main() {
	Stack s;
	s.Push(5);
	s.Push(7);
	std::cout << s.Top() << std::endl;
	s.Pop();
	s.Pop();
	s.IsEmpty();

	// Reversal of string
	int l = 6;
	char C[l] = "string";
	std::cout << C << std::endl;
	
	char* C2 = Reverse(C, l);
	std::cout << C2;
}