#!/usr/bin/env bash
# LlamaDuck Pro Installer
# A professional installation script for the LlamaDuck Pro CLI tool

set -eo pipefail

# ANSI color codes for pretty output
readonly RED='\033[1;31m'
readonly GREEN='\033[1;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[1;34m'
readonly PURPLE='\033[1;35m'
readonly CYAN='\033[1;36m'
readonly GRAY='\033[0;37m'
readonly BOLD='\033[1m'
readonly RESET='\033[0m'

# Configuration
readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly VENV_DIR="$SCRIPT_DIR/.venv"
readonly MIN_PYTHON_VERSION="3.8.0"
readonly LOG_FILE="$SCRIPT_DIR/install.log"

# Create fresh log file
> "$LOG_FILE"

# =====================================================================
# Helper Functions
# =====================================================================

log() {
    local msg="[$(date +'%Y-%m-%d %H:%M:%S')] $1"
    echo -e "$msg" | tee -a "$LOG_FILE"
}

log_cmd() {
    local cmd="$1"
    log "${GRAY}Running: $cmd${RESET}"
    
    # Run command and capture output to log
    if output=$(eval "$cmd" 2>&1); then
        echo "$output" >> "$LOG_FILE"
        return 0
    else
        echo "$output" >> "$LOG_FILE"
        log "${RED}Command failed: $cmd${RESET}"
        return 1
    fi
}

print_header() {
    echo -e "\n${CYAN}${BOLD}$1${RESET}"
    echo -e "${CYAN}$(printf '=%.0s' $(seq 1 70))${RESET}\n"
}

print_success() {
    echo -e "\n${GREEN}✅ $1${RESET}\n"
}

print_error() {
    echo -e "\n${RED}❌ $1${RESET}\n"
    echo -e "${YELLOW}Check the log file for details: $LOG_FILE${RESET}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${RESET}"
}

print_step() {
    echo -e "${BLUE}→ $1${RESET}"
}

check_command() {
    if ! command -v "$1" &> /dev/null; then
        return 1
    fi
    return 0
}

check_python_version() {
    local python_cmd="$1"
    local required_version="$2"
    
    if ! check_command "$python_cmd"; then
        return 1
    fi
    
    local current_version
    current_version=$("$python_cmd" -c "import sys; print('.'.join(map(str, sys.version_info[:3])))")
    
    # Compare versions
    if python3 -c "
import sys
from packaging import version
current=version.parse('$current_version')
required=version.parse('$required_version')
sys.exit(0 if current >= required else 1)
" 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

# =====================================================================
# Main Installation Steps
# =====================================================================

check_requirements() {
    print_step "Checking system requirements..."
    
    # Check for Python
    if ! check_command python3; then
        print_error "Python 3 is required but not found. Please install Python 3 and try again."
        exit 1
    fi
    
    # Check Python version
    if ! check_python_version python3 "$MIN_PYTHON_VERSION"; then
        print_warning "Python version should be at least $MIN_PYTHON_VERSION. You might experience issues."
    fi
    
    # Check for pip
    if ! check_command pip3 && ! check_command pip; then
        print_warning "pip not found. Will attempt to install it."
    fi
    
    # Check for git
    if ! check_command git; then
        print_warning "git not found. This might be needed for version control."
    fi
    
    log "System requirements check completed"
}

setup_virtual_environment() {
    print_step "Setting up virtual environment..."
    
    # Remove existing venv if it exists
    if [ -d "$VENV_DIR" ]; then
        log_cmd "rm -rf $VENV_DIR"
    fi
    
    # Create new virtual environment
    log_cmd "python3 -m venv $VENV_DIR"
    
    # Activate virtual environment
    log_cmd "source $VENV_DIR/bin/activate"
    
    # Upgrade pip
    log_cmd "pip install --upgrade pip"
    
    print_success "Virtual environment created successfully"
}

install_dependencies() {
    print_step "Installing dependencies..."
    
    # Install the package in development mode
    log_cmd "pip install -e ."
    
    # Install development and test dependencies (optional)
    if [ "$1" = "dev" ]; then
        log_cmd "pip install -e '.[dev,test]'"
    fi
    
    print_success "Dependencies installed successfully"
}

create_launcher() {
    print_step "Creating launcher script..."
    
    # Create launcher script in the main directory
    cat > "$SCRIPT_DIR/llamaduck.sh" <<'EOF'
#!/usr/bin/env bash
# LlamaDuck Pro launcher script

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_DIR="$SCRIPT_DIR/.venv"

if [ ! -d "$VENV_DIR" ]; then
    echo -e "\033[1;31m❌ Virtual environment not found at $VENV_DIR\033[0m"
    echo "Please run the installation script first."
    exit 1
fi

# Activate virtual environment and run llamaduck with all arguments
source "$VENV_DIR/bin/activate"
llamaduck "$@"
EOF
    
    # Make launcher executable
    log_cmd "chmod +x $SCRIPT_DIR/llamaduck.sh"
    
    # Create symlink in parent directory if needed
    if [ "$SCRIPT_DIR" != "$(dirname "$SCRIPT_DIR")" ]; then
        log_cmd "ln -sf $SCRIPT_DIR/llamaduck.sh $(dirname "$SCRIPT_DIR")/llamaduck"
        log_cmd "chmod +x $(dirname "$SCRIPT_DIR")/llamaduck"
    fi
    
    print_success "Launcher script created successfully"
}

run_tests() {
    print_step "Running tests..."
    
    if log_cmd "pytest -xvs tests/"; then
        print_success "Tests passed successfully"
    else
        print_warning "Some tests failed. See log for details."
    fi
}

# =====================================================================
# Main Installation Process
# =====================================================================

main() {
    clear
    print_header "LlamaDuck Pro Installation"
    
    log "Starting installation in $SCRIPT_DIR"
    
    # Ask if user wants to install development dependencies
    local install_dev=false
    read -p "$(echo -e "${PURPLE}Do you want to install development dependencies? (y/N): ${RESET}")" yn
    case $yn in
        [Yy]* ) install_dev=true;;
        * ) install_dev=false;;
    esac
    
    # Installation steps
    check_requirements
    setup_virtual_environment
    
    if [ "$install_dev" = true ]; then
        install_dependencies "dev"
        run_tests
    else
        install_dependencies
    fi
    
    create_launcher
    
    print_header "Installation Complete!"
    echo -e "${GREEN}LlamaDuck Pro has been successfully installed!${RESET}"
    echo
    echo -e "${CYAN}Try these commands:${RESET}"
    echo -e "  ${YELLOW}./llamaduck.sh search \"python best practices\"${RESET}"
    echo -e "  ${YELLOW}./llamaduck.sh chat \"Tell me about llamas\"${RESET}"
    echo
    echo -e "${GRAY}Installation log saved to: $LOG_FILE${RESET}"
    
    log "Installation completed successfully"
}

# Run main function
main 