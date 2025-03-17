#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>

// Token structure
struct Token {
    std::string type;
    std::string value;
};

// Tokenizer function
std::vector<Token> tokenize(const std::string& code) {
    std::istringstream iss(code);
    std::vector<Token> tokens;
    std::string token;
    
    while (iss >> token) {
        if (token == "echo") {
            tokens.push_back({"PRINT", token});
        } else if (token == "cond") {
            tokens.push_back({"IF", token});
        } else {
            tokens.push_back({"IDENTIFIER", token});
        }
    }
    return tokens;
}

// AST Node structure
struct ASTNode {
    std::string type;
    std::string value;
    std::vector<ASTNode*> children;

    ASTNode(std::string t, std::string v) : type(t), value(v) {}
};

// Parser function
ASTNode* parse(const std::vector<Token>& tokens) {
    ASTNode* root = new ASTNode("PROGRAM", "");
    for (const auto& token : tokens) {
        root->children.push_back(new ASTNode(token.type, token.value));
    }
    return root;
}

// Convert AST to Hexadecimal IR
std::string generateHexIR(ASTNode* root) {
    std::ostringstream hexStream;
    for (const auto& node : root->children) {
        if (node->type == "PRINT") {
            hexStream << "48 89 E5 "; // MOV RBP, RSP
        } else if (node->type == "IF") {
            hexStream << "74 05 "; // JZ (Jump if Zero)
        }
    }
    return hexStream.str();
}
