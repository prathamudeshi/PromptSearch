import requests
import openai

api_key = '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'
openai.api_key = api_key

def generate_text(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt="Write a prompt that i can search on google for most appropriate results about: "+prompt,
            max_tokens=100
        )

        return response.choices[0].text.strip()

    except Exception as e:
        print(prompt)
        print("Error:", e)
        return None
    
def search(query):
    url = "https://www.googleapis.com/customsearch/v1" 
    api_key = "AIzaSyArmR0VWxfyy5urqsX0nI-Ngb8L3iLGVe8"
    cx = "7647ac75be2b045ea"
    params = {
        "key": api_key,
        "cx": cx,
        "q": query
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_answer(query):
    data = search(query)
    if "items" in data and len(data["items"]) > 0:
        top_result = data["items"][0]
        if "title" in top_result and "snippet" in top_result:
            title = top_result["title"]
            snippet = top_result["snippet"]
            return f"{title}\n\n{snippet}"
    return "Sorry, I couldn't find an answer to your question, please try asking again"

# Generate the most appropriate prompt for google
if __name__ == "__main__":
    prompt = input("Enter a prompt: ")

    generated_text = generate_text(prompt)

# Generate the best result found on google
if generated_text:
    user_input = generated_text
    answer = get_answer(user_input)
    print("KnowitAll:", answer)


# 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