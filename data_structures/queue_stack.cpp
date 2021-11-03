#include<iostream>

#define MAX_SIZE 101

class Queue {
private:
	int front = -1;
	int rear = -1;
	int arr[MAX_SIZE];
public:
	void Enqueue(int x);
	void Dequeue();
	int Front();
	bool IsEmpty();
	void Print();
};

void Queue::Enqueue(int x) {
	if(IsEmpty()) {
		front = rear = 0;
	}
	else {
		rear = (rear+1)%MAX_SIZE;
	}
	arr[rear] = x;
}

void Queue::Dequeue() {
	if(front == rear){
		front = rear = -1;
	}
	else {
		front = (front+1)%MAX_SIZE;
	}
}

int Queue::Front() {
	return arr[front];
}

bool Queue::IsEmpty() {
	return (front == -1 && rear == -1);
}

void Queue::Print() {
	for(int i = front; i < rear + 1; i++){
		std::cout << arr[i] << " ";
	}
	std::cout << "\n";
}

int main() {
	Queue Q;
	Q.Enqueue(4);
	Q.Enqueue(6);
	Q.Enqueue(9); Q.Print();
	Q.Dequeue(); Q.Print();
	std::cout << Q.IsEmpty() << std::endl;
	std::cout << Q.Front() << std::endl;
	Q.Dequeue(); Q.Print(); 
	Q.Dequeue();
	std::cout << Q.IsEmpty() << std::endl;
}