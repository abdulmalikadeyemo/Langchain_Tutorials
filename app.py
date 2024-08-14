from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()


# Create an instance of the llama-3.1-8b-instant model
model = ChatGroq(model="llama-3.1-8b-instant")

#Create the ouput parser
parser = StrOutputParser()

#Create the prompt
system_template = "Translate the following into {language}:"

user_template = "{text}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system",system_template), ("user", user_template)]
)

#Create the chain
chain = prompt_template | model | parser