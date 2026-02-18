import logging
from google import genai
from google.genai import types
from configs.environment import Config

logger = logging.getLogger(__name__)

client: genai.Client | None = None


def get_client() -> genai.Client:
    global client
    if client is None:
        if not Config.GEMINI_API_KEY:
            raise EnvironmentError("GEMINI_API_KEY is not configured")
        client = genai.Client(api_key=Config.GEMINI_API_KEY)
    return client


PROMPT_TEMPLATE = """
Analyze the following application log and return a JSON object with exactly these keys:
- root_cause: string describing the likely root cause
- suggested_fix: string with actionable remediation steps  
- confidence: one of "High", "Medium", or "Low"

LOG:
{log_text}
"""


def analyze_log(log_text: str) -> dict:
    gemini = get_client()

    response = gemini.models.generate_content(
        model="gemini-2.0-flash",
        contents=PROMPT_TEMPLATE.format(log_text=log_text),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    result = response.parsed
    logger.info("AI analysis completed with confidence: %s",
                result.get("confidence"))
    return result
