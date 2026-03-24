import os
from openai import OpenAI

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY が設定されていません")
        
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="30文字以内で、GitHub Actions上でAI呼び出し成功と日本語で返して"
    )

    print(response.output_text)

if __name__ == "__main__":
    main()
