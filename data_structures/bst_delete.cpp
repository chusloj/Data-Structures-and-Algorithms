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

BstNode* FindMin(BstNode* root) {
	if(root == NULL) {
		return root;
	}
	while(root->left != NULL) {
		root = root->left;
	}
	return root;
}

BstNode* Delete(BstNode* root, int x) {
	if(root == NULL) {
		return root;
	}
	else if(x < root->data) {
		root->left = Delete(root->left, x);
	}
	else if(x > root->data) {
		root->right = Delete(root->right, x);	
	}
	else // "then you are only meant for one thing...deletion." - The Matrix Reloaded
	{
		// Case 1: no child
		if(root->left == NULL && root->right == NULL) {
			delete[] root;
			root = NULL;
		}

		// Case 2: one child
		else if(root->left == NULL) {
			BstNode* temp = root;
			root = root->right;
			delete[] temp;
		}
		else if(root->right == NULL) {
			BstNode* temp = root;
			root = root->left;
			delete[] temp;
		}

		// Case 3: 2 children
		else {
			BstNode* temp = FindMin(root->right);
			root->data = temp->data;
			root->right = Delete(root->right, temp->data);
		}
	}
	return root;
}

bool Search(BstNode* root, int y) {
	if(root == NULL) {return false;}
	else if(root->data == y) {return true;}
	else if(y <= root->data) {return Search(root->left, y);}
	else {return Search(root->right, y);}
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

	std::cout << Search(root, 6) << std::endl;

	root = Delete(root, 6);

	std::cout << Search(root, 6) << std::endl;
}
