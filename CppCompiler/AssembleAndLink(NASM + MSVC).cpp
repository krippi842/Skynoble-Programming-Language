void compileExecutable() {
    // Assemble with NASM
    system("nasm -f win64 output.asm -o output.obj");

    // Link with MSVC (cl.exe)
    system("link /subsystem:console /entry:main output.obj kernel32.lib /OUT:output.exe");
}
