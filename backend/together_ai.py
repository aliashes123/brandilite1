from together import Together

API_KEY = 'afffcfacf5ebb6d86d286816880d32cc0d69bf62596b45e3e06f8c7ec884e95b'

def generate_youtube_script(prompt):
    client = Together(api_key=API_KEY)

    # Prepare the message for the Llama model
    messages = [{"role": "user", "content": prompt}]

    # Call the Together AI model
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        messages=messages,
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=True
    )

    # Initialize an empty string to capture the AI response
    generated_script = ""

    for token in response:
        if hasattr(token, 'choices'):
            generated_script += token.choices[0].delta.content

    return generated_script
