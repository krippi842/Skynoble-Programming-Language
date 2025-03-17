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
        sudo apt update && sudo apt install -y build-essential clang cmake git python3 python3-pip
    elif [[ "$PLATFORM" == "Mac" ]]; then
        brew install clang cmake git python3
    elif [[ "$PLATFORM" == "Windows" ]]; then
        choco install llvm cmake git python
    else
        echo "Unsupported OS: $PLATFORM"
        exit 1
    fi
}

# Clone and Build Skynoble Compiler
build_skynoble() {
    echo "Cloning Skynoble repository..."
    git clone https://github.com/VioletAuraCreations/Skynoble.git ~/Skynoble
    cd ~/Skynoble
    echo "Building Skynoble Compiler..."
    mkdir -p build && cd build
    cmake .. && make -j$(nproc || sysctl -n hw.logicalcpu || echo 2)
    echo "Skynoble Compiler built successfully!"
}

# Setup Environment Variables
configure_environment() {
    echo "Configuring Environment..."
    SKYNOBLE_PATH="$HOME/Skynoble/build/skynoble"
    echo "export PATH=\"$SKYNOBLE_PATH:\$PATH\"" >> ~/.bashrc || ~/.zshrc
    source ~/.bashrc || source ~/.zshrc
    echo "Skynoble added to PATH."
}

# Run Setup
install_dependencies
build_skynoble
configure_environment

echo "Skynoble Setup Complete! Run 'skynoble --version' to verify installation."
