#!/bin/bash
# Skynoble Ultimate Setup Script
# Automatically installs dependencies, sets up the compiler, and configures the environment

set -e  # Exit on error

# Detect OS
echo "Detecting Operating System..."
OS="$(uname -s)"

case "$OS" in
    Linux*)   PLATFORM="Linux";;
    Darwin*)  PLATFORM="Mac";;
    CYGWIN*|MINGW32*|MSYS*|MINGW*) PLATFORM="Windows";;
    *)        PLATFORM="UNKNOWN";;
esac

echo "Detected Platform: $PLATFORM"

# Install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    if [[ "$PLATFORM" == "Linux" ]]; then
        sudo apt update && sudo apt install -y build-essential cmake git python3 python3-pip nasm
    elif [[ "$PLATFORM" == "Mac" ]]; then
        brew install cmake git python3 nasm
    elif [[ "$PLATFORM" == "Windows" ]]; then
        echo "Installing dependencies via Chocolatey..."
        choco install -y nasm cmake git python visualstudio2022buildtools
    else
        echo "Unsupported OS: $PLATFORM"
        exit 1
    fi
}

# Clone and Build Skynoble Compiler
build_skynoble() {
    echo "Cloning Skynoble repository..."
    git clone https://github.com/VioletAuraCreations/Skynoble.git ~/Skynoble || { echo "Failed to clone repository."; exit 1; }
    cd ~/Skynoble

    echo "Building Skynoble Compiler..."
    mkdir -p build && cd build

    if [[ "$PLATFORM" == "Windows" ]]; then
        cmake .. -G "Visual Studio 17 2022" -DCMAKE_ASM_NASM_COMPILER="nasm"
        cmake --build . --config Release
    else
        cmake .. -DCMAKE_ASM_NASM_COMPILER="nasm"
        make -j$(nproc || sysctl -n hw.logicalcpu || echo 2)
    fi

    echo "Skynoble Compiler built successfully!"
}

# Setup Environment Variables
configure_environment() {
    echo "Configuring Environment..."
    SKYNOBLE_PATH="$HOME/Skynoble/build/skynoble"

    if [[ "$PLATFORM" == "Windows" ]]; then
        SKYNOBLE_PATH_WIN="$(cygpath -w $SKYNOBLE_PATH)"
        echo "Adding Skynoble to PATH (Windows)..."
        setx PATH "$SKYNOBLE_PATH_WIN;%PATH%" /M
    else
        SHELL_PROFILE="$HOME/.bashrc"
        [[ -f "$HOME/.zshrc" ]] && SHELL_PROFILE="$HOME/.zshrc"
        echo "export PATH=\"$SKYNOBLE_PATH:\$PATH\"" >> "$SHELL_PROFILE"
        source "$SHELL_PROFILE"
    fi

    echo "Skynoble added to PATH."
}

# Run Setup
install_dependencies
build_skynoble
configure_environment

echo "Skynoble Setup Complete! Run 'skynoble --version' to verify installation."
