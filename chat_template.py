from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()


#LLM COnfigurations
config = {'max_new_tokens': 256, 'temperature': 0.6}

llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin', model_type='llama', config=config)
print('Model Loaded Successfully')


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Professor who knows how to explain a concept to people based on their knoweledge level."),
    ("user", "{input}")
])

def get_user_message(concept, target_person_type):
    return f"Explain the concept: {concept} in Machine Learning \n assuming you are talking to a {target_person_type}"

chain = prompt | llm | output_parser

print(chain.invoke({"input": get_user_message('Machine Learning', 'Mathematics PhD Student')}))

