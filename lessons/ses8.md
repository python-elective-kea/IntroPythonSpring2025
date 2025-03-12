# "Back to basics" - python one liners
I dag tager vi en "Back to basics" gang, hvor forkus bliver på Python kode og små programmeringsøvelser og Python one liners.


## Læringsmål
* Kunne bruge python list comprehensions
* Kunne bruge Python lambda expressions
* Kunne arbejde med fuctions
* Kunne arbejde med decorators
* kunne arbejde med context managers
* Have forståelse for python virtual environments


## Forberedelse



## Dagen i dag

Vi starter dagen i dag med denne lille test:

Intro: Watson Test
------------------

Wason-test (Peter Cathcart Wason, 1966).     
Consider 4 cards, where you can only see one side.      
On each card there is a number on one side and a letter on the other.     
Suppose you see the following 4 cards:     

![](../assets/card_chal.png)

Which cards do you need to turn over to determine if the following rule is correct?     
If there is a vowel on one side, then there is an even number on the other side.     

You get 5 minutes to thinks this through, and then we make some statistics at the black board, about your solutions.
Afterwards you have to create a script that takes 4 cards as input and checks in the shortest/fastests way if is 'valid' cards or not.



## Materiale



### Øvelser

#### 1. Watson test
I denne fil [Watson test]() ligger der en lang liste a kort, som hver især ville kunne køres i gennem en "Watson test".

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

Du skal finde ud af:

* Hvor mange set kort der i filen
* I hvor man af sættene der er brug for at vende: 
    * alle kort
    * 3 kort
    * 2 kort
    * 1 kort
* Hvor mange set vil fejle testen

Prøv så vidt muligt at gøre brug af python "one-liners" til dine løsninger. 

#### 1. Apache log file
I den virksomhed hvor du arbejder har der på det seneste været en mistanke om at jeres websites har været under angreb fra ikke venligtsindet hackere. Du er blevet bedt om at kigge log filer igennem for at se om du kan identificere noget mistænkeligt. Man kan godt installere applikationer der kan lave denne analyse på jeres logfiler, men i første omgang vil det nemmeste være at bruge python til at lave en indledende undersøgelse. 

Derfor skal du med undersøge denne apache-log fil for om der har været:

* mistænkelige login forsøg (`/login`) som man måske skulle gøre noget ved.
*  

Du skal når det giver mening bruge list comprehesions, lambda expression og i det hele taget 'one-liners'

Logfilen finder du her [apache-log.txt]()
