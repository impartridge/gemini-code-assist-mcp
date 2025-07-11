"""
Tests for the main Gemini MCP server.
"""

import json
from unittest.mock import AsyncMock, Mock, patch

import pytest

from ...core.gemini_client import GeminiResponse
from ..gemini_server import (
    BugAnalysisRequest,
    CodeExplanationRequest,
    CodeReviewRequest,
    CodeReviewResponse,
    FeaturePlanRequest,
    create_server,
)


class TestRequestModels:
    """Test request/response models."""

    def test_code_review_request(self):
        """Test CodeReviewRequest model."""
        request = CodeReviewRequest(
            code="def hello(): pass",
            language="python",
            focus="security"
        )
        assert request.code == "def hello(): pass"
        assert request.language == "python"
        assert request.focus == "security"

    def test_code_review_request_defaults(self):
        """Test CodeReviewRequest with defaults."""
        request = CodeReviewRequest(code="test code")
        assert request.code == "test code"
        assert request.language is None
        assert request.focus == "general"

    def test_feature_plan_request(self):
        """Test FeaturePlanRequest model."""
        request = FeaturePlanRequest(
            feature_plan="Add user login",
            context="Web app",
            focus_areas="security,usability"
        )
        assert request.feature_plan == "Add user login"
        assert request.context == "Web app"
        assert request.focus_areas == "security,usability"

    def test_bug_analysis_request(self):
        """Test BugAnalysisRequest model."""
        request = BugAnalysisRequest(
            bug_description="App crashes",
            code_context="def crash(): raise Exception()",
            error_logs="Exception raised"
        )
        assert request.bug_description == "App crashes"
        assert request.code_context == "def crash(): raise Exception()"
        assert request.error_logs == "Exception raised"

    def test_code_explanation_request(self):
        """Test CodeExplanationRequest model."""
        request = CodeExplanationRequest(
            code="lambda x: x**2",
            language="python",
            detail_level="advanced"
        )
        assert request.code == "lambda x: x**2"
        assert request.language == "python"
        assert request.detail_level == "advanced"


class TestServerCreation:
    """Test server creation and configuration."""

    def test_create_server(self):
        """Test server creation."""
        server = create_server()
        assert server is not None
        assert server.name == "Gemini MCP Server"

    @patch('src.server.gemini_server.GeminiCLIClient')
    @patch('src.server.gemini_server.ConfigManager')
    def test_server_components_initialized(self, mock_config_manager, mock_client):
        """Test that server components are properly initialized."""
        # Mock the config manager
        mock_config_instance = Mock()
        mock_config_instance.config.name = "Test Server"
        mock_config_instance.config.gemini_options = Mock()
        mock_config_manager.return_value = mock_config_instance

        # Mock the client
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance

        server = create_server()

        # Verify components were initialized
        mock_config_manager.assert_called_once()
        mock_client.assert_called_once()


