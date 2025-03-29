# 🦙 LlamaDuck Pro

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A powerful macOS-optimized CLI tool for searching the web and getting information using DuckDuckGo's API, built with professional engineering practices.

<p align="center">
  <img src="docs/images/llamaduck-demo.gif" alt="LlamaDuck Demo" width="700">
</p>

## ✨ Features

- 🔍 **Powerful Search** - Get instant search results from DuckDuckGo right in your terminal
- 💬 **Interactive Chat** - Get answers to your questions with a chat-like interface
- 🌈 **Rich Terminal UI** - Beautiful, colorful output with smart formatting
- 🛠️ **Professional Engineering** - Modular architecture, comprehensive testing, and clean code
- 📦 **Easy Installation** - Simple installation process with multiple options

## 🚀 Installation

### Quick Install (Recommended)

```bash
git clone https://github.com/yourusername/llamaduck_pro.git
cd llamaduck_pro
./install.sh
```

### Manual Installation

```bash
git clone https://github.com/yourusername/llamaduck_pro.git
cd llamaduck_pro
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 📋 Usage

### Basic Search

Search the web directly from your terminal:

```bash
llamaduck search "python best practices"
```

### Chat Mode

Have a conversation to get information:

```bash
llamaduck chat "Tell me about llamas"
```

### Help

View all available commands and options:

```bash
llamaduck --help  # Show all commands
llamaduck help-me  # Show detailed help
```

## 🧪 Development

LlamaDuck Pro follows professional engineering practices:

```bash
# Install development dependencies
pip install -e ".[dev,test]"

# Run tests
pytest

# Run linting
ruff check .
mypy llamaduck/

# Format code
ruff format .
```

## 🏗️ Architecture

LlamaDuck Pro is built with a modular architecture:

- `llamaduck/cli.py` - Command-line interface and UI components
- `llamaduck/search.py` - DuckDuckGo search implementation
- `llamaduck/__init__.py` - Package metadata

## 🔄 Continuous Integration

LlamaDuck Pro uses GitHub Actions for CI to ensure quality with every commit:
- Automated testing across multiple Python versions
- Code quality checks with linting and type checking
- Built with professional DevOps practices

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<p align="center">
  Made with ❤️ by Your Name
</p> 