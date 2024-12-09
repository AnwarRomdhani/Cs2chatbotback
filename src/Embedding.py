from Import import get_pdf_text
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

pdf=get_pdf_text()
def embeddocs(pdf):
    model=SentenceTransformer('all-MiniLM-L6-v2')
    chunk_size = 500
    text_chunks = [pdf[i:i + chunk_size] for i in range(0, len(pdf), chunk_size)]

    embeds=model.encode(text_chunks)
    return(text_chunks,embeds)

def get_chunk(text_chunks,embeds,question):
    model=SentenceTransformer('all-MiniLM-L6-v2')
    user_question = question

    user_question_embed = model.encode([user_question])

    similarities = cosine_similarity(user_question_embed, embeds)

    most_similar_idx = np.argmax(similarities)
    most_similar_chunk = text_chunks[most_similar_idx]
    return(most_similar_chunk)