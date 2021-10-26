#include<iostream>

struct Node {
	int data;
	Node* next;
};

// global variable(s)
// Node* head;

Node* InsertAtBeginning(int x, Node* head) {
	Node* temp = new Node;
	temp->data = x;
	if(head != NULL) {
		temp->next = head;
	}
	// temp->next = head; // shorthand that covers the case when list is empty
	head = temp;
	return head;
}

void PrintList(Node* head) {
	Node* walker = head; // temp variable for clarity
	while(walker != NULL) {
		std::cout << walker->data << " ";
		walker = walker->next;
	}
}

int main() {
	Node* head = NULL; // initialize pointer to nULL
	int x;
	std::cout << "Insert a number" << std::endl;
	std::cin >> x;
	head = InsertAtBeginning(x, head);
	PrintList(head);

	std::cout << "\n";

	std::cout << "Insert a number" << std::endl;
	std::cin >> x;
	head = InsertAtBeginning(x, head);
	PrintList(head);
}