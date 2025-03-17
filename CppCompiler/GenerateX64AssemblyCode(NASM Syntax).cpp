void generateAssembly(const std::string& hexIR) {
    std::ofstream asmFile("output.asm");
    asmFile << "section .text\n";
    asmFile << "global main\n";
    asmFile << "extern ExitProcess\n";
    
    asmFile << "main:\n";
    
    // Translate Hex IR into NASM Assembly
    asmFile << "    " << "; Hex IR instructions: " << hexIR << "\n";
    
    // Exit cleanly
    asmFile << "    mov rcx, 0\n";  // Exit code 0
    asmFile << "    call ExitProcess\n";
    asmFile << "    ret\n";

    asmFile.close();
}
