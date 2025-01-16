# Data Science Tools: Numpy, Pandas og Matplotlib: Intro til moduler
![](../assests/vector_matrix_tensor.png)

I dag tager vi hul på dataanalyse delen af dette valgfag. Vi starter med at lære 3 biblioteker at kende: **Numpy**, **Pandas** og **Matplotlib**. Numpy er et akronym for "Numerical Python", Pandas for "Panel Data" og "Matplotlib" kunne vel tolkes som "Mathmatical Plotting Library", selvom det mere korrekt er "MATLAB plotting Library".

"Numerical" peger på at biblioteket bruges til tal og beregninger. Så numpy er et bibliotek til at arbejde med tal, Statistik, linier algebra mm. "Panel Data" er et begreb fra statistik og økonomi, der refererer til multidimensionelle datasæt.    
Matplotlib bibliotekets formål er at generere visuelle grafer og diagrammer, ofte baseret på det data man har arbejdet med i numpy og pandas.

## Læringsmål
* Kunne bruge biblioteket Numpy
* Have viden om biblioteket Pandas
* Kunne bruge biblioteket Matplotlib

## Forberedels
_(forberedelse til i dag er på omkring 3 timer)_    

Se først denne korte introduktion til hvad modulerne **Numpy** og **Pandas** er og hvad de bruges til:

* [NumPy vs Pandas](https://www.youtube.com/watch?v=KHoEbRH46Zk) (5:54)

Resten af denne uges sessioner bruger vi på **Numpy** og **Matplotlib**, mens **Pandas** er fokusområdet for næste uge. 

Gå nu videre med denne introduktion til Numpy:
* [Python NumPy Tutorial for Beginners](https://www.youtube.com/watch?v=QUT1VHiLmmI) (58:09)

Herefter skal du træne brugen af numpy vha. af følgende prompt.

> PROMPT: "I want to practice Python exercises focusing on the NumPy library. Each exercise should cover one of the following topics: creating a NumPy array, manipulating arrays, or applying mathematical operations on arrays.
> Please give me one exercise at a time. After I submit my solution, evaluate my answer, provide constructive feedback, and grade it on a scale of 1 to 10. Based on my performance, adjust the difficulty level of the next exercise to either be harder or easier."

Til sidst skal du se denne video om Matplotlib:

* [Matplotlib Tutorial: For Physicists, Engineers, and Mathematicians](https://www.youtube.com/watch?v=cTJBJH8hacc&list=PLkdGijFCNuVnGxo-1fSNcdHh5gZc17oRM) (47:59)

OBS: Han starter  med at beskrive et modul der skal installeres (SciencePlots). Det er ikke nødvendigt, så bare undlad dette. 


<!--
* [Intro to Data Visualization in Python with Matplotlib! (line graph, bar chart, title, labels, size)](https://www.youtube.com/watch?v=DAQNHzOcO5A) (32:32)
-->


## Dagen i dag


Vi starter med at opsumere hvad i har været igennem i forberedelsen. 

* [NumPy Tutorial.ipynb](https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb)
* [Matplotlib Tutorial.ipynb](https://github.com/KeithGalli/matplotlib_tutorial/blob/master/Matplotlib%20Tutorial.ipynb)

I skal også lære at bruge [numpy](https://numpy.org/doc/stable/user/absolute_beginners.html) og [matplotlibs](https://matplotlib.org/stable/) dokumentation.

## Materialeliste
* [NumPy vs Pandas](https://www.youtube.com/watch?v=KHoEbRH46Zk)
* [Numpy dokumentation](https://numpy.org/doc/stable/user/absolute_beginners.html)
* [Matplotlib dokumentation](https://matplotlib.org/stable/)
* [Intro to Data Visualization in Python with Matplotlib! (line graph, bar chart, title, labels, size)](https://www.youtube.com/watch?v=DAQNHzOcO5A) (32:32)
* [Python NumPy Tutorial for Beginners](https://www.youtube.com/watch?v=QUT1VHiLmmI) (58:09)
* [NumPy Tutorial.ipynb](https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb)
* [Matplotlib Tutorial.ipynb](https://github.com/KeithGalli/matplotlib_tutorial/blob/master/Matplotlib%20Tutorial.ipynb)

<!-- 
* [NumPy Tutorial: Your First Steps Into Data Science in Python](https://realpython.com/numpy-tutorial/#hello-numpy-curving-test-grades-tutorial)
-->

### Øvelser

### Øv 1: Numpy, Matplotlib og linær regressions analyse
Start med at downloade disse fire filer:
* [Data 1](../assests/data1.tsv), [Data 2](../assests/data2.tsv), [Data 3](../assests/data3.tsv), og [Data 4](../assests/data4.tsv).    
Formatet er _.tsv_ og det står for _tab seperated values_. Som du senere vil finde ud af grunden til er disse dataset berømte! Hver fil har to kolonner (adskilt med tab-tegnet). Den første kolonne er x-værdier, og den anden kolonne er y-værdier.    

Det er ok bare at højreklikke på filerne og derefter sige ja til at downloade dem, men det er sjovere at bruge python til det. Men du bestemmer.     

**Og nu til selve øvelsen:**    

1. Brug `numpy` funktionen `mean` til at beregne gennemsnittet af både x-værdier og y-værdier for hvert datasæt. For at formatere resultaterne med præcis 2 decimaler, skal du bruge Python f-string.
2. Beregn nu variansen for alle de forskellige sæt af x- og y-værdier ved at bruge `numpy` funktionen `var`. Print det med tre decimaler.


### Øv Numpy

* [Python Plotting With Matplotlib (Guide)
](https://realpython.com/python-matplotlib-guide/)
