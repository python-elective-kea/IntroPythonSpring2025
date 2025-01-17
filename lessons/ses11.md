# Dataanalyse med numpy, pandas og matplotlib

## Læringsmål
* Kunne bruge biblioteket Numpy
* Kunne bruge biblioteket Pandas
* Kunne bruge biblioteket Matplotlib

## Forberedels  
Denne tutotial er lang og du kan vælge at "skimme" dele af den igennem, men sørg for som udgangspunkt at have en god forståelse for hvordan du bruger **Pandas**.

* [Complete Python Pandas Data Science Tutorial! (2024 Updated Edition)](https://www.youtube.com/watch?v=2uvysYbKdjM) (1:34:10)
## Dagen i dag




## Materiale
* [Numpy dokumentation](https://numpy.org/doc/stable/user/absolute_beginners.html)
* [Matplotlib dokumentation](https://matplotlib.org/stable/)
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

I kan enten først kigge på denne simple tutorial [Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp), eller i kan  hoppe dirrekte til øvelsen herunder og så bruge tutorialen som opslagsværk. I bestemmer selv.

* [Dataanalyse af San Fransisco crime data](https://github.com/ITAKEA/kode_fra_undervisning_e24/tree/master/python3/Pandas_SF_Crime/exercise_pandas_sf.ipynb)


### Tutorials
Som det sidste skal i gennemgå disse 2 tutorials. Den ene om Numpy, den anden om Matplotlib. Jeg (Claus) har været igennem dele af materialet i mine gennemgange af stoffet i klassen, så i kan se det som en slags "opfrisker". Ud over det går begge tutorials lidt mere i dybden med begge biblioteker. 

* [NumPy Tutorial: Your First Steps Into Data Science in Python](https://realpython.com/numpy-tutorial/)
* [Python Plotting With Matplotlib (Guide)](https://realpython.com/python-matplotlib-guide/)
