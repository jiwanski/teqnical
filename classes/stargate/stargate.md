# Stargate dial-up

Funkcja `stargate()` ma wydrukować następujące zachowania w Stargate Command podczas wykręcania gwiezdnego adresu:

1. komentarz Stargate Command, z reguły typu:
  
  `[Stargate Command] miejmy nadzieję, że PRZYJACIEL pomoże nam przeciwko WROGOWI`

2. sekwencję wykręcania adresu z kolejnymi numerami i podanym **chevronem**
  * przy 7 lub więcej chevronach, ostatni jest raportowany jako _locked_
  * wszystkie inne jako _encoded_:


```haskell
chevron 1 encoded (q)
chevron 2 encoded (h)
chevron 3 encoded (o)
chevron 4 encoded (e)
chevron 5 encoded (t)
chevron 6 encoded (f)
chevron 7 locked (b)
```

3. komentarz SG-1 oparty na liczbie **chevrons** i wartości ostatniego z nich, np. przy czterech:

`[SG-1] oh, for crying out loud!`

## argumenty funkcji stargate()

* dowolna ilość liter oraz _earth_, która **powinna** być ostatnim _chevronem_
* określenia 
  * **wroga** (opcjonalnie), domyślny to _Goa'uld_
  * **sprzymierzeńca** (obowiązkowo)
  
Brak sprzymierzeńca powoduje print wiadomości:

   `brak sprzymierzeńców przeciwko WROGOWI, gra skończona`
    
i przerwanie wykonywania funkcji

### przykład

```python
stargate('q', 'h', 'o', 'e', 't', 'f', 'earth',  ally="Asgard", enemy="Ori")
```

```haskell
[Stargate Command] let's hope Asgard will help us against Ori
chevron 1 encoded (q)
chevron 2 encoded (h)
chevron 3 encoded (o)
chevron 4 encoded (e)
chevron 5 encoded (t)
chevron 6 encoded (f)
chevron 7 locked (earth)
[SG-1] indeed
```
   

## logika odpowiedzi SG-1

| liczba chevrons                         | reakcja               |
|-----------------------------------------|-----------------------|
| poniżej 7                               | O'Neill wkurzony      |
| 7 lub więcej, ale ostatni to nie Ziemia | Carter zaniepokojona  |
| 7 i ostatni to Ziemia                   | Tea'lc zadowolony     |
| więcej niż 7 i ostatni to Ziemia        | Jackson zaintrygowany |

## definicje na start

```python
SG1 = {
    "oneill": "oh, for crying out loud!",
    "tealc": "indeed",
    "carter": "colonel...",
    "jackson": "maybe it's not such a bad idea?"
}
chevron = ['locked', 'encoded']

def stargate():
    pass
```

## dalsze przykłady:

### 1

```python
stargate('i', 's', ally="Asgard", enemy="Replicators")
```

```haskell
[Stargate Command] let's hope Asgard will help us against Replicators
chevron 1 encoded (i)
chevron 2 encoded (s)
[SG-1] oh, for crying out loud!
```

### 2

```python
stargate('q', 'h', 'o', 'e', 't', 'f', 'earth',  ally="Tok'ra")
```

```haskell
[Stargate Command] let's hope Tok'ra will help us against Goa'uld
chevron 1 encoded (q)
chevron 2 encoded (h)
chevron 3 encoded (o)
chevron 4 encoded (e)
chevron 5 encoded (t)
chevron 6 encoded (f)
chevron 7 locked (earth)
[SG-1] indeed
```

### 3

```python
stargate('a', 'b', 'c', 'd', 'e', 'f', 'a',  ally="Nox", enemy="Wraith")
```

```haskell
[Stargate Command] let's hope Nox will help us against Wraith
chevron 1 encoded (a)
chevron 2 encoded (b)
chevron 3 encoded (c)
chevron 4 encoded (d)
chevron 5 encoded (e)
chevron 6 encoded (f)
chevron 7 locked (a)
[SG-1] colonel...
```

### 4

```python
stargate('z', 'x', 'c', 'd', 't', 'f', 'y', 'earth',  ally="Tollan")
```

```haskell
[Stargate Command] let's hope Tollan will help us against Goa'uld
chevron 1 encoded (z)
chevron 2 encoded (x)
chevron 3 encoded (c)
chevron 4 encoded (d)
chevron 5 encoded (t)
chevron 6 encoded (f)
chevron 7 encoded (y)
chevron 8 locked (earth)
[SG-1] maybe it's not such a bad idea?
```

### 5

```python
stargate('t', 'y', 'u', 'd', 'k', 'f', 'y', 'x',  ally="Tok'ra", enemy="Ori")
```

```haskell
[Stargate Command] let's hope Tok'ra will help us against Ori
chevron 1 encoded (t)
chevron 2 encoded (y)
chevron 3 encoded (u)
chevron 4 encoded (d)
chevron 5 encoded (k)
chevron 6 encoded (f)
chevron 7 encoded (y)
chevron 8 locked (x)
[SG-1] colonel...
```


### 6

```python
stargate('t', 'y', 'u', 'd', 'k', 'f', 'y', 'x')
```

```haskell
[Stargate Command] no allies against Goa'uld, game over
```
