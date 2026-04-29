import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_email(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0,
        response_format={"type": "json_object"}  # forces valid JSON
    )

    content = response.choices[0].message.content

    # ✅ Safe JSON parsing
    try:
        parsed_output = json.loads(content)
        return parsed_output
    except Exception as e:
        return {
            "error": "Invalid JSON",
            "raw_output": content
        }


if __name__ == "__main__":
    user_input = input("Enter customer email: ")
    output = classify_email(user_input)

    print("\nOUTPUT:\n")
    print(json.dumps(output, indent=2, ensure_ascii=False))  # pretty print JSON