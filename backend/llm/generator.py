from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2:3b-instruct-q8_0", temperature=0)

def generate_answer(msg_history, query):
    prompt = create_prompt_obj(msg_history, query)
    chain = prompt | model

    response = chain.invoke({})
    # print(f"AI-CBOT: {response}")

    msg_history.append(("system", response))

    return response, msg_history

def create_prompt_obj(msg_history, prompt_text):
    msg_history.append(("human", prompt_text))

    prompt = ChatPromptTemplate.from_messages(msg_history)
    return prompt

if __name__ == "__main__":
    
    msg_history = [
        ("system", "You are a helpful AI chat bot. Your name is AI-CBOT!"),
    ]

    while(True):
        user_query = input("User: ")
        generate_answer(msg_history, user_query)