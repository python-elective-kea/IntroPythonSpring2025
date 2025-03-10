# Prompt Engineering

## Læringsmål
Efter denne uge er overstået vil i kunne:
* Forstå hvad vi opnår ved at bruge prompt enginering. 
* Kunne skrive prompts der følger teknikker i:
    * Zero-shot prompting, Few-shot prompting, Using delimiters, Detailed, numbered steps prompting.

## Forberedelse
I skal se følgende videoer
* [RAG from scratch: Part 5 (Query Translation -- Multi Query)](https://www.youtube.com/watch?v=JChPi0CRnDY) (6:08)
* [RAG from scratch: Part 6 (Query Translation -- RAG Fusion)](https://www.youtube.com/watch?v=77qELPbNgxA) (5:41)
* [RAG from scratch: Part 7 (Query Translation -- Decomposition)](https://www.youtube.com/watch?v=h0OPWlEOank) (6:36)
* [RAG from scratch: Part 8 (Query Translation -- Step Back)](https://www.youtube.com/watch?v=xn1jEjRyJ2U) (6:58)
* [RAG from scratch: Part 9 (Query Translation -- HyDE)](https://www.youtube.com/watch?v=SaDzIVkYqyY) (4:46)

Og læse denne artikkel:

* [Prompt Engineering: A Practical Example](https://realpython.com/practical-prompt-engineering/)


## Dagen i dag
Vi gennemgår (som sidst) koden fra de 5 langchain videoer. Vi vil have fokus på at forklare koden, så i forstår præcist hvad der sker. Vi vil også have fokus på at forklare de prompt koncepter der berøres, og de langchain koncepter han snakker om i videoen. 

Vi kommer til at gennemgå noget af det der er i disse videoer:

* [Getting Started with LangSmith (1/7): Tracing](https://www.youtube.com/watch?v=Hab2CV_0hpQ)
* [Getting Started with LangSmith (2/7): Playground](https://www.youtube.com/watch?v=suJU1VYzy50)
* [Getting Started with LangSmith (3/7): Prompts](https://www.youtube.com/watch?v=OJUR7Aa5atM)

**Notebooks fra undervisningen:**

* [Rag From Scratch: Query Transformations](../materialer/ses7/rag_from_scratch_5_to_9.ipynb)
* [MultiQueryRetriever](../materialer/ses7/MultiQueryRetriever.ipynb)



## Materiale
* [LangChain Hub](https://smith.langchain.com/hub/)
* [Prompt Engineering: A Practical Example](https://realpython.com/practical-prompt-engineering/)
* [RAG from scratch: Part 5 (Query Translation -- Multi Query)](https://www.youtube.com/watch?v=JChPi0CRnDY)
* [RAG from scratch: Part 6 (Query Translation -- RAG Fusion)](https://www.youtube.com/watch?v=77qELPbNgxA)
* [RAG from scratch: Part 6 (Query Translation -- RAG Fusion)](https://www.youtube.com/watch?v=77qELPbNgxA) (5:41)
* [RAG from scratch: Part 7 (Query Translation -- Decomposition)](https://www.youtube.com/watch?v=h0OPWlEOank) (6:36)
* [RAG from scratch: Part 8 (Query Translation -- Step Back)](https://www.youtube.com/watch?v=xn1jEjRyJ2U) (6:58)
* [RAG from scratch: Part 9 (Query Translation -- HyDE)](https://www.youtube.com/watch?v=SaDzIVkYqyY) (4:46)
* [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

* [Getting Started with LangSmith (1/7): Tracing](https://www.youtube.com/watch?v=Hab2CV_0hpQ)
* [Getting Started with LangSmith (2/7): Playground](https://www.youtube.com/watch?v=suJU1VYzy50)
* [Getting Started with LangSmith (3/7): Prompts](https://www.youtube.com/watch?v=OJUR7Aa5atM)

### Øvelser
#### 1. Arbejd videre på samme projekt som i arbejde på sidste uge, og tilføj de prompt koncepter i har læst om derhjemme.    
_(Husk at det ikke er spildt arbjede at finde et projekt at arbejde på. Det er nærmest én til én hvad i vil kunne tage med til en eksamen.)_  

#### 2. [Quiz: Practical Prompt Engineering](https://realpython.com/quizzes/practical-prompt-engineering/viewer/)

#### 3. Langsmith Prompt play
Brug https://smith.langchain.com/prompts/ til at lave en prompts gemme dem og brug `hub.pull("<prompt>")` til at gøre brug af den i en notebook.

#### 4. Analyser denne application [https://madeometer.com/](https://madeometer.com/).
Hvis i bruger jeres browsers inspect tool vil i blandt andet kunne se at den sender et billede til dette endpoint: https://liafcajrwvaytbcskbwr.supabase.co/functions/v1/analyze-product får den noget ala dette tilbage: 

````
{
    "productName": "Post-it Notes",
    "country": "USA",
    "score": 100,
    "explanation": "Post-it is a brand of stationery products created by 3M Company, which was founded in 1902 in Minnesota, USA. The brand is recognized globally for its sticky notes and other office supplies.",
    "priceRangeDKK": "50-150 DKK",
    "brandInfo": {
        "name": "Post-it",
        "reputation": "Well-known for quality stationery products",
        "ultimateOwnerCompany": "3M Company",
        "countryOfOrigin": "USA",
        "ultimateOwnerCountry": "USA"
    },
    "mainBeneficiary": "USA",
    "ultimateOwner": "3M Company (USA)",
    "brandOriginCountry": "USA",
    "europeanAlternatives": [
        "Faber-Castell Sticky Notes - A German brand known for high-quality stationery products, owned by Faber-Castell AG.",
        "Pukka Pad - A UK-based company offering a range of stationery products, owned by Pukka Pad Ltd.",
        "Leitz Sticky Notes - A German brand providing office supplies, owned by Esselte Group.",
        "Clairefontaine Sticky Notes - A French brand known for its paper products, owned by Exacompta Clairefontaine.",
        "Rhodia Sticky Notes - A French brand recognized for its quality paper products, owned by Exacompta Clairefontaine."
    ],
    "healthInfo": {
        "lactoseFree": false,
        "glutenFree": false,
        "veganFriendly": false,
        "allergens": [],
        "nutritionalHighlights": []
    },
    "fullAnalysisResponse": {
        "id": "chatcmpl-B8PmiNn3PnXzYPIumBZ2pxqN7ibtb",
        "object": "chat.completion",
        "created": 1741345440,
        "model": "gpt-4o-mini-2024-07-18",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "```json\n{\n  \"productName\": \"Post-it Notes\",\n  \"productType\": \"non-food\",\n  \"manufacturingCountry\": \"USA\",\n  \"brandInfo\": {\n    \"name\": \"Post-it\",\n    \"reputation\": \"Well-known for quality stationery products\",\n    \"ultimateOwnerCompany\": \"3M Company\",\n    \"countryOfOrigin\": \"USA\",\n    \"ultimateOwnerCountry\": \"USA\"\n  },\n  \"score\": 100,\n  \"explanation\": \"Post-it is a brand of stationery products created by 3M Company, which was founded in 1902 in Minnesota, USA. The brand is recognized globally for its sticky notes and other office supplies.\",\n  \"priceRangeDKK\": \"50-150 DKK\",\n  \"europeanAlternatives\": [\n    \"Faber-Castell Sticky Notes - A German brand known for high-quality stationery products, owned by Faber-Castell AG.\",\n    \"Pukka Pad - A UK-based company offering a range of stationery products, owned by Pukka Pad Ltd.\",\n    \"Leitz Sticky Notes - A German brand providing office supplies, owned by Esselte Group.\",\n    \"Clairefontaine Sticky Notes - A French brand known for its paper products, owned by Exacompta Clairefontaine.\",\n    \"Rhodia Sticky Notes - A French brand recognized for its quality paper products, owned by Exacompta Clairefontaine.\"\n  ],\n  \"healthInfo\": {\n    \"lactoseFree\": false,\n    \"glutenFree\": false,\n    \"veganFriendly\": false,\n    \"allergens\": [],\n    \"nutritionalHighlights\": []\n  }\n}\n```",
                    "refusal": null
                },
                "logprobs": null,
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 1933,
            "completion_tokens": 345,
            "total_tokens": 2278,
            "prompt_tokens_details": {
                "cached_tokens": 1152,
                "audio_tokens": 0
            },
            "completion_tokens_details": {
                "reasoning_tokens": 0,
                "audio_tokens": 0,
                "accepted_prediction_tokens": 0,
                "rejected_prediction_tokens": 0
            }
        },
        "service_tier": "default",
        "system_fingerprint": "fp_7fcd609668"
    },
    "imagePath": null
}
````

Hvis du sender et billede via din RAG pipeline får du ikke umiddelbart det samme resultat tilbage. Der mangler en ordenlig promt. (og du mangler evt. også at kunne sende et billede til den model du bruger.)

* Opret en RAG pipeline der med brug af en relevant prompt kan få nogenlunde det samme response tilbage.