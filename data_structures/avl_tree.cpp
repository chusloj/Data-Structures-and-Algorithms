#include<iostream>

// https://www.programiz.com/dsa/avl-tree

struct AvlNode {
	int data;
	AvlNode* left;
	AvlNode* right;
};

AvlNode* GetNewNode(int x) {
	AvlNode* newNode = new AvlNode;
	newNode->data = x;
	newNode->left = newNode->right = NULL;

	return newNode;
}

int FindHeight(AvlNode* root) {
	if(root == NULL) {
		return -1;
	}
	int leftHeight = FindHeight(root->left);
	int rightHeight = FindHeight(root->right);

	return std::max(leftHeight, rightHeight) + 1;
}

int FindBalanceFactor(AvlNode* root) {
	if(root == NULL) {
		return 0;
	}
	int leftHeight = FindHeight(root->left);
	int rightHeight = FindHeight(root->right);

	int balance = leftHeight - rightHeight;
	return balance;
}

AvlNode* RightRotation(AvlNode* root) {
	AvlNode* rightChild = root->right;
	AvlNode* rightChildLeft = rightChild->left;

	rightChild->left = root;
	root->right = rightChildLeft;

	return rightChild;
}

AvlNode* LeftRotation(AvlNode* root) {
	AvlNode* leftChild = root->left;
	AvlNode* leftChildRight = leftChild->right;

	leftChild->right = root;
	root->left = leftChildRight;

	return leftChild;
}

AvlNode* InsertWithRotation(AvlNode* root, int x) {
	if(root == NULL) {
		root = GetNewNode(x);
		return root;
	}
	else if(x <= root->data) {
		root->left = InsertWithRotation(root->left, x);
	}
	else {
		root->right = InsertWithRotation(root->right, x);
	}

	int balanceFactor = FindBalanceFactor(root);

	if(balanceFactor > 1) {
		if(x <= root->left->data) {
			return RightRotation(root);
		}
		else if(x > root->left->data) {
			root->left = LeftRotation(root->left);
			return RightRotation(root);
		}
	}
	else if(balanceFactor < -1) {
		if(x > root->right->data) {
			return LeftRotation(root);
		}
		else if(x <= root->right->data) {
			root->right = RightRotation(root->right);
			return LeftRotation(root);
		}
	}

	return root;
}

void PrintTree(AvlNode* root, std::string indent, bool last) {
  if (root != NULL) {
    std::cout << indent;
    if (last) {
      std::cout << "R----";
      indent += "   ";
    } else {
      std::cout << "L----";
      indent += "|  ";
    }
    std::cout << root->data << std::endl;
    PrintTree(root->left, indent, false);
    PrintTree(root->right, indent, true);
  }
}


int main() {
	AvlNode* root = NULL;
	root = InsertWithRotation(root, 33);
	root = InsertWithRotation(root, 13);
	root = InsertWithRotation(root, 53);
	root = InsertWithRotation(root, 9);
	root = InsertWithRotation(root, 21);
	root = InsertWithRotation(root, 61);
	root = InsertWithRotation(root, 8);
	root = InsertWithRotation(root, 11);
	PrintTree(root, "", true);
	std::cout << FindBalanceFactor(root);
}

