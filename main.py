import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))
    print(os.environ.get("OPENAI_BASE_URL"))


if __name__ == "__main__":
    main()
