#include<iostream>

struct Stack {
	int data;
	Stack* next;
};

Stack* Push(int x, Stack* head) {
	Stack* temp = new Stack;
	temp->data = x;
	temp->next = head;
	head = temp;

	return head;
}

Stack* Pop(Stack* head) {
	Stack* old;
	old = head;
	head = old->next;
	delete[] old;

	return head;
}

void Top(Stack* head) {
	std::cout << head->data << std::endl;
}

void IsEmpty(Stack* head) {
	std::cout << (head == NULL) << std::endl;
}

void PrintList(Stack* head) {
	Stack* walker = head; // temp variable for clarity
	while(walker != NULL) {
		std::cout << walker->data << " ";
		walker = walker->next;
	}
	std::cout << "\n";
}

int main() {
	Stack* head = NULL;
	head = Push(5, head);
	head = Push(7, head);
	IsEmpty(head);
	Top(head);
	PrintList(head);
	head = Pop(head);
	head = Pop(head);
	IsEmpty(head);
}
