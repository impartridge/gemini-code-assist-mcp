# Contributing to Gemini Code Assist MCP

Thank you for your interest in contributing to the Gemini Code Assist MCP server! This document provides guidelines and information for contributors.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- UV package manager
- Google Cloud CLI with authentication set up
- Gemini CLI installed and configured

### Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/gemini-code-assist-mcp.git
   cd gemini-code-assist-mcp
   ```

2. **Set up development environment**:
   ```bash
   # Create and activate virtual environment
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # .venv\Scripts\activate  # On Windows
   
   # Install dependencies
   uv sync
   
   # Install in development mode
   uv pip install -e .
   ```

3. **Verify installation**:
   ```bash
   # Test the CLI
   uv run gemini-mcp-cli --help
   
   # Run tests
   uv run pytest
   
   # Test MCP server
   uv run python src/main.py
   ```

## Development Guidelines

### Code Style

This project follows strict code style guidelines outlined in `CLAUDE.md`:

- **Follow PEP 8** with type hints for all functions
- **Use Pydantic models** for data validation
- **Add docstrings** for all public functions using Google style
- **Keep functions under 50 lines** and classes under 50 lines
- **Use descriptive variable names** and clear logic flow

### Architecture Principles

- **KISS**: Keep it simple, stupid - choose straightforward solutions
- **YAGNI**: You aren't gonna need it - implement only what's needed
- **Vertical slice architecture** with tests next to code
- **Dependency inversion** for flexibility and testability

### Testing

- **Always write tests** for new functionality
- **Tests live next to the code** they test in `tests/` directories
- **Use pytest** for all testing
- **Maintain test coverage** above 80%

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=html

# Run specific test file
uv run pytest src/core/tests/test_gemini_client.py -v
```

### Code Quality

Before submitting changes, ensure your code passes quality checks:

```bash
# Format code
uv run ruff format .

# Run linter
uv run ruff check .

# Run type checker
uv run mypy .
```

## Contributing Process

### 1. Choose an Issue

- Look for issues labeled `good first issue` for newcomers
- Check existing issues and discussions
- For new features, create an issue first to discuss the approach

### 2. Create a Branch

Use descriptive branch names following this pattern:
- `feature/description-of-feature`
- `fix/issue-description`
- `docs/what-is-changing`
- `refactor/what-is-changing`

```bash
git checkout -b feature/add-new-gemini-tool
```

### 3. Make Changes

- Follow the coding standards and architecture guidelines
- Write or update tests for your changes
- Update documentation as needed
- Keep commits focused and atomic

### 4. Testing

Before submitting, ensure your changes work correctly:

```bash
# Run full test suite
uv run pytest

# Test CLI functionality
uv run gemini-mcp-cli status check

# Test MCP server
uv run python src/main.py
```

### 5. Submit Pull Request

1. **Push your branch**:
   ```bash
   git push origin feature/add-new-gemini-tool
   ```

2. **Create a pull request** with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Reference any related issues
   - Screenshots or examples if applicable

3. **Wait for review** and address any feedback

## Pull Request Guidelines

### PR Title Format
- Use conventional commit format: `type: description`
- Examples: `feat: add new gemini tool`, `fix: resolve authentication issue`

### PR Description Template
```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows the project style guidelines
- [ ] Self-review of code completed
- [ ] Documentation updated as needed
- [ ] No breaking changes without proper justification
```

## Types of Contributions

### Bug Fixes
- Fix issues with existing functionality
- Improve error handling and user experience
- Performance optimizations

### New Features
- New MCP tools and functionality
- CLI enhancements
- Integration improvements

### Documentation
- README improvements
- Code documentation
- Examples and tutorials

### Testing
- Additional test coverage
- Integration tests
- Performance tests

## Specific Areas for Contribution

### High Priority
- Additional Gemini tools (security analysis, test generation)
- Claude Code integration improvements
- Performance optimizations
- Better error handling and user feedback

### Medium Priority
- CLI enhancements and new commands
- Template system improvements
- Configuration options
- Documentation and examples

### Low Priority
- Code refactoring
- Additional test coverage
- Development tooling improvements

## Development Tips

### Working with MCP
- Use `uv run mcp dev src/main.py` for development testing
- Test tools using MCP Inspector
- Verify JSON schema compliance

### Working with Gemini CLI
- Test authentication with `gemini --help`
- Use `--debug` flag for troubleshooting
- Verify prompt formatting and responses

### Debugging
- Use `--show-prompts` flag to see Gemini interactions
- Enable debug logging in configuration
- Check logs for authentication and API issues

## Questions and Support

- **Issues**: Use GitHub issues for bug reports and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Documentation**: Check README.md and CLAUDE.md for guidance

## Recognition

Contributors will be acknowledged in:
- GitHub contributors page
- CHANGELOG.md for significant contributions
- README.md for major features

Thank you for helping make Gemini Code Assist MCP better!