from ai_engine.gemini_client import generate_response


prompt = (
    "What is the capital of Australia? "
    "Answer in one sentence."
)


print("Connecting to Gemini API...")


response = generate_response(prompt)


print("\nGemini Response:")

print(response)