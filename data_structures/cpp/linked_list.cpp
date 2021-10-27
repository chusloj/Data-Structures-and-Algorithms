#include<iostream>
#include<cassert>

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

Node* InsertAtPosition(int x, int pos, Node* head) {
	Node* temp = new Node;
	temp->data = x;
	temp->next = NULL;
	Node* walker = head;
	for(int i = 0; i < pos-2; i++) {
		walker = walker->next;
	}
	std::cout << "walker data at position " << pos-1 << ": " << walker->data << std::endl;
	temp->next = walker->next;
	walker->next = temp;
	return head;
}

Node* DeleteAtPosition(int pos, Node* head) {
	Node* walker = head;
	Node* walker_after;
	if(pos == 1) {
		head = walker->next;
		delete[] walker;
		return head;
	}
	for(int i = 0; i < pos-2; i++) {
		walker = walker->next;
	}
	walker_after = walker->next;
	walker->next = walker_after->next;
	delete[] walker_after;
	return head;
}

Node* ReverseListIterative(Node* head) {
	Node* walker = head;
	Node* walker_behind = NULL;
	Node* walker_front;
	while(walker != NULL) {
		walker_front = walker->next;
		walker->next = walker_behind;
		walker_behind = walker;
		walker = walker_front;
	}
	head = walker_behind;
	return head;
}

void PrintList(Node* head) {
	Node* walker = head; // temp variable for clarity
	while(walker != NULL) {
		std::cout << walker->data << " ";
		walker = walker->next;
	}
	std::cout << "\n";
}

int main() {
	Node* head = NULL; // initialize pointer to NULL
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

	head = InsertAtPosition(11, 3, head);
	PrintList(head);

	head = DeleteAtPosition(1, head);
	PrintList(head);

	head = InsertAtBeginning(2, head);
	head = InsertAtBeginning(3, head);
	head = InsertAtBeginning(9, head);
	PrintList(head);

	Node* head2 = ReverseListIterative(head);
	std::cout << "\n";
	PrintList(head2);

	assert(head==ReverseListIterative(head2));
	std::cout << "Assert true: The list is the same as the reversal of the reversed list.";

}
