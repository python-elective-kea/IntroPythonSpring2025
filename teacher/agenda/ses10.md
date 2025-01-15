
# Agenda ses 10 (datascience tools)

Fokus i dag ligger på at bruge matplotlib og numpy (og på modulet Pandas). Fokus er altså på at bruge 2(3) moduler.  
Dataanalyse med brug af **pandas** modulet og **matplotlib** kommer næste uge.


## Matplotlib

Dokumentation: https://matplotlib.org/3.5.0/index.html

* Forklar hvordan disse elementer laves udfra dette image

![](https://matplotlib.org/3.5.0/_images/anatomy.png)


**figure**
* En Figure er hele det visuelle objekt, se det som et lærred.

````
plt.figure()
````


**Axes**
* 


**subplot** (pyplot-style)    

````
# Create a 2x2 grid of subplots
plt.subplot(2, 2, 1)  # Top-left
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Plot 1")

plt.subplot(2, 2, 2)  # Top-right
plt.plot([1, 2, 3], [3, 6, 9])
plt.title("Plot 2")

````



### pyplot vs OO-style

**subplot vs subplots**
forklar hvorfor supplots, vis forskellen på med og uden subplots

```
fig, ax = plt.subplot() # en figure med en axes
fig, ax = plt.subplot(2,2) # a figure with a 2x2 grid of Axes
```
