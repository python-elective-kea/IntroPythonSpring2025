# Tutorial - Github API

Denne tutorial viser dig hvordan du bruger Githubs API til at oprette et repository med en readme, .gitignore og en License fil, opdatere det eksisterende repo, og slette det igen. Dette sker først gennem Postman og herefter vha. python og dets `requests` modul.

Du kan godt springe Postman delene over hvis du føler dig velbevandret i disse dicipliner, og gå dirrekte til den sidste del omhandlende `requests`. 

## Tutorial:

For at oprette et nyt repository i en organisation på GitHub gennem API'en og postman, skal du følge disse trin: 

1. **Opret en Personal Access Token:** Først skal du oprette en 'Personal Access Token (classic)' på GitHub. Gå til dine indstillinger på GitHub, vælg 'Developer settings', og derefter 'Personal access tokens'. 
Klik på 'Generate new token', og sørg for at vælge de nødvendige omfang (scopes) for din token. For at oprette et repository som en almindelig bruger, skal du mindst have 'repo' adgang, men det er også en god ide at have delete rettigheder.
2. **Konfigurer din anmodning i Postman:**
    - Åbn Postman og opret en ny anmodning.
    - Vælg 'POST' som anmodningstype.
    - Indtast URL'en for API-anmodningen: **`https://api.github.com/user/repos`**.
    - Gå til 'Headers' fanen og tilføj en ny header med nøglen 'Authorization' og værdien 
    'token YOUR_PERSONAL_ACCESS_TOKEN'. Erstat **`YOUR_PERSONAL_ACCESS_TOKEN`** med din personlige adgangstoken.
    - Gå til 'Body' fanen, vælg 'raw' og 'JSON (application/json)'. Indtast derefter JSON-dataene for din anmodning. For eksempel:
    
    ```
    {
        "name": "intro_til_python",
        "description":"Demo repo til Github api øvelse",
        "private": false,
        "auto_init": true,
        "gitignore_template": "Python",
        "license_template": "mit"
    }
    ```

1. **Send anmodningen:** Klik på 'Send' knappen for at sende anmodningen.
    
    Hvis alt er i orden, vil du få et svar fra GitHub API med oplysningerne om det nyligt oprettede repository.
    
    Hvilken statuskode har du fået tilbage, og hvad betyder den?
    
2. **Find github clone url**: og clon dit nye repository til din egen computer. 
Dette skal du **ikke** bruge githubs api til, men kommandoen 
*git clone https://github.com/user/repo.git.*
Eller gennem det program du hidtil har brugt til at clone repositories.  

## Slet dit repository

For at slette et repository gennem GitHub API, skal du sende en DELETE-anmodning til følgende URL:

```jsx
https://api.github.com/repos/USERNAME/REPO_NAME
```

Erstat **`USERNAME`** med dit GitHub brugernavn og **`REPO_NAME`** med navnet på det repository, du ønsker at slette.

Her er hvordan du kan gøre det i Postman:

1. Åbn Postman og opret en ny anmodning.
2. Vælg 'DELETE' som anmodningstype.
3. Indtast URL'en for API-anmodningen: **`https://api.github.com/repos/USERNAME/REPO_NAME`**.
4. Gå til 'Headers' fanen og tilføj en ny header med nøglen 'Authorization' og værdien 'token YOUR_PERSONAL_ACCESS_TOKEN'. Erstat **`YOUR_PERSONAL_ACCESS_TOKEN`** med din personlige adgangstoken.
5. Klik på 'Send' knappen for at sende anmodningen.

Hvis alt er i orden, vil du få et 204 No Content svar fra GitHub API, hvilket betyder, at repository'et er blevet slettet.

Bemærk: Hvis du ikke kan slette, feks pga admin rettigheder skal du kigge på din accesstoken og om du har de rettighededer skal til.


## Brug githubs api via Python og `requests`    

Du skal først se følgende tutorial: [Interacting With REST APIs and Python](https://realpython.com/courses/interacting-rest-apis-python/)    
(Du skal kun se den gratis del af videoerne (1-5))

Herefter skal du oprette et github repository ved hjælp af pythons requests modul.
