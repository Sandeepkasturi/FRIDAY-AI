#SANDEEP KASTURI
#Download Openai package in python
import openai
import pyttsx3
# create an account in OpenAI to get free API's
openai.api_key = "# YOUR_API_KEY" 

def chatbot(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",  # produces higher quality writing.
    prompt=prompt,
    max_tokens=1024, // defines the maximum tokens
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

engine = pyttsx3.init() // Speech Module code you can change it

while True:
  user_input = input("User: ")
  response = chatbot(user_input)
  print("Chatbot: ", response)
  engine.say(response)
  engine.runAndWait()
