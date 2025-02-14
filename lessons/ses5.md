# Introduktion til Large Language Models (LLM) i Python     
Formålet med dagens emner er at give dig et overblik over hvordan vi kan arbejde med LLM´er som en inkoorpereret del af dine applikationer.     
I skal som udgangspunkt have styr på nogle grundlæggende begreber som Transformers, Embeddings, RAG, Agents, og i det hele taget på et overordnet plan hvordan en LLM fungerer.  

Og ikke mindst, så hedder valgfaget jo **Introduktion til python**, så vi kommer også til at bruge en del tid på at forstå den kode vi skriver eller kopierer fra tutorials eller ChatGpt. 

## Læringsmål
* Have en overordnet forståelse for hvad en LLM kan bruges til (ud over chatbot scenariet)
* Forstå og kunne forklare konceptetet RAG og Agentic RAG.
* Forstå hvad embeddings er og hvordan de bruges af LLM´s 
* Kunne bruge text, audio, image, video embeddings models

## Forberedelse
Du skal starte med at se denne introduktion til LLM´er:
* [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (45:00)      

> Åben herefter ChatGpt og prøv at se om du kan identificere noget af det som Andrey snakker om. Feks. kan du prøve at se på hvornår det er en ren sprogmodel du skriver med, eller på hvornår der er eksterne værktøjer indvolveret. Prøv at skifte model fra feks. GPT4 til o1 modellerne og iagtag om der er nogen ændring i forhold til hvad der blev snakket om i videoen. (15 minutter).

**Herefter skal du se 3 små videoer.**     
Formålet er at give dig en forståelse for hvad Retrieval-Augmented Generation (RAG) er, hvad Agents er og hvad Agentic RAG er og an bruges til i et RAG system. 

* [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M) (6:35)
* [What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI) (12:28)
* [What is Agentic RAG?](https://www.youtube.com/watch?v=0z9_MhcYvcY) (5:41)

**Teoretisk bagrund**
Denne video skal give dig en forståelse for lidt af teorien bag LLM´er.
* [Transformers (how LLMs work) explained visually | DL5](https://www.youtube.com/watch?v=wjZofJX0v4M) (27:13)
Den skal bare ses som baggrunds information, der giver dig en bredere forståelse for emnet. 

**Embeddings, Vetors og vectordatabaser**     
Embeddings er en betegnelse for modeller der har til formål at omdanne ord, sætninger eller dokumenter til vektore (lister af tal). 
Følgdende video er en overordnet gennemgang af hvordan man kan bruge OpenAI´s embeddings model og en vector database.

* [OpenAI Embeddings and Vector Databases Crash Course](https://www.youtube.com/watch?v=ySus5ZS0b94) (18:40)

**OBS:** Når du kommer til at prøve dette selv, kan du sagtens bruge andre embeddings modeller end OpenAI´s modeller. En mulighed er [Mistral](https://console.mistral.ai/) og deres embeddings model `mistral-embed`. Det er gratis for developers. Det er Open Source, open weights, europæisk, og fungerer i denne sammenhæng lige så fint som alle andre modeller. 

## Dagen i dag
Vi kommer i dag sammen til at lave en simpel applikation som kan embedde dokumenter (fra nettet, fra pdf etc.), gemme dem i en ChromaDB vector database, søge i databasen efter relevante dokumenter og sende disse dokumenter til en LLM med et spørgsmål til teksten.

## Materiale
* [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (45:00)      
* [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M) (6:35)
* [What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI) (12:28)
* [What is Agentic RAG?](https://www.youtube.com/watch?v=0z9_MhcYvcY) (5:41)
* [OpenAI Embeddings and Vector Databases Crash Course](https://www.youtube.com/watch?v=ySus5ZS0b94)
* [Transformers (how LLMs work) explained visually | DL5](https://www.youtube.com/watch?v=wjZofJX0v4M) (27:13)

<!-- * [Langchain Quickstart](https://github.com/langchain-ai/langchain/blob/72c8b3127dfaa5c68ef0d66cdb934b785bdfaa29/docs/docs/use_cases/graph/quickstart.ipynb) 
* [Langchain & Neo4j: Query Your Graph Database in Natural Language](https://www.youtube.com/watch?v=Wg445gThtcE)
* [Neo4j in 100 Seconds](https://www.youtube.com/watch?v=T6L9EoBy8Zk)
-->
<!-- 
**ChromaDB** (lav egen video)    
* [How to run a private Chroma Vector Database locally in 5 mins!](https://www.youtube.com/watch?v=61kaK-e3Owc&t=325s)
* [Setting Up Your First ChromaDB Server](https://medium.com/@kenzic/setting-up-your-first-chromadb-server-f5f566273ea9)
* [Usage Guide](https://docs.trychroma.com/guides)
-->

### Øvelser
#### Øv 1: Text embeddings
Du har i forberedelsen til i dag set videoen [OpenAI Embeddings and Vector Databases Crash Course](https://www.youtube.com/watch?v=ySus5ZS0b94). Hvis du ikke selv har prøvet det han viser i videoen skal du gøre det nu.    
Herefter brug [Mistral.ai embeddings](https://docs.mistral.ai/api/#tag/agents/operation/agents_completion_v1_agents_completions_post) (mistral-embed) til at lave det samme som i videoen, men nu skal du kontakte API´et gennem python kode du selv laver.     
_(OBS: Du har for 2 uger siden lavet noget tilsvarende da du kontaktede [githubs api med requests modulet](https://github.com/python-elective-kea/IntroPythonSpring2025/blob/main/materialer/ses3/tutorial_github_api.md).)_