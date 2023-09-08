import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        answer = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return answer


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
