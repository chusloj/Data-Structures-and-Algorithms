#include<iostream>

struct Queue {
	int data;
	Queue* next = NULL;
};

// global variables
Queue* head = NULL;
Queue* tail = NULL;

void Dequeue() {
	Queue* temp = head;
	if(head == NULL && tail == NULL) {
		return;
	}
	if(head == tail) {
		head = tail = NULL;
	}
	else {
		head = temp->next;
	}
	delete[] temp;
}

void Enqueue(int x) {
	Queue* temp = new Queue;
	temp->data = x;
	if(head == NULL && tail == NULL) {
		head = tail = temp;
		return;
	}
	tail->next = temp;
	tail = temp;
}

int Front() {
	return head->data;
}

bool IsEmpty() {
	return (head == NULL && tail == NULL);
}

void Print() {
	Queue* walker = head;
	while(walker != NULL) {
		std::cout << walker->data << " ";
		walker = walker->next;
	}
	std::cout << "\n";
}

int main() {
	Enqueue(6);
	std::cout << "head is : " << Front() << std::endl; 
	Enqueue(5); Print();
	Dequeue(); Print();
	std::cout << IsEmpty() << std::endl;
	std::cout << Front() << std::endl;
	Dequeue();
	std::cout << IsEmpty() << std::endl;
}
