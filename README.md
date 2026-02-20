# Advanced Scam Honeypot API

## Overview

This project implements a multi-turn AI-powered Scam Honeypot API designed to:

- Detect multiple types of fraud generically
- Engage scammers intelligently
- Extract actionable intelligence
- Maintain realistic multi-turn conversations
- Produce structured final evaluation output

The system is built to comply fully with the Hackathon Honeypot API Evaluation System.

## Key Capabilities

- Multi-turn scam detection (not single-message based)
- Cumulative confidence scoring
- Hybrid intelligence extraction (LLM + Regex)
- Automatic red-flag accumulation
- Engagement strategy enforcement (≥8 turns bias)
- Investigative question enforcement (≥5 guaranteed)
- Structured finalOutput generation
- No hardcoded scenario logic
- Fully generic detection engine

## Scam Detection Strategy

The detection engine uses:

1. LLM-based contextual analysis
2. Cumulative confidence tracking across turns
3. Red flag aggregation
4. Intelligence-triggered confidence boost
5. Hybrid detection fallback logic

Scam detection does NOT rely on specific keywords or hardcoded scenarios.

## Intelligence Extraction Strategy

Hybrid extraction approach:

- LLM entity extraction (context aware)
- Regex deterministic fallback
- Deduplication logic
- Overlap cleaning (phone/account conflict resolution)
- Email vs UPI separation

Extracted intelligence types:

- Phone numbers
- Bank account numbers
- UPI IDs
- Phishing links
- Email addresses
- Case IDs
- Policy numbers
- Order numbers

## Conversation Strategy

The honeypot:

- Maintains at least 8 conversational turns (engagement bias)
- Ensures ≥5 investigative questions
- Subtly references red flags
- Extracts identity and verification details
- Avoids direct accusation early
- Adapts to scam type dynamically

## Architecture

app/
├── main.py
├── config.py
├── models.py
├── core/
│ ├── session_manager.py
│ ├── scam_analyzer.py
│ ├── intelligence_extractor.py
│ ├── regex_extractor.py
│ ├── conversation_engine.py
│ ├── engagement_controller.py
│ └── final_output_builder.py
└── utils/
└── regex_patterns.py

## Tech Stack

- FastAPI
- OpenAI GPT (gpt-4o-mini)
- Python 3.10+
- Regex-based deterministic extraction
- In-memory session state manager

## Authentication

All endpoints require:
x-api-key: <guvi_hackathon_2026_tech_squad>

## API Endpoints

### POST `/honeypot`

Handles multi-turn conversation.

**Response format:**

```json
{
  "status": "success",
  "reply": "..."
}

GET /final-output/{session_id}

Returns structured evaluation result:

{
  "sessionId": "...",
  "scamDetected": true,
  "totalMessagesExchanged": 10,
  "engagementDurationSeconds": 180,
  "extractedIntelligence": {...},
  "agentNotes": "...",
  "scamType": "...",
  "confidenceLevel": 0.92
}