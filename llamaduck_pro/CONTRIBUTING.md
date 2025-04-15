# Contributing to LlamaDuck Pro

Thank you for considering contributing to LlamaDuck Pro! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to see if the problem has already been reported. When you are creating a bug report, please include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Describe the behavior you observed and what you expected to see
- Include screenshots or animated GIFs if possible
- Include details about your environment (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- List any alternatives you've considered

### Pull Requests

- Fill in the required template
- Follow the style guides
- Include tests for new features
- Document new code
- Make sure all tests pass

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment and install dependencies:
   ```bash
   cd llamaduck_pro
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev,test]"
   ```
3. Install pre-commit hooks:
   ```bash
   make install-hooks
   ```

## Development Workflow

1. Create a branch for your work:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. Make your changes and ensure tests pass:
   ```bash
   make format  # Format code
   make lint    # Check code quality
   make test    # Run tests
   ```

3. Commit your changes with meaningful commit messages:
   ```bash
   git commit -m "Add some amazing feature"
   ```

4. Push to your fork and submit a pull request

## Style Guides

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints
- Write descriptive docstrings following [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Format code with `ruff format`
- Check code with `ruff check` and `mypy`

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

## Additional Notes

### Issue and Pull Request Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `good first issue`: Good for newcomers

## Thank You!

Your contributions to open source, large or small, make projects like this possible. Thank you for taking the time to contribute. 