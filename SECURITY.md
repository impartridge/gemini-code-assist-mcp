# Security Policy

## Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1.0 | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

### How to Report

1. **Do NOT** open a public GitHub issue for security vulnerabilities
2. **Email** security reports to: [security@example.com] (replace with actual email)
3. **Include** as much information as possible:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fixes (if any)

### What to Expect

- **Acknowledgment**: We will acknowledge receipt within 24 hours
- **Initial Response**: We will provide an initial response within 72 hours
- **Status Updates**: We will keep you informed of progress
- **Resolution**: We aim to resolve critical issues within 7 days

## Security Considerations

### Authentication & Authorization

This MCP server relies on:
- **Google Cloud Authentication**: Uses `gcloud auth login` for Gemini CLI access
- **No API Keys**: No sensitive API keys are stored or transmitted
- **Local Execution**: All operations run locally on the user's machine

### Data Handling

- **No Data Storage**: The server does not store user code or data
- **Transient Processing**: All code analysis is performed in-memory
- **No External Transmission**: Code is only sent to Google Gemini via authenticated CLI

### Potential Security Risks

1. **Code Exposure**: User code is sent to Google Gemini for analysis
2. **Command Injection**: Malicious code in prompts could potentially be executed
3. **Authentication Bypass**: Misconfigured authentication could allow unauthorized access

### Security Best Practices

#### For Users
- **Verify Authentication**: Ensure proper Google Cloud authentication setup
- **Review Code**: Be aware that code is sent to Google Gemini for analysis
- **Use Sandbox Mode**: Enable sandbox mode for untrusted code analysis
- **Network Security**: Ensure secure network connections

#### For Developers
- **Input Validation**: All user inputs are validated using Pydantic models
- **Command Sanitization**: Gemini CLI commands are properly escaped
- **Error Handling**: Sensitive information is not exposed in error messages
- **Subprocess Security**: Subprocess calls use secure parameter passing

## Known Security Limitations

1. **Third-party Dependency**: Security depends on Google Gemini CLI security
2. **Network Transmission**: Code is transmitted over the network to Google services
3. **Local Environment**: Security depends on the user's local environment setup

## Security Updates

Security updates will be:
- Released as soon as possible after discovery
- Clearly marked in release notes
- Communicated through GitHub security advisories
- Backported to supported versions when feasible

## Secure Configuration

### Recommended Settings

```python
# In src/core/config.py
config = ServerConfig(
    gemini_options=GeminiOptions(
        sandbox=True,      # Enable sandbox mode
        debug=False,       # Disable debug in production
        yolo=False         # Disable auto-accept
    ),
    max_file_size_mb=10.0,  # Limit file sizes
    max_context_files=20    # Limit context files
)
```

### Environment Variables

```bash
# Disable debug mode in production
export GEMINI_DEBUG=false

# Enable sandbox mode
export GEMINI_SANDBOX=true
```

## Threat Model

### Assets
- User source code
- Google Cloud credentials
- MCP server configuration

### Threats
- Code injection attacks
- Credential theft
- Unauthorized code access
- Man-in-the-middle attacks

### Mitigations
- Input validation and sanitization
- Secure credential handling
- HTTPS-only communications
- Regular security updates

## Compliance

This project aims to comply with:
- **OWASP Security Guidelines**
- **Google Cloud Security Best Practices**
- **Python Security Guidelines**

## Security Testing

We perform:
- **Static Analysis**: Using mypy and ruff for code quality
- **Dependency Scanning**: Regular updates of dependencies
- **Input Validation Testing**: Comprehensive input validation tests
- **Authentication Testing**: Verification of authentication flows

## Incident Response

In case of a security incident:
1. **Immediate**: Assess the scope and impact
2. **Containment**: Implement immediate fixes or workarounds
3. **Communication**: Notify affected users and maintainers
4. **Recovery**: Deploy patches and verify fixes
5. **Learning**: Conduct post-incident review

## Security Resources

- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Python Security Guidelines](https://python.org/dev/security/)

## Contact

For security-related questions or concerns:
- **Security Issues**: Use the vulnerability reporting process above
- **General Questions**: Open a GitHub discussion
- **Documentation**: Check the README.md and project documentation

Last updated: 2025-01-14