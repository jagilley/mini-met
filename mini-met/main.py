import os
from dotenv import load_dotenv
import openai
from openai.embeddings_utils import get_embeddings, get_embedding
from get_content import get_content
from get_hyde_text import get_hyde_text
import pandas as pd
from tqdm import tqdm

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

df = pd.DataFrame(columns=["site", "content", "hyde_description", "hyde_embedding"])

sites_file = "sites.txt"
sites = []
with open(sites_file, "r") as f:
    for line in f:
        sites.append(line.strip())

for site in tqdm(sites):
    content = get_content(site)
    
    hyde_description = get_hyde_text(content)

    hyde_embedding = get_embedding(hyde_description)

    df = pd.concat([df, pd.DataFrame([[site, content, hyde_description, hyde_embedding]], columns=["site", "content", "hyde_description", "hyde_embedding"])])

df.to_csv("hyde.csv", index=False)