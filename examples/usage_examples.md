# Gemini MCP Server Usage Examples

This document shows how to use the Gemini MCP server tools in Claude Code.

## Setup

First, ensure you have:

1. **Gemini CLI installed and authenticated**:
   ```bash
   # Follow Google's installation instructions
   # Then authenticate
   gcloud auth login
   ```

2. **Server installed in Claude Code**:
   ```bash
   uv run mcp install src/main.py --name "Gemini Assistant"
   ```

## Tool Usage Examples

### Code Review

Review Python code for quality and security:

```json
@gemini_review_code
{
  "code": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)",
  "language": "python",
  "focus": "performance"
}
```

Review JavaScript with security focus:

```json
@gemini_review_code
{
  "code": "function getUserData(userId) {\n    return fetch('/api/users/' + userId)\n        .then(response => response.json());\n}",
  "language": "javascript", 
  "focus": "security"
}
```

### Feature Plan Review

Review a feature specification:

```json
@gemini_proofread_feature_plan
{
  "feature_plan": "## User Authentication Feature\n\n### Overview\nImplement OAuth2-based authentication with Google and GitHub providers.\n\n### Requirements\n- Users can sign in with Google or GitHub\n- Session management with JWT tokens\n- Role-based access control",
  "context": "React frontend with Node.js backend, existing users stored in PostgreSQL",
  "focus_areas": "security,implementation,testing"
}
```

### Bug Analysis

Analyze a bug with context:

```json
@gemini_analyze_bug
{
  "bug_description": "Application crashes when processing large CSV files",
  "code_context": "def process_csv(filepath):\n    with open(filepath, 'r') as f:\n        data = f.read()\n        lines = data.split('\\n')\n        return [line.split(',') for line in lines]",
  "error_logs": "MemoryError: Unable to allocate 2.3 GiB for array",
  "environment": "Python 3.11, 8GB RAM, Ubuntu 22.04",
  "reproduction_steps": "1. Upload CSV file larger than 1GB\n2. Click process button\n3. Application crashes",
  "language": "python"
}
```

### Code Explanation

Get a detailed explanation of complex code:

```json
@gemini_explain_code
{
  "code": "const debounce = (func, delay) => {\n  let timeoutId;\n  return (...args) => {\n    clearTimeout(timeoutId);\n    timeoutId = setTimeout(() => func.apply(this, args), delay);\n  };\n};",
  "language": "javascript",
  "detail_level": "intermediate",
  "questions": "How does closure work here? When would I use this pattern?"
}
```

Get a beginner-friendly explanation:

```json
@gemini_explain_code
{
  "code": "list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))",
  "language": "python",
  "detail_level": "basic",
  "questions": "What does this line do step by step?"
}
```

## Resource Access

You can also ask Claude to show you configuration and status:

- "Show me the Gemini server configuration" (accesses `gemini://config`)
- "What templates are available?" (accesses `gemini://templates`)  
- "Check if Gemini is working" (accesses `gemini://status`)

## Tips for Best Results

### Code Review
- Provide the programming language when known
- Use specific focus areas: `general`, `security`, `performance`, `style`, `bugs`
- Include relevant context in comments

### Feature Plans
- Be specific about your tech stack in the context
- Focus on specific areas like `security,performance,usability,implementation`
- Include constraints and requirements

### Bug Analysis
- Provide complete error messages and stack traces
- Include environment details (OS, language version, memory, etc.)
- Give clear reproduction steps
- Share relevant code context, not just the error line

### Code Explanation
- Choose appropriate detail level: `basic`, `intermediate`, `advanced`
- Ask specific questions about concepts you want to understand
- Provide context about your experience level

## Advanced Usage

### Combining Tools

You can use multiple tools in sequence:

1. Use `@gemini_review_code` to identify issues
2. Use `@gemini_analyze_bug` for specific problems found
3. Use `@gemini_explain_code` to understand complex fixes

### Custom Prompts

The server uses templates internally, but you can get more specific results by:

- Being very detailed in your requests
- Providing comprehensive context
- Asking follow-up questions to drill down into specific areas

## Troubleshooting

If tools don't work:

1. **Check authentication**: Ensure `gcloud auth login` has been run
2. **Verify Gemini CLI**: Run `gemini --help` to confirm it's installed
3. **Check server status**: Ask Claude to access the `gemini://status` resource
4. **Review error messages**: The tools will return helpful error messages if something goes wrong