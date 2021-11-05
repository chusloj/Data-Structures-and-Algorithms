#include<iostream>

struct BstNode {
	int data;
	BstNode* left;
	BstNode* right;
};

BstNode* GetNewNode(int x) {
	BstNode* newNode = new BstNode;
	newNode->data = x;
	newNode->left = newNode->right = NULL;
	return newNode;
}

// recursive approach
BstNode* Insert(BstNode* root, int x) {
	if(root == NULL) {
		root = GetNewNode(x);
	}
	else if(x <= root->data) {
		root->left = Insert(root->left, x);
	}
	else {
		root->right = Insert(root->right, x);
	}
	return root;
}

bool Search(BstNode* root, int y) {
	if(root == NULL) {return false;}
	else if(root->data == y) {return true;}
	else if(y <= root->data) {return Search(root->left, y);}
	else {return Search(root->right, y);}
}

int FindMin(BstNode* root) {
	if(root == NULL) {
		return -1;
	}
	while(root->left != NULL) {
		root = root->left;
	}
	return root->data;
}

int FindHeight(BstNode* root) {
	if(root == NULL) {
		return -1;
	}
	int leftHeight = FindHeight(root->left);
	int rightHeight = FindHeight(root->right);

	return std::max(leftHeight, rightHeight) + 1;
}


int main() {
	BstNode* root = NULL;
	root = Insert(root, 15);
	root = Insert(root, 10);
	root = Insert(root, 20);
	root = Insert(root, 25);
	root = Insert(root, 5);
	std::cout << Search(root, 25) << std::endl;
	std::cout << FindMin(root) << std::endl;
	std::cout << FindHeight(root) << std::endl;
}
