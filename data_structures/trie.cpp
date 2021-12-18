#include <iostream>
#include <string>


struct TrieNode {
	char data;
	TrieNode* child[26];
	bool wordend;
};

TrieNode* GetNewNode(char c) {
	TrieNode* newNode = new TrieNode;
	newNode->data = c;
	for(int i = 0; i < 26; i++) {
		newNode->child[i] = NULL;
	}
	return newNode;
}


TrieNode* Insert(TrieNode* root, std::string s) {
	if(root == NULL) {
		root = GetNewNode(' ');
	}

	TrieNode* walker = root;
	for(int i = 0; i < s.size(); i++) {
		char c = s[i];
		int diff = c - 'a';
		if(walker->child[diff] == NULL) {
			walker->child[diff] = GetNewNode(c);
		}
		walker = walker->child[diff];
	}
	walker->wordend = true;

	return root;
}


bool Search(TrieNode* root, std::string s) {
	if(root == NULL) {
		return false;
	}

	TrieNode* walker = root;
	for(int i = 0; i < s.size(); i++) {
		char c = s[i];
		int diff = c - 'a';
		if(walker->child[diff] == NULL) {
			std::cout << "word not present" << std::endl;
			return false;
		}
		walker = walker->child[diff];
	}
	
	std::cout << "word found" << std::endl;
	return walker->wordend;
}


void PrintTrie(TrieNode* root) {
	if(root != NULL && root->data != ' ') {
		std::cout << root->data << std::endl;
	}

	for(int i = 0; i < 26; i++) {
		if(root->child[i] != NULL) {
			PrintTrie(root->child[i]);
		}
	}
}


int main() {
	TrieNode* root = NULL;
	root = Insert(root, "car");
	root = Insert(root, "call");
	Search(root, "car");
	Search(root, "cat");
	Search(root, "call");
	PrintTrie(root);
}
