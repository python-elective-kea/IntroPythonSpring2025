# Introduktion til Large Language Models (LLM) i Python     
Formålet med dagens emner er at give dig et overblik over hvordan vi kan arbejde med LLM´er som en inkoorpereret del af dine applikationer.     
I skal som udgangspunkt have styr på nogle grundlæggende begreber som Transformers, Embeddings, RAG, Agents, og i det hele taget på et overordnet plan hvordan LLM´er fungerer.  




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

**Embeddings, Vetors og vectordatabaser**
Embeddings er en betegnelse for modeller der har til formål at omdanne ord, sætninger eller dokumenter til vektore (lister af tal). 

## Dagen i dag
Denne uges materiale, øvelser og undervisningssessioner er tænkt som en slags overblik over de elementer vi skal bruge til at lave RAG systemer.    
 

## Materiale
* [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (45:00)      
<!-- * [RAG Explained](https://www.youtube.com/watch?v=qppV3n3YlF8) (Ikke så god) -->
* [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M) (6:35)
* [What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI) (12:28)
* [What is Agentic RAG?](https://www.youtube.com/watch?v=0z9_MhcYvcY) (5:41)
* [OpenAI Embeddings and Vector Databases Crash Course](https://www.youtube.com/watch?v=ySus5ZS0b94)

<!-- * [Langchain Quickstart](https://github.com/langchain-ai/langchain/blob/72c8b3127dfaa5c68ef0d66cdb934b785bdfaa29/docs/docs/use_cases/graph/quickstart.ipynb) 
* [Langchain & Neo4j: Query Your Graph Database in Natural Language](https://www.youtube.com/watch?v=Wg445gThtcE)
* [Neo4j in 100 Seconds](https://www.youtube.com/watch?v=T6L9EoBy8Zk)
-->
**ChromaDB** (lav egen video)    
* [How to run a private Chroma Vector Database locally in 5 mins!](https://www.youtube.com/watch?v=61kaK-e3Owc&t=325s)
* [Setting Up Your First ChromaDB Server](https://medium.com/@kenzic/setting-up-your-first-chromadb-server-f5f566273ea9)
* [Usage Guide](https://docs.trychroma.com/guides)

**Teoretisk bagrund**
* [Transformers (how LLMs work) explained visually | DL5](https://www.youtube.com/watch?v=wjZofJX0v4M) (27:13)

### Øvelser
#### Øv 1: Text embeddings
Se videoen [OpenAI Embeddings and Vector Databases Crash Course](https://www.youtube.com/watch?v=ySus5ZS0b94) **(TODO: LAV egen video)**    
Herefter brug [Mistral.ai embeddings](https://docs.mistral.ai/api/#tag/agents/operation/agents_completion_v1_agents_completions_post) (mistral-embed) til at lave det samme som i videoen, men nu skal du kontakte API´et gennem python kode du selv laver. 