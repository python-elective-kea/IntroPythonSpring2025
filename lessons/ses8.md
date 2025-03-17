# "Back to basics" - python one liners
I dag tager vi en "Back to basics" gang, hvor forkus bliver på Python kode og små programmeringsøvelser og Python one liners.


## Læringsmål
* Kunne bruge python list comprehensions
* Kunne bruge Python lambda expressions
* Kunne bruge ternary operators
* Kunne arbejde med fuctions
* Kunne arbejde med boolean logik
* Have forståelse for og kunne bruge python virtual environments gennem terminalen og i en notebook


## Forberedelse
Læs og lav følgende tutorial.

* [List comprehensions 101](https://mathspp.com/blog/pydonts/list-comprehensions-101)

Du skal desuden lave følgende øvelser inden vi mødes:

* [python basic øvelser](../materialer/ses8/exercises_prompt.md)
    * Du skal udskifte "python programming" i promptens første linie med henholdsvis:
        * "python functions"
        * "python boolean logic"
        * "python list comprehension"
        * "python lambda or ternary oprators"

Brug gerne 2 timer på disse øvelser.

## Dagen i dag

Vi starter dagen i dag med dette lille spil: (kommer umiddelbart inden undervisningen)

Intro: Watson Test
------------------

<small><i>Wason-test (Peter Cathcart Wason, 1966)</i></small>    
Consider 4 cards, where you can only see one side.      
On each card there is a number on one side and a letter on the other.     
Suppose you see the following 4 cards:     

![](../assets/card_chal.png)

Which cards do you need to turn over to determine if the following rule is correct?     
If there is a vowel on one side, then there is an even number on the other side.     

You get 5 minutes to thinks this through, and then we make some statistics at the black board, about your solutions.
Afterwards you have to create a script that takes 4 cards as input and checks in the shortest/fastests way if is 'valid' cards or not.


Herefter kigger vi på de helt basale dele af python functions, gennemgår nogle eksempler med list comprehensions. Blandt andet prøver vi at "flatening" den liste i lige har arbejdet med i øvelsen.

Vi kigger også på **lambda** eksempler og brug af **ternary oprators**.

## Materiale
* [List comprehensions 101](https://mathspp.com/blog/pydonts/list-comprehensions-101)
* [python basic øvelser](../materialer/ses8/exercises_prompt.md)

### Øvelser

#### 1. Watson test
I denne fil [watson_data.py](../materialer/ses8/watson_data.py) ligger der en lang liste a kort, som hver især ville kunne køres i gennem en "Watson test". Systemet i listen er:

``` 
    [
        (
            ('A', 2), ('K', 9), (4, 'B'), (7, 'K')
        ), 
        (
            (2, 'A'), ('V', 9), (3, 'C'), (9, 'L')
        ), 
        ...
    ]
``` 

Der er en liste med tupler der inderholder 4 kort. Hvert kort er en tuple og det første element i hver tuple er den synlige side af kortet, det andet element er den skjulte side. 

Du skal finde ud af:

1. Hvor mange set kort der i filen
2. I hvor man af sættene der er brug for at vende: 
    * alle kort
    * 3 kort
    * 2 kort
    * 1 kort
3. Hvor mange set vil fejle testen

Det vil nok være enten umuligt eller meget rodet at bruge list comprehensions til denne øvelse, så almindelige loops er fint. 

Du får en halv time til denne øvelse, og så gennemgår vi den ved tavlen inden vi går videre til næste emne.


#### 2. funktioner
Tænk over hver af følgende funktioner og bestem, hvad der er:

* returværdi
* returtype
* parametertype
* parameterværdi

**example1**

```
   def add(num1, num2):
        return num1 + num2
```

**example2**

```
   def add():
        print('Hello')
```

**example3** 

```
   def add():
        pass
```

**example4**

```
   def add(*args):
        return sum(args)
``` 

**example5**

```
   def msg(x, y):
        return x(y)
        
   # what does this one return, what are the parameters??
   msg(len, 'Hello')
```

#### 3. Apache log file
I den virksomhed hvor du arbejder har der på det seneste været en mistanke om at jeres websites har været under angreb fra ikke venligtsindet hackere. Du er blevet bedt om at kigge log filer igennem for at se om du kan identificere noget mistænkeligt. Man kan godt installere applikationer der kan lave denne analyse af jeres logfiler, men i første omgang vil det nemmeste være at bruge python til at lave en indledende undersøgelse. 

Undersøg denne [apache-log fil](../materialer/ses8/apache_log.txt) for om der har været:


#### **1. Mistænkelige IP-adresser**
- Find de mest hyppigt forekommende IP-adresser i logfilen.
- Identificér IP-adresser, der sender et stort antal forespørgsler inden for en kort tidsperiode (muligt DDoS-angreb).
- Sammenlign IP-adresserne med kendte sorte lister (f.eks. abuse-databaser).

#### **2. brute-force angreb**
- Analyser mislykkede login-forsøg til administrationspaneler (f.eks. `/wp-login.php`, `/admin`, `/login`).
- Identificér IP-adresser, der gentagne gange forsøger at tilgå login-sider.

#### **3. SQL-injektions**
- Søg efter typiske SQL-injektionsmønstre i URL-anmodninger (f.eks. `SELECT`, `UNION`, `' OR 1=1 --`).
- Identificér forespørgsler, der indeholder kodede SQL-payloads.

#### **4. web shell-uploads**
- Søg efter filuploads, der målretter sig mod `.php`, `.jsp` eller andre eksekverbare scripts.
- Identificér usædvanlig adgang til mapper som `/uploads/` eller `/tmp/`.

#### **5. XSS (Cross-Site Scripting) angreb**
- Søg efter `<script>`, `javascript:`, `onerror=alert(1)`, og andre scriptbaserede payloads i forespørgsler.

#### **6. Mistænkelige User-Agent headers**
- Identificér forespørgsler med mistænkelige eller tomme User-Agent headers.
- Find bots, der udgiver sig for at være legitime browsere.

#### **7. Directory Traversal-angreb**
- Søg efter forsøg på at tilgå følsomme filer via `../../../etc/passwd` eller `../admin/`.

#### **8. HTTP-status koder**
- Identificér en stor mængde 404-fejl (muligt forsøg på at finde skjulte filer).
- Find hyppige 403-fejl (forsøg på uautoriseret adgang).
- Spot mange 500-fejl (mulige sårbarheder i webapplikationen).

#### **9. Forsøg på manipulation af logfiler**
- Søg efter usædvanlige logposter, manglende tidsstempler eller ændrede data.

#### **10. Undersøg usædvanlige trafikmønstre**
- Identificér overdreven trafik til en enkelt side.
- Undersøg, om der er trafikspidser, der sammenfalder med sikkerhedshændelser.


Brug som udgangspunkt **list comprehesions**, **lambda expression** og i det hele taget 'one-liners'

Logfilen finder du her [apache-log.txt](../materialer/ses8/apache_log.txt)

