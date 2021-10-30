#include<iostream>

struct Node {
	int data;
	Node* next;
	Node* prev;
};

Node* GetNewNode(int x) {
	Node* newNode = new Node;
	newNode->data = x;
	newNode->next = NULL;
	newNode->prev = NULL;
	return newNode;
}

Node* InsertAtHead(int x, Node* head) {
	Node* newNode = GetNewNode(x);
	if(head == NULL) {
		head = newNode;
		return head;
	}
	head->prev = newNode;
	newNode->next = head;
	head = newNode;
	return head;
}

Node* InsertAtTail(int x, Node* head) {
	Node* newNode = GetNewNode(x);
	if(head == NULL) {
		head = newNode;
		return head;
	}
	Node* walker = head;
	while(walker->next != NULL) {
		walker = walker->next;
	}
	walker->next = newNode;
	newNode->prev = walker;
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

void PrintListReverse(Node* head) {
	Node* walker = head; // temp variable for clarity
	while(walker->next != NULL) {
		walker = walker->next;
	}
	while(walker != NULL) {
		std::cout << walker->data << " ";
		walker = walker->prev;
	}
	std::cout << "\n";
}

int main() {
	Node* head = NULL; // initialize pointer to NULL
	int x;
	std::cout << "Insert a number" << std::endl;
	std::cin >> x;
	head = InsertAtHead(x, head);
	PrintList(head);

	std::cout << "\n";

	std::cout << "Insert a number" << std::endl;
	std::cin >> x;
	head = InsertAtHead(x, head);
	PrintList(head);

	std::cout << "\n";

	std::cout << "Insert a number" << std::endl;
	std::cin >> x;
	head = InsertAtTail(x, head);
	PrintList(head);

	std::cout << "\n";

	head = InsertAtHead(2, head);
	head = InsertAtHead(9, head);
	PrintList(head);

	PrintListReverse(head);

}
