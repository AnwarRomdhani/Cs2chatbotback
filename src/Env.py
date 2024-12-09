import os
from dotenv import load_dotenv
def envset():
    os.chdir("../")
    load_dotenv()
    os.environ["HUGGINGFACE_TOKEN"]=os.getenv('HUGGINGFACE_TOKEN')
    os.environ["GROQ_API_KEY"]=os.getenv('GROQ_API_KEY')