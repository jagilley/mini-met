# mini-met
#### A minimalist re-implementation of Metaphor Systems' Search API

## How it works

`mini-met/main.py` looks at the list of sites in `sites.txt` and scrapes its text content with Browserless' `scrape` API. It generates a [HyDE](https://arxiv.org/abs/2212.10496) description of each site, then embeds it using OpenAI's ada embedding model. Embeddings and descriptions are stored in `hyde.csv`.

In `query.ipynb`, you can type in a site query and it will return the most similar sites in `hyde.csv`, ranked by cosine similarity of the embedded query to the embedded site descriptions. You can also use Metaphor's official API on the same query and compare the results.