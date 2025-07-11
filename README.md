# Gemini MCP Server

A robust Model Context Protocol (MCP) server that integrates Google Gemini CLI with Claude Code for AI-powered development assistance.

## Features

This MCP server provides the following tools for development assistance:

### 🔍 Code Analysis & Review
- **`gemini_review_code`**: Comprehensive code review with quality, security, and performance analysis
- **`gemini_analyze_security`**: Security-focused code analysis

### 📋 Feature Planning & Documentation  
- **`gemini_proofread_feature_plan`**: Review and improve feature specifications
- **`gemini_suggest_implementation`**: Implementation guidance and architecture suggestions

### 🐛 Bug Analysis & Debugging
- **`gemini_analyze_bug`**: Root cause analysis and fix suggestions
- **`gemini_debug_assistance`**: Debugging workflow assistance

### 📖 Code Understanding
- **`gemini_explain_code`**: Clear code explanations with varying detail levels
- **`gemini_generate_tests`**: AI-assisted test generation

## Prerequisites

Before using this MCP server, ensure you have:

1. **Gemini CLI installed and configured**
   ```bash
   # Install Gemini CLI (follow Google's official instructions)
   # https://github.com/google-gemini/gemini-cli
   ```

2. **Google authentication set up**
   ```bash
   # Authenticate with Google (no API key needed)
   gcloud auth login
   ```

3. **Python 3.11+ with UV package manager**
   ```bash
   # Install UV if not already installed
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

## Installation

1. **Clone and install the MCP server**:
   ```bash
   git clone <repository-url>
   cd gemini-mcp-server
   uv sync
   ```

2. **Test the installation**:
   ```bash
   # Test Gemini CLI access
   gemini --help
   
   # Test the MCP server
   uv run python src/main.py
   ```

3. **Test the installation**:
   ```bash
   # Run installation tests
   uv run python test_installation.py
   ```

4. **Install in Claude Code**:
   ```bash
   # Install the server for Claude Code
   uv run mcp install src/main.py
   
   # Or with a custom name
   uv run mcp install src/main.py --name "Gemini Assistant"
   ```

## Usage in Claude Code

Once installed, you can use the Gemini tools directly in Claude Code:

### Code Review Example
```
@gemini_review_code
{
  "code": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)",
  "language": "python",
  "focus": "performance"
}
```

### Feature Plan Review Example
```
@gemini_proofread_feature_plan
{
  "feature_plan": "Add user authentication with OAuth2...",
  "context": "Web application with React frontend",
  "focus_areas": "security,usability,implementation"
}
```

### Bug Analysis Example
```
@gemini_analyze_bug
{
  "bug_description": "Application crashes when processing large files",
  "code_context": "def process_file(filepath):\n    with open(filepath) as f:\n        return f.read()",
  "error_logs": "MemoryError: Unable to allocate array",
  "environment": "Python 3.11, 8GB RAM"
}
```

## Configuration

### Server Configuration

The server can be configured by modifying the `ServerConfig` in `src/core/config.py`:

```python
config = ServerConfig(
    name="Custom Gemini Server",
    gemini_options=GeminiOptions(
        model="gemini-2.5-pro",  # or "gemini-pro"
        sandbox=False,           # Enable sandbox mode
        debug=False             # Enable debug logging
    ),
    enable_caching=True,
    max_file_size_mb=10.0
)
```

### Gemini CLI Options

The server supports all major Gemini CLI options:

- `model`: Choose the Gemini model (`gemini-2.5-pro`, `gemini-pro`)
- `sandbox`: Run in sandbox mode for code execution
- `debug`: Enable detailed logging
- `all_files`: Include all files in context
- `yolo`: Auto-accept all actions
- `checkpointing`: Enable file edit checkpointing

### Custom Templates

You can add custom prompt templates by extending the `ConfigManager`:

```python
from src.core.config import ConfigManager, PromptTemplate

manager = ConfigManager()
custom_template = PromptTemplate(
    name="custom_review",
    description="Custom code review template",
    system_prompt="You are a specialized reviewer for...",
    user_template="Review this {language} code: {code}",
    variables={"language": "Programming language", "code": "Code to review"}
)
manager.add_template(custom_template)
```

## Available Resources

The server exposes several MCP resources for inspection:

- **`gemini://config`**: Current server configuration
- **`gemini://templates`**: Available prompt templates
- **`gemini://status`**: Gemini CLI status and authentication info

Access these in Claude Code:
```
Can you show me the current Gemini configuration?
# Claude will automatically fetch gemini://config resource
```

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test files
uv run pytest src/core/tests/test_gemini_client.py -v

# Run with coverage
uv run pytest --cov=src --cov-report=html
```

### Code Quality

```bash
# Format code
uv run ruff format .

# Run linter
uv run ruff check .

# Run type checker
uv run mypy .
```

### Development Mode

For development and testing:

```bash
# Run server in development mode
uv run mcp dev src/main.py

# This allows testing with MCP Inspector
# Visit the provided URL to test tools interactively
```

## Architecture

The server follows a vertical slice architecture:

```
src/
├── main.py                 # Entry point
├── server/                 # FastMCP server implementation
│   ├── gemini_server.py   # Main server with tools
│   └── tests/
├── core/                   # Core utilities
│   ├── gemini_client.py   # Gemini CLI wrapper
│   ├── config.py          # Configuration management
│   └── tests/
├── features/               # Feature modules
│   ├── proofreading/      # Review and proofreading
│   ├── analysis/          # Bug and code analysis
│   ├── utilities/         # Helper utilities
│   └── tests/
└── templates/              # Prompt templates
```

### Key Components

1. **GeminiCLIClient**: Handles subprocess calls to Gemini CLI with proper authentication
2. **ConfigManager**: Manages server configuration and prompt templates
3. **FastMCP Server**: Implements MCP tools and resources
4. **Prompt Templates**: Structured prompts for different use cases

## Troubleshooting

### Common Issues

1. **"Gemini CLI not found"**
   - Install Gemini CLI following Google's instructions
   - Ensure `gemini` command is in your PATH

2. **Authentication errors**
   - Run `gcloud auth login` to authenticate
   - Verify access with `gemini --help`

3. **"Command failed with exit code 1"**
   - Check your Google authentication status
   - Verify you have access to Gemini models
   - Check internet connectivity

4. **Tool timeouts**
   - Large code files may take time to process
   - Consider breaking down large requests
   - Check if you've hit rate limits

### Debug Mode

Enable debug mode for detailed logging:

```python
# In src/core/config.py
gemini_options = GeminiOptions(debug=True)
```

Or set temporarily:
```bash
export GEMINI_DEBUG=true
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the code style guidelines
4. Add tests for new functionality
5. Run the test suite and ensure all tests pass
6. Submit a pull request

### Code Style

- Follow PEP 8
- Use type hints for all functions
- Add docstrings for all public functions and classes
- Keep functions under 50 lines
- Keep classes under 50 lines
- Use Pydantic models for data validation

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

## Acknowledgments

- Google Gemini team for the excellent CLI tool
- Anthropic for the Model Context Protocol
- The open-source community for various dependencies