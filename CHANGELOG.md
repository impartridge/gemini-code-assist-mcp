# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.3] - 2025-01-14

### Fixed
- **MCP Install Support**: Fixed "no server object found" error in `uv run mcp install src/main.py`
- **Server Entry Point**: Exposed FastMCP server object at module level for proper MCP installation
- **Direct Execution**: Fixed server.run() method call to use synchronous execution instead of asyncio

### Added
- **Manual Installation**: Added `claude mcp add` JSON command as alternative installation method
- **Enhanced Troubleshooting**: Added MCP connection timeout and "not connected" error solutions
- **Installation Verification**: Added steps to verify MCP server installation and connectivity

### Changed
- **Main Entry Point**: Modified `src/main.py` to expose server objects (`mcp`, `server`, `app`) at module level
- **Documentation**: Updated README.md with working installation commands and troubleshooting

## [0.1.2] - 2025-01-14

### Added
- Input/output transparency with `--show-prompts` option in CLI
- Both CLI and MCP server now return input prompts and raw responses
- Enhanced response models with `input_prompt` and `gemini_response` fields
- Version tracking in CLI with `--version` command
- Comprehensive output formatting showing both structured and raw responses

### Changed
- Updated CLI from `gemini-cli` to `gemini-mcp-cli` to avoid conflicts
- Enhanced JSON response parsing for better structured output
- Improved error handling with clear messages for authentication failures

### Fixed
- Fixed CLI option context passing for `--show-prompts` flag
- Corrected Gemini CLI integration to use proper `-p` flag for prompts
- Resolved response parsing issues for nested JSON structures

## [0.1.1] - 2025-01-14

### Added
- Complete MCP server implementation using FastMCP
- Gemini CLI integration with Google Cloud authentication
- Four main tools: code review, feature planning, bug analysis, code explanation
- CLI interface for testing and development
- Comprehensive test suite with 14 passing tests
- Vertical slice architecture with proper separation of concerns

### Features
- **Code Review**: Comprehensive analysis with security, performance, and style checks
- **Feature Planning**: Review and improvement of feature specifications
- **Bug Analysis**: Root cause analysis and fix suggestions
- **Code Explanation**: Educational explanations with varying detail levels

### Technical
- FastMCP server with stateless HTTP support for Claude Code compatibility
- Gemini CLI wrapper with proper subprocess handling
- Pydantic models for data validation and API contracts
- Rich CLI output with colored formatting and JSON support
- Template-based prompt system for consistent AI interactions

### Documentation
- Comprehensive README with installation and usage instructions
- CLAUDE.md with development guidelines and principles
- Examples and usage documentation
- Test coverage and development setup instructions

## [0.1.0] - 2025-01-14

### Added
- Initial project structure and setup
- Basic MCP server framework
- Gemini CLI integration prototype
- Core client and configuration modules