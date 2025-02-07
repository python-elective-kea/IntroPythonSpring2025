# Python modules
 I dag skal i arbejde med python kode andre folk har lavet og som i importerer og bruger i jeres egne applikationer. For at i kan det skal i vide lidt om moduler og packages, og i skal vide noget om hvad et virtuelt miljø er og hvordan i opretter det, installerer pakker i det og sørger for at holde styr på de installerede og håndterer jeres projekters requirements.

## Læringsmål

* Kunne arbejde med filer i python
* Kende til og kunne bruge pythons ```import``` statement 
* Lave egne moduler
* Lave egne packages
* Kende til forskellen på moduler og packages
* Importere egne, build-in og 3. parts -moduler
* Installere 3. parts moduler med ```pip```
* Forstå hvad et 'virtual environment' er og kunne oprette dem fra kommandolinien og gennem VSCode gui.
* Kunne arbejde med dependencies og requirements.txt filen
* Kunne lave kode der gør brug af pythons ```requests``` module.

## Forberedelse

Start med at læse denne [LLM vejledning](../materialer/ses2/godLLM.md)

Se følgende videoer om moduler og pakker, og læs dokumentet om at arbejde med filer.    

* [Moduler og pakker i python 1 (egne moduler)](https://youtu.be/miGblWWfsvY) (8:37)
* [Moduler og pakker i python 2 (indbyggede)](https://youtu.be/sEvWF1YLxXs) (6:12)
* [Moduler og pakker i python 3 (3. parts)](https://youtu.be/wbEWDsj3vIg) (8:20)
* [Text Files in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=4mX0uPQFLDU&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=31) (6:18)

> PROMPT: "I would like to have some exercises in python covering "Text files in python". Each exercise should include one of the following topics: Opening files, file modes (r, w, a), with, help, dir. You should give me one exercise at the time, and then evaluate my answer and grade it with a grade from 1 to 10. Then give me another exercise that is either harder or easier based on the evaluation and grade you gave me."

<!-- 
* [Arbejd med filer i Python](materialer/filer.html) (5:00)
-->

* [Using Python's pip to Manage Your Projects' Dependencies](https://realpython.com/what-is-pip/) (45:00)
    * Sørg for at forstå starten af hver afsnit i denne artikkel. Hen imod slutningen af hvert afsnit bliver det mere og mere detaljeret. Det er fint at i bare har skimmet det, og derved kan finde tilbage til det hvis i får brug for det. Så ... relativ god forståelse af hovedpointerne fra hvert afsnit, og overblik over resten.

## Dagen i dag
<!-- Vi starter med en lille [quiz](../exercises/ses3/opvarmning/moduler.ipynb) for at tjekke om i har forstået forberedelsesmaterialet.   --> 
Vi starter dagen med en kort opsumering af det i har set hjemme inden undervisningen.    

Herefter laver vi en [øvelse/demo](../materialer/ses3/requirements_demo/) der viser hvorfor vi skal bruge `requirements.txt` filen i vores projekter.     

Så kigger vi på 3 moduler ```OS```, ```subprocess``` og ```requests```.


## Materialer
* [Arbejd med filer i Python](../materialer/ses3/filer.ipynb)
* [Moduler og pakker i python 1 (egne moduler)](https://youtu.be/miGblWWfsvY) (8:37)
* [Moduler og pakker i python 2 (indbyggede)](https://youtu.be/sEvWF1YLxXs) (6:12)
* [Moduler og pakker i python 3 (3. parts)](https://youtu.be/wbEWDsj3vIg) (8:20)
* [Python Module Index](https://docs.python.org/3/py-modindex.html) 
* [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/)

## Øvelser

### Øv 1: Environment variabler og OS modulet
Du har set at ved `import os` har adgang til et modul der indeholder en masse funktioner som kan bruges til interaktion og manipulation af fil- og operativsystem.

Vi kommer snart til at skulle bruge **API tokens** i vores kode til 'Authorization' i forhold til forskellige LLM API´er.

Når vi arbejder med Authorization tokens skal de gemmes i environment variables. 

Du skal i første omgang gemme en miljøvariabel i en celle, og læse den samme variable fra en efterfølgende celle.

Når du har styr på det skal vi gemme varablen i en anden fil.

* I OS modulet find de funktioner der skriver og læser miljøvariabler, og få det til at virke.


I VS Code kan vi oprette en fil `.env` hvor i vi kan gemme vores environment variabler. Denne `.env` fil kan vi så skrive i vores `.gitignore` fil, og derved undgå deling af den hemmelige nøgle på Github.

* Lav en `.env` fil i roden af dit projekt, og skriv din environment variable i denne fil på formen **API_KEY=1234asdf4w4w**     

* ignorer denne `.env` fil i din `.gitignore` fil

Læs nu denne environmen variabel fra din .env fil og brug den i din notebook i stedet for at skrive den dirrekte i en celle.

Til dette skal du bruge modulet `python-dotenv`.

### Øv 2: Subprocess
Til denne øvelse skal du bruge subprocess modulet.     
[The subprocess Module: Wrapping Programs With Python](https://realpython.com/python-subprocess/)

* Clone dette respository: https://github.com/python-elective-kea/spring2024.git
* åben her etfer `index.html` filen fra `docs` mappen i din browser.

Det hele skal selvfølgelig kodes, ikke noget med feks. manuelt at klikke på index.html filen.

### Øv 3:Requests, json og Github API

* [Lav denne tutorial](../materialer/ses3/tutorial_github_api.md)


### Øv 4: CSV

* Læs [reviews.csv](/materialer/ses3/reviews.csv) filen vha. `csv` modulet.    
* Udskriv reviews kollonen (kun reviews kollonnen!)
<!-- 
### Øv 5: Download filer
I denne øvelse skal du lave et script som kan læse filer fra nettet og gemme dem i en fil i en mappe på din computer.

**Lav et modul (.py fil) som:**     
* Opretter en mappe på din computer
* Læs [denne fil](https://itakea.github.io/e24_swa/py_intro_3.html) og gem den i mappen
* Åbner filen i din browser

Når det fungerer kan du se at der mangler stylesheets til siden:

Ændre koden i dit script så det samtidigt
* læser hvert stylesheet ([feks. dette](https://itakea.github.io/e24_swa/_static/css/custom.css?v=a5898925)) 
* Ændrer `<link rel="stylesheet" type="text/css" >` attributterne på html siden til at pege på de filer du har downloaded.

Øvelsen skal laves med det vi har været igennem indtil nu. Modulerne fra i dag, string manipulation (herunder slicing) etc.    
Hvis i spørger en ven, vil den sikkert foreslå en masse andre moduler (feks. `Beautifull Soup`). Det skal i ikke bruge til denne øvelse!

I opfordres til at følge **KISS** designprincippet. **Keep it simple stupid**. Altså start med at lave det så simpelt som overhoved muligt. Lad vær med at ville tilføje alt muligt andet funktionalitet end det der står i kravene, og det der er allemest nødvendigt. 
>

