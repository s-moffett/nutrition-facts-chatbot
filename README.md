# Nutrition facts chatbot

A small RAG project that uses an LLM to answer nutrition questions based on the blog posts at https://nutritionfacts.org/blog/.

## Running the project
Make sure an Anthropic API key is defined in `ANTHROPIC_API_KEY`.
I recommend using a venv with Python 3.12.

Unzip the nutrition_facts_data into data/.

`pip install -r requirements.txt`

`python src/main.py`

## Example questions

- Are there foods that are best for migraines?
- What should I eat to lower my blood pressure?
- Are there foods that are best for anxiety?

## Example responses

See the `example_responses` directory for several example responses.