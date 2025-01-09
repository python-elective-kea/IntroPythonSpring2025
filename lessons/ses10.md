# Dataanalyse med numpy, pandas og matplotlib: Intro til moduler
I dag tager vi hul på dataanalyse delen af dette valgfag. Vi starter med at lære 3 biblioteker at kende: **Numpy**, **Pandas** og **Matplotlib**. Numpy er et akronym for "Numerical Python", Pandas for "Panel Data" og "Matplotlib" kunne vel tolkes som "Mathmatical Plotting Library", selvom det mere korrekt er "MATLAB plotting Library".

"Numerical" peger på at biblioteket bruges til tal og beregninger. Så numpy er et bibliotek til at arbejde med tal, Statistik, linier algebra mm. "Panel Data" er et begreb fra statistik og økonomi, der refererer til multidimensionelle datasæt.    
Matplotlib bibliotekets formål er at generere visuelle grafer og diagrammer, ofte baseret på det data man har arbejdet med i numpy og pandas.

## Læringsmål
* Kunne bruge biblioteket Numpy
* Kunne bruge biblioteket Pandas
* Kunne bruge biblioteket Matplotlib

## Forberedelse
Se først denne korte introduktion til hvad modulerne **Numpy** og **Pandas** er og hvad de bruges til:

* [NumPy vs Pandas](https://www.youtube.com/watch?v=KHoEbRH46Zk) (5:54)

Herefter kig på denne introduktion til hvad Matplolib biblioteket kan bruges til:
* [Intro to Data Visualization in Python with Matplotlib! (line graph, bar chart, title, labels, size)](https://www.youtube.com/watch?v=DAQNHzOcO5A) (32:32)

Den næste tutorial handler om **Numpy** og om mere detaljeret brug af modulet.

* [Complete Python NumPy Tutorial (Creating Arrays, Indexing, Math, Statistics, Reshaping)](https://www.youtube.com/watch?v=GB9ByFAIAH4) (58:40)

<!--
Herefter skal du træne brugen af numpy vha. af følgende prompt.

> PROMPT: "I would like to have some exercises in python covering the Numpy library. Each exercise should include one of the following topics: Creating a numpy array,. All exercises should make a relation between the for loop approch vs the comprehesion approach. You should give me one exercise at the time, and then evaluate my answer and grade it with a grade from 1 to 10. Then give me another exercise that is either harder or easier based on the evaluation and grade you gave me."
-->

Som det sidste i forberedelsen skal du lære om modulet **Pandas**:

* []()





## Dagen i dag

## Materiale
* []()
* [Video: Numpy]()
* [Video: Pandas]()
* [Video: Matplotlib]()
* [NumPy vs Pandas](https://www.youtube.com/watch?v=KHoEbRH46Zk)
* [Numpy dokumentation](https://numpy.org/doc/stable/user/absolute_beginners.html)
* [Matplotlib dokumentation](https://matplotlib.org/stable/)
* [Word2vec](https://en.wikipedia.org/wiki/Word2vec)
* [Regression](https://www.webmatematik.dk/lektioner/matematik-b/regression)
* [iGensim](https://radimrehurek.com/gensim/)
* [Python Statistics Fundamentals: How to Describe Your Data](https://realpython.com/python-statistics/)
* [NumPy Tutorial: Your First Steps Into Data Science in Python](https://realpython.com/numpy-tutorial/#hello-numpy-curving-test-grades-tutorial)

### Øvelser
### Øv 1: Numpy, Matplotlib og linær regressions analyse
Start med at downloade disse fire filer:
* [Data 1](../assests/data1.tsv), [Data 2](../assests/data2.tsv), [Data 3](../assests/data3.tsv), og [Data 4](../assests/data4.tsv).    
Formatet er _.tsv_ og det står for _tab seperated values_. Som du senere vil finde ud af grunden til er disse dataset berømte! Hver fil har to kolonner (adskilt med tab-tegnet). Den første kolonne er x-værdier, og den anden kolonne er y-værdier.    

Det er ok bare at højreklikke på filerne og derefter sige ja til at downloade dem, men det er sjovere at bruge python til det. Men du bestemmer.     

**Og nu til selve øvelsen:**    

1. Brug `numpy` funktionen `mean` til at beregne gennemsnittet af både x-værdier og y-værdier for hvert datasæt. For at formatere resultaterne med præcis 2 decimaler, skal du bruge Python f-string.
2. Beregn nu variansen for alle de forskellige sæt af x- og y-værdier ved at bruge `numpy` funktionen `var`. Print det med tre decimaler.

### Øv 2: Dataanalyse med Pandas

I den næste øvelse skal du arbejde med biblioteket [Pandas](https://www.w3schools.com/python/pandas/default.asp). 

Vi kommer til at bruge dette bibliotek løbende gennem dette semesteret, både i dette fag,  men også med Michael sammen med programmet Tableau. Men lige nu skal i bare lege med det. 

I kan enten først kigge på denne simple tutorial [Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp), eller i kan  hoppe dirrekte til øvelsen herunder og så bruge tutorialen som opslagsværk. I bestemmer selv.

* [Dataanalyse af San Fransisco crime data](https://github.com/ITAKEA/kode_fra_undervisning_e24/tree/master/python3/Pandas_SF_Crime/exercise_pandas_sf.ipynb)


### Øv Numpy

* [NumPy Practical Examples: Useful Techniques](https://realpython.com/numpy-example/#numpy-example-4-writing-your-own-vectorized-functions)

* [Python Plotting With Matplotlib (Guide)
](https://realpython.com/python-matplotlib-guide/)

### Øv prompt
Copy/paste følgende prompt ind i chatgpt (eller lign llm). Prompten virker bedst i gpt4o.

> Can you give me some exercises in python regarding the use of the Pandas library. 
You should give me one exercise at the time, and then evaluate my answer to the exercise from 1 to 10,
and then give me another exercise that is either harder or easier based on the evaluation you did.