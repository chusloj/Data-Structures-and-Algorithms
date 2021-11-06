#include<iostream>
#include<queue>

struct Node {
	char data;
	Node* left;
	Node* right;
};

Node* GetNewNode(int x) {
	Node* newNode = new Node;
	newNode->data = x;
	newNode->left = newNode->right = NULL;
	return newNode;
}

Node* Insert(Node* root, char c) {
	if(root == NULL) {
		root = GetNewNode(c);
	}
	else if(c <= root->data) {
		root->left = Insert(root->left, c);
	}
	else {
		root->right = Insert(root->right, c);
	}
	return root;
}

void PreOrder(Node* root) {
	if(root == NULL) {
		return;
	}
	std::cout << root->data << std::endl;
	PreOrder(root->left);
	PreOrder(root->right);
}

void InOrder(Node* root) {
	if(root == NULL) {
		return;
	}
	std::cout << root->data << std::endl;
	InOrder(root->left);
	InOrder(root->right);
}

int main() {
	Node* root = NULL;
	root = Insert(root, 'F');
	root = Insert(root, 'D');
	root = Insert(root, 'J');
	root = Insert(root, 'B');
	root = Insert(root, 'E');
	root = Insert(root, 'G');
	root = Insert(root, 'K');
	
}