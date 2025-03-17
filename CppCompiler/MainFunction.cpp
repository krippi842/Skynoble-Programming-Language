int main() {
    // Example Skynoble code
    std::string skynobleCode = "echo 'Hello, Windows NASM!'";

    // Tokenization
    auto tokens = tokenize(skynobleCode);

    // Parsing
    ASTNode* ast = parse(tokens);

    // Generate Hexadecimal IR
    std::string hexIR = generateHexIR(ast);

    // Generate Assembly (NASM)
    generateAssembly(hexIR);

    // Compile to Executable using NASM + MSVC
    compileExecutable();

    std::cout << "Compilation complete. Run 'output.exe' to execute." << std::endl;
    return 0;
}
