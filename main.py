from langchain.agents.agent_toolkits import GmailToolkit
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
import os 

os.environ['OPENAI_API_KEY']='ENTER YOUR API KEY HERE'
# openai_api_key = os.getenv("OPENAI_API_KEY")
toolkit = GmailToolkit()

llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)

agent.run(
    {
        "input": {
            "message":'''This is the email body, I'm trying to Integrate Gmail with GPT but getting issues. Working on resolving these issues.
            this is the 3rd time now''',
            "to": ["recipent.email@gmail.com"],
            "subject": "Integration of Gmail with GPT",
            # Optional fields:
            "cc": ["rajasami@gmail.com"],
            "bcc": ["random.user@gmail.com"]
        }
    }
)


agent.run(
    {
        
"input": "Create a gmail draft for me to edit of a letter from the perspective of a sentient parrot"
"who is looking to collaborate on some research with her"
"estranged friend, a cat. Under no circumstances may you send the message, however.", 
"to": ["rajasami@example.com"],  # Replace with the cat's email
"subject": "Research Collaboration from a Sentient Parrot" # Your full text for creating a draft
    }   
)


agent.run(
    {
        "input": "Could you search in my drafts for the latest email?"  # Your text for searching drafts
    }
)






