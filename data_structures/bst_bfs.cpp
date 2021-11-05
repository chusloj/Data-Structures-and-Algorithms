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

void LevelOrder(Node* root) {
	if(root == NULL) {
		return;
	}
	std::queue<Node*> Q;
	Q.push(root);
	Node* current;
	while(!Q.empty()) {
		current = Q.front();
		std::cout << current->data << " ";
		if(current->left != NULL) {Q.push(current->left);}
		if(current->right != NULL) {Q.push(current->right);}
		Q.pop();
	}
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
	LevelOrder(root);
}