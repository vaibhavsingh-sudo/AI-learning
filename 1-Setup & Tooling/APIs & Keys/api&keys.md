# APIs & Keys

## Overview

This lesson introduces the fundamentals of working with AI APIs. Every modern LLM API follows the same high-level workflow:

1. Send an HTTP request.
2. Authenticate using an API key.
3. Receive a JSON response.

Although different providers (Anthropic, OpenAI, Google, etc.) expose different SDKs and endpoints, the overall pattern remains the same.

---

# Learning Objectives

After completing this lesson, I can:

- Store API keys securely using environment variables.
- Use a `.env` file for local development.
- Make API calls using an official SDK.
- Make API calls using raw HTTP requests.
- Understand the request and response lifecycle.
- Recognize common API errors.
- Understand rate limits and authentication.

---

# API Request Flow

```
Application
     │
     │ HTTP Request
     │
     ▼
AI API Server
     │
     │ JSON Response
     ▼
Application
```

Every request contains:

- Endpoint URL
- API Key
- Headers
- Request Body

Every response contains:

- Status Code
- Response Headers
- JSON Body

---

# Secure API Keys

Never hardcode API keys inside source code.

Instead, use environment variables.

Example:

```bash
export ANTHROPIC_API_KEY="your_key_here"
export OPENAI_API_KEY="your_key_here"
```

For local development, store them inside a `.env` file.

Example:

```text
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

The `.env` file should always be included inside `.gitignore`.

Example:

```gitignore
.env
```

This prevents secrets from being committed to GitHub.

---

# Python SDK API Call

Implemented in:

```
apicall.py
```

The SDK automatically:

- Reads the API key
- Creates HTTP requests
- Parses JSON responses
- Returns Python objects

Typical workflow:

1. Create client
2. Select model
3. Send prompt
4. Receive response
5. Print generated text

---

# TypeScript SDK API Call

Implemented in:

```
apicall.ts
```

The TypeScript SDK follows nearly the same workflow as Python.

General flow:

1. Create client
2. Read environment variables
3. Send request
4. Receive response
5. Display output

---

# Raw HTTP API Call

Implemented in:

```
rawhttp.py
```

Instead of using an SDK, this implementation manually builds the HTTP request.

A raw request includes:

- URL
- Headers
- API key
- Request body
- JSON encoding

The response must then be decoded manually.

Understanding raw HTTP makes debugging much easier because SDKs simply automate these steps.

---

# Request Lifecycle

```
Program
   │
   ▼
Read API Key
   │
   ▼
Create Request
   │
   ▼
Send HTTP Request
   │
   ▼
API Processes Prompt
   │
   ▼
Receive JSON Response
   │
   ▼
Extract Generated Text
   │
   ▼
Display Output
```

---

# Common API Errors

## Authentication Error

Cause:

- Invalid API key
- Missing API key
- Expired API key

Result:

```
401 Unauthorized
```

Solution:

- Verify API key.
- Ensure environment variables are loaded correctly.

---

## Permission Error

Cause:

- Accessing unavailable models.
- Incorrect organization permissions.

Result:

```
403 Forbidden
```

Solution:

- Verify account permissions.
- Confirm model availability.

---

## Rate Limit Error

Cause:

Too many requests in a short period.

Result:

```
429 Too Many Requests
```

Solution:

- Wait before retrying.
- Implement exponential backoff.

---

## Server Error

Cause:

Temporary provider issue.

Result:

```
500 Internal Server Error
```

Solution:

Retry after a short delay.

---

## Timeout

Cause:

Network delays or long-running requests.

Solution:

Retry with an increased timeout or smaller request.

---

# SDK vs Raw HTTP

| SDK | Raw HTTP |
|------|----------|
| Less code | More code |
| Easier to use | More control |
| Automatic JSON parsing | Manual parsing |
| Built-in error handling | Manual error handling |
| Recommended for production | Useful for debugging and learning |

---

# Important Concepts

## API Key

A secret credential that authenticates requests to an API.

---

## Environment Variable

A system variable used to securely store configuration values such as API keys.

---

## Endpoint

The URL where requests are sent.

Example:

```
https://api.anthropic.com/v1/messages
```

---

## Headers

Metadata sent with an HTTP request.

Examples:

- Content-Type
- x-api-key
- anthropic-version

---

## Request Body

The JSON payload containing:

- model
- messages
- max_tokens

---

## Response Body

A JSON object returned by the server containing the generated output and metadata.

---

## Token

The unit used by language models for processing text.

Both input and output tokens contribute to usage.

---

## Streaming

Receiving generated text incrementally instead of waiting for the complete response.

---

## Rate Limit

The maximum number of API requests allowed within a given time period.

Exceeding this limit usually returns HTTP 429.

---

# Files Created

```
apicall.py
apicall.ts
rawhttp.py
```

---

# Summary

In this lesson I learned how to:

- Securely store API keys.
- Configure environment variables.
- Use official SDKs for API requests.
- Send raw HTTP requests manually.
- Understand request and response structures.
- Debug common API issues.
- Handle authentication failures.
- Handle rate limits.
- Understand how modern AI APIs operate under the hood.

This knowledge forms the foundation for building AI-powered applications, agents, and workflows in later phases.