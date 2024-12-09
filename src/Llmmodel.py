from Env import envset
envset()
import aisuite as ai
client = ai.Client()
from Embedding import embeddocs,get_chunk
from Import import get_pdf_text
def get_llm_response(question):
    pdf=get_pdf_text()
    (text_chunks,embeds)=embeddocs(pdf)
    most_similar_chunk=get_chunk(text_chunks,embeds,question)

    prompt=f"Context: {most_similar_chunk}\n\nQuestion:{question}"

    #models = ["openai:gpt-4o"]
    model = "groq:gemma-7b-it"

    messages = [
        {"role": "system", "content": "Respond to the question with accordance to this"},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.75
            )
    return(response.choices[0].message.content)