#include<iostream>
// Best practice is not to use namespace std

struct Node {
	int data;
	Node* link;
};

int main(){
	Node* A;
	A = NULL; // Null pointer

	Node* temp = new Node;
	temp->data = 2;
	temp->link = NULL;
	A = temp;

	// print results
	// std::cout << *A;
	std::cout << A->data << std::endl;
	std::cout << A->link;
}