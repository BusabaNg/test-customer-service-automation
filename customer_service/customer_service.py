from openai_client import client


SYSTEMPROMPT = """
You are a friendly and intelligent customer service representative who typically  handle customer service questions like inquiries about account status, service disruptions, or product details.
Your task is to assist customers with their inquiries accurately. 
Provide clear, polite, and helpful responses. 

user_inquiry: {user_inquiry}
"""


def generate_response(user_inquiry):
    """Function to generate a response"""
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system", 
                "content": SYSTEMPROMPT
             },
            {   
                "role": "user", 
                "content": f"user_inquiry={user_inquiry}"
            }
        ],
        temperature=0,
        max_tokens=256 
    )

    return completion.to_dict()['choices'][0]['message']['content']


def handle_customer_inquiry(user_input):
    """Handles user input and response generation"""
    try:
        gpt_response = generate_response(user_input)
        formatted_response = format_response(gpt_response)
        return formatted_response
    except Exception as e:
        return f"An error occurred: {e}"


def format_response(response):
    """Formats the GPT response for better presentation."""
    return f"Customer Service: {response}\n"


def main():
    
    print("\n#########################################################")
    print("#        Welcome to Customer Service Automation         #")
    print("#########################################################\n")

    while True:
        user_input = input("Customer: ")
        if user_input.lower() == "exit":
            break

        formatted_response = handle_customer_inquiry(user_input)
        print(formatted_response)
   

if __name__ == "__main__":
    main()