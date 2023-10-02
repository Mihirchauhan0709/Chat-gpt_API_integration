import openai

# api-key from chat-gpt
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

def generate_advice(user_profile, user_interest, user_question):
    # Generate a prompt that includes user information and question
    prompt = f"User Profile: {user_profile}\nArea of Interest: {user_interest}\n\nQuestion: {user_question}"

    # Send a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use "text-davinci-003" for gpt-3.5-turbo
        prompt=prompt,
        max_tokens=100,  # Adjust as needed
        temperature=0.7,  # Adjust for response randomness
    )

    # Extract and return the AI-generated advice
    advice = response.choices[0].text
    return advice

# User input
user_profile = input("Enter your profile information (e.g., Name: John, Age: 30, Gender: Male, Profession: Engineer): ")
user_interest = input("Enter your area of interest (e.g., Subject: Math): ")
user_question = input("Enter your question: ")

advice = generate_advice(user_profile, user_interest, user_question)
print("AI-Generated Advice:")
print(advice)
