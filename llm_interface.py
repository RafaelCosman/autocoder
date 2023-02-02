import openai

ENGINE = 'text-davinci-003'
MAX_TOKENS = 1500
TEMPERATURE = 0.0
def complete(prompt):
    completion = openai.Completion.create(
        engine=ENGINE,
        prompt=prompt,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        stream=False,
    )

    return completion['choices'][0]['text']