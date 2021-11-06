#include<iostream>
#include<climits>

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

bool IsBstUtil(BstNode* root, int minValue, int maxValue) {
	if(root == NULL) {
		return true;
	}

	if(root->data > minValue && root->data < maxValue
		&& IsBstUtil(root->left, minValue, root->data)
		&& IsBstUtil(root->right, root->data, maxValue)
		) {
		return true;
	}

	else {
		return false;
	}
}

bool IsBinarySearchTree(BstNode* root) {
	return IsBstUtil(root, INT_MIN, INT_MAX);
}


int main() {
	BstNode* root = NULL;
	root = Insert(root, 7);
	root = Insert(root, 4);
	root = Insert(root, 9);
	root = Insert(root, 1);
	root = Insert(root, 6);
	root = Insert(root, 8);
	root = Insert(root, 13);
	std::cout << IsBinarySearchTree(root) << std::endl;
}
