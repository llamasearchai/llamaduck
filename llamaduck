#!/usr/bin/env bash
# Llamaduck CLI wrapper script
# Makes it easy to run llamaduck commands without activating the venv manually

set -eo pipefail

# ANSI color codes for better UX
readonly RED='\033[1;31m'
readonly GREEN='\033[1;32m'
readonly YELLOW='\033[1;33m'
readonly CYAN='\033[1;36m'
readonly RESET='\033[0m'

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_DIR="$SCRIPT_DIR/.venv"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${RED}❌ Virtual environment not found at $VENV_DIR${RESET}"
    echo -e "${YELLOW}Please run the installation script first:${RESET}"
    echo -e "${CYAN}  ./install.sh${RESET}"
    exit 1
fi

# Check if llamaduck is installed
if ! source "$VENV_DIR/bin/activate" &>/dev/null || ! command -v llamaduck &>/dev/null; then
    echo -e "${RED}❌ Llamaduck command not found in virtual environment${RESET}"
    echo -e "${YELLOW}Please run the installation script to reinstall:${RESET}"
    echo -e "${CYAN}  ./install.sh${RESET}"
    exit 1
fi

# Activate virtual environment and run llamaduck with the provided arguments
echo -e "${GREEN}🦙 Running Llamaduck Pro...${RESET}"
source "$VENV_DIR/bin/activate"
llamaduck "$@" 