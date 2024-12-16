# Introduktion til Large Language Models (LLM) i Python     
Formålet med dagens emner er at give dig et overblik over hvordan vi kan arbejde med LLM´er som en inkoorpereret del af vores applikationer. Vi vil først få styr på et par grundlæggende koncepter som Transformers, Embeddings, RAG, Agents. Til at kode vores applikationer som gør brug af disse elementer skal vi bruge et framework som hedder **Langchain**. Dette framework kommer du også til at lege med idag.     
Og ikke mindst, så hedder valgfaget jo **Introduktion til python**, så vi kommer også til at bruge en del tid på at forstå den kode vi skriver eller kopierer fra tutorials eller ChatGpt. 

## Læringsmål
* Have en overordnet forståelse for hvad en LLM kan bruges til (ud over chatbot scenariet)
* Forstå og kunne forklare konceptetet RAG og Agentic RAG.
* Forstå hvad embeddings er og hvordan de bruges af LLM´s 
* Kunne bruge text, audio, image, video embeddings models

## Forberedelse
Du skal starte med at se denne introduktion til LLM´er:
* [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (45:00)      

> Åben herefter ChatGpt og prøv at se om du kan identificere noget af det som Andrey snakker om. Feks. kan du prøve at se på hvornår det er en ren sprogmodel du skriver med, eller på hvornår der er en for for eksterne værktøjer indvolveret. Prøv at skifte model fra feks. GPT4 til o1 modellerne og iagtag om der er nogen ændring i forhold til hvad der blev snakket om i videoen. (15 minutter).

**Herefter skal du se 3 små videoer.**     
Formålet er at give dig en forståelse for hvad Retrieval-Augmented Generation (RAG) er, og hvad Agents er og kan bruges til i et RAG system. 

* [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M) (6:35)
* [What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI) (12:28)
* [What is Agentic RAG?](https://www.youtube.com/watch?v=0z9_MhcYvcY) (5:41)

**Embeddings, Vetors og vectordatabaser**
Embeddings er en betegnelse for modeller der har til formål at omdanne ord, sætninger eller dokumenter til vektore. 



**Lav følgende tutorial**    
* [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)
Du kan evt. downloade tutorialen som [notebook](https://github.com/langchain-ai/langchain/blob/master/docs/docs/tutorials/chatbot.ipynb) og arbejde med den herfra.     
Formålet er ikke at du bare læser den igennem og får den til at køre. Du skal vide hvad der foregår, og helst i så mange detaljer som du magter at sætte dig ind i. Vi kommer i undervisningen til at kigge på selve koden, og i får en forklaring på hvad de forskellige elementer betyder. Så hvis det virker uforståeligt går du bare videre, og glæder dig over at du har et umiddelbart overblik over koden.     


* [RAG From Scratch: Part 1 (Overview)](https://www.youtube.com/watch?v=wd7TZ4w1mSw)
* [RAG From Scratch: Part 2 (Indexing)](https://www.youtube.com/watch?v=bjb_EMsTDKI)
* [RAG From Scratch: Part 3 (Retrieval)](https://www.youtube.com/watch?v=LxNVgdIz9sU)
* [RAG From Scratch: Part 4 (Generation)](https://www.youtube.com/watch?v=Vw52xyyFsB8)



## Dagen i dag
Dagen i dag er tilrettelagt som selvstudie. I skal følge planen herunder fra start til slut. Materialet ligger på Fronter. Om I har bestået den obligatoriske opgave nummer 2, vil være afhængigt af om I har åbnet dokumenterne eller ikke, klikket på linkene og afleveret det der skal afleveres (jeg kan se om I har åbnet dokumenterne i Fronters statistik).


## Materiale
* [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)
* [RAG Explained](https://www.youtube.com/watch?v=qppV3n3YlF8) (Ikke så god)
* [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M) (BEDST)
* [What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI)
* [What is Agentic RAG?](https://www.youtube.com/watch?v=0z9_MhcYvcY)
* [OpenAI Embeddings and Vector Databases Crash Course](https://www.youtube.com/watch?v=ySus5ZS0b94)
* [What is LangChain?](https://www.youtube.com/watch?v=1bUy-1hGZpI)

<!-- * [Langchain Quickstart](https://github.com/langchain-ai/langchain/blob/72c8b3127dfaa5c68ef0d66cdb934b785bdfaa29/docs/docs/use_cases/graph/quickstart.ipynb) 
* [Langchain & Neo4j: Query Your Graph Database in Natural Language](https://www.youtube.com/watch?v=Wg445gThtcE)
* [Neo4j in 100 Seconds](https://www.youtube.com/watch?v=T6L9EoBy8Zk)
-->
**ChromaDB** (lav egen video)    
* [How to run a private Chroma Vector Database locally in 5 mins!](https://www.youtube.com/watch?v=61kaK-e3Owc&t=325s)
* [Setting Up Your First ChromaDB Server](https://medium.com/@kenzic/setting-up-your-first-chromadb-server-f5f566273ea9)
* [Usage Guide](https://docs.trychroma.com/guides)

**Teoretisk bagrund**
* [Transformers (how LLMs work) explained visually | DL5](https://www.youtube.com/watch?v=wjZofJX0v4M)

### Øvelser
#### Øv 1: Text embeddings
Se videoen [OpenAI Embeddings and Vector Databases Crash Course](https://www.youtube.com/watch?v=ySus5ZS0b94) **(TODO: LAV egen video)**    
Og lav en python fil som 