import openai, json

def readConfig() -> str:
    return json.loads(open("config.json", mode="r", encoding="utf-8").read())["token"]

openai.api_key = readConfig()



def chatBot(msg: str = ...):
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=msg,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )


    message = completions.choices[0].text
    return message




