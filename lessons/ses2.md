# Python - Datastrukture

I dag skal vi arbejde med pythons datastrukturer. Python har som udgangspunkt kun fire indbyggede datastrukture. Det er Lister, Tuples, Sets og Dictionaries.     
Efter i dag vil i være i stand til at oprette  Listes og Tupler, tilgå deres elementer vha. deres index, bruge pythons slicing værktøj på lister og tupler, bruge arethmetikske operatore på lister og tupler, bruge pythons indbyggede functioner på lister og tupler, arbejde med metoderne tilknyttet list og tuple objekterne, og i vil have en grundlæggende forståelse for forskellen i brugen af disse 2.     
I vil kunne bruge Sets til at finde unikke værdier i en collection, og i vil arbejde med Dictionaries og forstå dens key : Value struktur.

## Læringsmål
---        
- Arbejde med lister, tuples, dicts og sets
    - Arbejde med deres indeks
    - Bruge slicing syntaksen
- Kende til de vigtigste forskelle mellem lister, tuples, sets og dictionaries
- 

## Forberedelse
---
Før vi mødes i klassen skal du have set følgende videoer og løst de tilhørende forståelses opgaver vha. ChatGpt Prompten under linkene:

* [Python Lists || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=ohCDWZgNIU0) (5:43)
   
> PROMPT: "I would like to have exercises in Python that focus on lists. Each exercise should cover one of the following topics: creating a list, accessing list elements, slicing, list methods, and using help() and dir(). Please give me one exercise at a time, evaluate my answer, and assign a grade from 1 to 10. Based on the evaluation and grade, provide me with another exercise that is either more challenging or easier." 

* [Python Tuples || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=NI26dqhs2Rk&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=16) (7:43)

> PROMPT: "I would like to have exercises in Python that focus on tuples. Each exercise should cover one of the following topics: Creating a tuple, getting tuple elements, unpacking tuples, help() and dir(). Please give me one exercise at a time, evaluate my answer, and assign a grade from 1 to 10. Based on the evaluation and grade, provide me with another exercise that is either more challenging or easier."

* [Sets in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=sBvaPopWOmQ&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=13) (6:33)

> PROMPT: "I would like to have exercises in Python that focus on Sets. Each exercise should cover one of the following topics: Creating a set, set methods (add, remove, discard), union, intersection, using the in operator, help() and dir(). Please give me one exercise at a time, evaluate my answer, and assign a grade from 1 to 10. Based on the evaluation and grade, provide me with another exercise that is either more challenging or easier."

* [Python Dictionaries || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=XCcpzWs-CI4&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=15) (6:08)

> PROMPT: "I would like to have some exercises in python covering Dictionaries. Each exercise should include one of the following topics: Creating a dictionary, adding elements, access elements, using the in operator, try/except errors, get(), keys(), values(), items(), help() and dir(). You should give me one exercise at the time, and then evaluate my answer and grade it with a grade from 1 to 10. Then give me another exercise that is either harder or easier based on the evaluation and grade you gave me."

* [10 Python Comprehensions You SHOULD Be Using](https://www.youtube.com/watch?v=twxE0dEp3qQ)

> PROMPT: "I would like to have some exercises in python covering List Comprehensions. Each exercise should include one of the following topics: basic comprehension, if conditions, if/else conditions, nested loops, caling functions inside a comprehension. All exercises should make a relation between the for loop approch vs the comprehesion approach. You should give me one exercise at the time, and then evaluate my answer and grade it with a grade from 1 to 10. Then give me another exercise that is either harder or easier based on the evaluation and grade you gave me."

## Dagens indhold
---

Vi starter med denne:

* [opvarmningsøvelse](../exercises/ses2/ses2_warm_up.ipynb) 

Så snakker vi kort om hvorfor der er 4 datastrukture i python, og hvad de kan bruges til. 

Herefter arbejder vi ping pong med øvelerne til i dag.

* [list1](../exercises/ses2/list1.ipynb))
* [list2](../exercises/ses2/list2.ipynb)
* [Dictionary](../exercises/ses2/dict.ipynb)
* [Set](../exercises/ses2/set.ipynb)

## Materialer
---

* [Kodeeksempler fra undervisningen](../exercises/ses2/codeexamples.ipynb)
* [Python Course at Kaggle](https://www.kaggle.com/code/colinmorris/hello-python)

### Øvelser
---
#### Ex 0.1: Slicing
---
By using the slicing syntax change the following collections.

After slicing:

```
['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
'Hello World Huston we are here' -> 'World Huston we'
``` 

Figure out more on your own and practice this a lot!    

   <hr>

### Ex 1.1: Is it a tuple or a list?
---
The following data should be presented as either a list or a tuple, or as a combination of both.      
Your job is to choose the right one.     
Hint: A list is a collection of the same type of data, a tuple is a record (e.g. in a database a **record** is called a **row**)     

1. Claus, 51, male, clbo@kea.dk, 31011970-1313
2. Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo
3. Claus, Henning, Torben, Carl, Tine
4. 'Hello', 'World', 'Huston', 'we', 'are', 'here'
5. Rolling Stones, Goats Head Soup, 31 August 1973, 46:56
6. 40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan;
   
   <hr>

### List & Tuples, Set, Dict øvelser
---
* [list1](../exercises/ses2/list1.ipynb))
* [list2](../exercises/ses2/list2.ipynb)
* [Dictionary](../exercises/ses2/dict.ipynb)
* [Set](../exercises/ses2/set.ipynb)

#### quizes
* [Lists and Tuples Quiz](https://realpython.com/quizzes/python-lists-tuples/)
* ["while" Loops Quiz](https://realpython.com/quizzes/python-while-loop/)