class TestServerTools:
    """Test server tool functionality."""

    @pytest.fixture
    def mock_context(self):
        """Create a mock MCP context."""
        context = AsyncMock()
        context.info = AsyncMock()
        context.error = AsyncMock()
        return context

    @pytest.fixture
    def mock_gemini_client(self):
        """Create a mock Gemini client."""
        return AsyncMock()

    @pytest.mark.asyncio
    async def test_code_review_tool_success(self, mock_context, mock_gemini_client):
        """Test successful code review."""
        # Mock successful Gemini response with JSON
        mock_response = GeminiResponse(
            content='```json\n{"summary": "Good code", "issues": [], "suggestions": ["Add docstring"], "rating": "B+"}\n```',
            success=True
        )
        mock_gemini_client.call_with_structured_prompt.return_value = mock_response

        with patch('src.server.gemini_server.GeminiCLIClient') as mock_client_class:
            mock_client_class.return_value = mock_gemini_client

            server = create_server()

            # Get the tool function
            tools = [tool for tool in server._tools if tool.name == "gemini_review_code"]
            assert len(tools) == 1
            tool_func = tools[0].func

            request = CodeReviewRequest(
                code="def hello(): return 'world'",
                language="python"
            )

            result = await tool_func(request, mock_context)

            assert isinstance(result, CodeReviewResponse)
            assert result.summary == "Good code"
            assert result.rating == "B+"
            mock_context.info.assert_called()

    @pytest.mark.asyncio
    async def test_code_review_tool_error(self, mock_context, mock_gemini_client):
        """Test code review with error."""
        # Mock failed Gemini response
        mock_response = GeminiResponse(
            content="",
            success=False,
            error="API error"
        )
        mock_gemini_client.call_with_structured_prompt.return_value = mock_response

        with patch('src.server.gemini_server.GeminiCLIClient') as mock_client_class:
            mock_client_class.return_value = mock_gemini_client

            server = create_server()

            tools = [tool for tool in server._tools if tool.name == "gemini_review_code"]
            tool_func = tools[0].func

            request = CodeReviewRequest(code="test code")
            result = await tool_func(request, mock_context)

            assert isinstance(result, CodeReviewResponse)
            assert "failed" in result.summary.lower()
            assert result.rating == "Failed"
            mock_context.error.assert_called()

    @pytest.mark.asyncio
    async def test_feature_plan_tool_success(self, mock_context, mock_gemini_client):
        """Test successful feature plan review."""
        mock_response = GeminiResponse(
            content="The feature plan looks good but needs more details on...",
            success=True
        )
        mock_gemini_client.call_with_structured_prompt.return_value = mock_response

        with patch('src.server.gemini_server.GeminiCLIClient') as mock_client_class:
            mock_client_class.return_value = mock_gemini_client

            server = create_server()

            tools = [tool for tool in server._tools if tool.name == "gemini_proofread_feature_plan"]
            tool_func = tools[0].func

            request = FeaturePlanRequest(
                feature_plan="Add user authentication system"
            )

            result = await tool_func(request, mock_context)

            assert isinstance(result, str)
            assert "good but needs more details" in result
            mock_context.info.assert_called()

    @pytest.mark.asyncio
    async def test_bug_analysis_tool_success(self, mock_context, mock_gemini_client):
        """Test successful bug analysis."""
        mock_response = GeminiResponse(
            content="The bug is caused by a null pointer exception. To fix...",
            success=True
        )
        mock_gemini_client.call_with_structured_prompt.return_value = mock_response

        with patch('src.server.gemini_server.GeminiCLIClient') as mock_client_class:
            mock_client_class.return_value = mock_gemini_client

            server = create_server()

            tools = [tool for tool in server._tools if tool.name == "gemini_analyze_bug"]
            tool_func = tools[0].func

            request = BugAnalysisRequest(
                bug_description="App crashes on startup",
                error_logs="NullPointerException at line 42"
            )

            result = await tool_func(request, mock_context)

            assert isinstance(result, str)
            assert "null pointer exception" in result.lower()
            mock_context.info.assert_called()

    @pytest.mark.asyncio
    async def test_code_explanation_tool_success(self, mock_context, mock_gemini_client):
        """Test successful code explanation."""
        mock_response = GeminiResponse(
            content="This code defines a lambda function that squares its input...",
            success=True
        )
        mock_gemini_client.call_with_structured_prompt.return_value = mock_response

        with patch('src.server.gemini_server.GeminiCLIClient') as mock_client_class:
            mock_client_class.return_value = mock_gemini_client

            server = create_server()

            tools = [tool for tool in server._tools if tool.name == "gemini_explain_code"]
            tool_func = tools[0].func

            request = CodeExplanationRequest(
                code="lambda x: x**2",
                language="python"
            )

            result = await tool_func(request, mock_context)

            assert isinstance(result, str)
            assert "lambda function" in result.lower()
            mock_context.info.assert_called()


class TestServerResources:
    """Test server resources."""

    def test_config_resource(self):
        """Test config resource."""
        server = create_server()

        # Find config resource
        resources = [res for res in server._resources if res.uri == "gemini://config"]
        assert len(resources) == 1

        config_func = resources[0].func
        result = config_func()

        # Should return valid JSON
        config_data = json.loads(result)
        assert "name" in config_data
        assert "gemini_options" in config_data

    def test_templates_resource(self):
        """Test templates resource."""
        server = create_server()

        resources = [res for res in server._resources if res.uri == "gemini://templates"]
        assert len(resources) == 1

        templates_func = resources[0].func
        result = templates_func()

        # Should return valid JSON with templates
        templates_data = json.loads(result)
        assert isinstance(templates_data, dict)
        assert "code_review" in templates_data
