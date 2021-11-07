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

BstNode* Find(BstNode* root, int y) {
	if(root == NULL) {return NULL;}
	else if(root->data == y) {return root;}
	else if(y <= root->data) {return Find(root->left, y);}
	else {return Find(root->right, y);}
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

BstNode* GetSuccessor(BstNode* root, int data) {
	// search for the node
	BstNode* current = Find(root, data);
	if(current == NULL) {
		return NULL;
	}
	// Case 1: Node has right subtree
	if(current->right != NULL) {
		return FindMin(current->right);
	}
	// Case 2: Node does not have right subtree
	else {
		BstNode* successor = NULL;
		BstNode* ancestor = root;
		while(ancestor != current) {
			if(current->data < ancestor->data) {
				successor = ancestor;
				ancestor = ancestor->left;
			}
			else {
				ancestor = ancestor->right;
			}
		}
		return successor;
	}

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

	BstNode* scsr;

	scsr = GetSuccessor(root, 6);
	std::cout << scsr->data << std::endl;

	scsr = GetSuccessor(root, 8);
	std::cout << scsr->data << std::endl;

	scsr = GetSuccessor(root, 9);
	std::cout << scsr->data << std::endl;
}
