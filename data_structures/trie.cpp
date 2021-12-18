#include <iostream>

struct TrieNode {
	char data;
	TrieNode* child[26];
	// bool wordend;
};

TrieNode* GetNewNode(char s) {
	TrieNode* newNode = new TrieNode;
	newNode->data = s;
	for(int i = 0; i < 26; i++) {
		newNode->child[i] = NULL;
	}
	return newNode;
}

TrieNode* Insert(TrieNode* root, char s) {
	if(root == NULL) {
		root = GetNewNode(' ');
	}

	int diff = s - 'a';
	if(root->child[diff] == NULL) {
		root->child[diff] = GetNewNode(s);
	}

	TrieNode* walker = root->child[diff];

	return root;
}

void PrintTrie(TrieNode* root) {
	if(root != NULL) {
		std::cout << root->data << endl;
	}

	for(int i = 0; i < 26; i++) {
		if(root->child[i] != NULL) {
			PrintTrie(root->child[i]);
		}
	}
}

int main() {
	TrieNode* root = NULL;
	root = Insert(root, 'c');
	PrintTrie(root);
}
