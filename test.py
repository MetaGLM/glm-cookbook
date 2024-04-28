from openai import OpenAI

base_url = "http://zrbridge.top:12363/v1/"
client = OpenAI(api_key="llama3", base_url=base_url)


def chat(use_stream=True):
    messages = [
        {
            "role": "user",
            "content": "tell me a story"
        }
    ]
    response = client.chat.completions.create(
        model="llama3",
        messages=messages,
        stream=use_stream,
        max_tokens=4096,
        temperature=0.8,
        top_p=0.8
    )
    if response:
        if use_stream:
            for chunk in response:
                print(chunk.choices[0].delta.content)
        else:
            content = response.choices[0].message.content
            print(content)
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    chat(use_stream=False)
