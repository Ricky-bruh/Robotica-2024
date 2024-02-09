#!/usr/bin/env python
# coding: utf-8

# # Il Primo Programma #

# ## Variabili ed Input Utente ##

# In[4]:


nome = input("Inserisci il tuo nome: ")
print("Ciao", nome, "!")


# In[5]:


nome = "Edoardo"
print(nome)


# In[7]:


Via = input("Inserisci nome della via")
print("Hai inserito", Via)


# Ripetere il codice più volte

# In[12]:


nome = input("Inserisci il tuo nome: ")
for contatore in range(3):
    print("Ciao", nome, "!") #Ripeterà solo quello dentro l'indentazione


# # Calcolatrice Python #

# ## Addizione ##

# In[16]:


numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
somma = numero1 + numero2
print("La somma è:", somma)


# ## Sottrazione ##

# In[17]:


sottrazione = numero1 - numero2
print("La sottrazioneè:", sottrazione)


# ## Moltiplicazione ##

# In[18]:


numero1 = int(input("Inserisci il pirmo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
moltiplicazione = numero1 * numero2
print("La moltiplicazione è:", moltiplicazione)


# ## Divisione ##

# In[23]:


numero1 = int(input("Inserisci il pirmo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
divisione = numero1 / numero2
print("La divisione è:", divisione)


# # Loop e Ripetizione #

# In[25]:


for numero in range(11): #il range parte da 0 ed arriva a 11
    print(numero)


# In[26]:


for numero in range(1,11): #il range parte da 1 ed arriva a 11
    print(numero)


# # Condizioni e Decisioni #

# In[8]:


# Calcolatrice Python con decisioni

operazione = input("Inserisci l'operazione (+, -, *, /): ")

numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

if operazione == "+":
    risultato = numero1 + numero2
elif operazione == "-":
    risultato = numero1 - numero2
elif operazione == "*":
    risultato = numero1 * numero2
elif operazione == "/":
    risultato = numero1 / numero2
else:
    risultato = "Operazione non valida"
    
print("Il risultato è:", risultato)


# # Contare fino a N #

# In[14]:


n = int(input("Inserisci un numero intero positivo:"))

for numero in range(1,n+1):
    print(numero)


# # Calcolare la Somma #

# In[17]:


n = int(input("Inserisci un numero intero positivo: "))
somma = 0

for numero in range(1, n+1):
    #somma = somma + numero
    somma += numero
print("La somma dei primi", n, "numeri interi è:", somma)


# # Calcolare il Quadrato dei Primi Numeri #

# In[24]:


n = int(input("Inserisci un numero intero positivo: "))

print("Quadrati dei primi", n, "numeri:")

for numero in range (1, n+1):
    quadrato = numero ** 2
    print("Il quadrato di", numero, "è", quadrato)


# # Verificare la Parità #

# In[29]:


numero = int(input("Inserisci un numero: "))

#Se input è DIVISIBILE(%) per 2 e ha resto 0 (== 0)
if numero % 2 == 0:
    print(numero, "é un numero pari.")
else:
    print(numero, "è un numero dispari.")


# # Calcolare il Fattoriale #

# In[55]:


n = int(input("Inserire un numero intero positivo: "))
fattoriale = 1

for numero in range(1, n+1):
    #fattoriale = fattoriale * numero
    fattoriale *= numero
print("Il fattoriale di", n, "è:", fattoriale)


# # Calcolare la media di una Lista di Numeri #

# In[61]:


numeri = [] #Lista vuota di nome numeri

n = int(input("Quanti numeri vuoi inserire= ")) #Chiede quanti numeri voglio inserire dentro la lista vuota

#chiede un numero per quanto hai detto alla prima domanda
for i in range(n):
    numero = float(input("Inserisci un numero: "))
    numeri.append(numero) #mette il numero inserito dopo quello precedente
    
media = sum(numeri) / len(numeri) #Somma numeri dentro la lista e divide per lunghezza di quanti elementi ci sono

print("La media dei numeri inseriti è:", media, numeri)


# # Gioco dell'Indovinello #

# In[10]:


import random #importa la libreria del random

numero_da_indovinare =random.randint(1, 100) #spara un numero da 1 a 100
tentativi = 0

#chiede un numero
while True:
    tentativo = int(input("Indovina il numero (1-100): "))
    tentativi += 1
    
    if tentativo == numero_da_indovinare:
        print("Bravo! Hai indovinato il numero", numero_da_indovinare, "in", tentativi, "tentativi")
        break
    elif tentativo < numero_da_indovinare:
        print("Il numero è più grande")
    else:
        print("Il numero è più piccolo")


# # MORRA CINESE #

# In[69]:


import random

mosse = ["carta", "forbice", "sasso"]

computer_mossa = random.choice(mosse)

print("Benvenuti al gioco del Morra Cinese!")
scelta_giocatore = input("Scegli la tua mossa (Carta, forbici, sasso): ")

if scelta_giocatore not in mosse:
    print("Mossa non permessa")
else:
    print("Il computer ha scelto:", computer_mossa)
    if scelta_giocatore == computer_mossa:
        print("Pareggio!")
    elif (scelta_giocatore == "carta" and computer_mossa == "sasso") or \
         (scelta_giocatore == "forbici" and computer_mossa == "carta") or \
         (scelta_giocatore == "sasso" and computer_mossa == "forbici"):
        print("Hai Vinto!")
    else:
        print("Hai Perso!")


# # Calcolo del fattoriale #

# In[74]:


n = int(input("Inserisci un numero intero: "))

fattoriale = 1

if n<0:
    print("Numero Negativo")
elif n ==0:
    print("Il numero di zero è un 1 per definizione")
else:
    for numero in range(1, n+1):
        fattoriale*=numero
print(f"Il fattoriale di {n} è {fattoriale}")


# # somma numeri n #

# In[13]:


# Chiedere all'utente d'inserire un numero imtero positivo N

N = int(input("Inserisci un numero intero positivo N: "))

# Inizializzare la somma a zero
somma = 0

# Calcolare la somma dei primi N numeri pari
for numero in range(2, 2 * N + 1, 2):
    somma += numero
    
# Stampare la somma
print(f"la somma dei primi {N} numeri pari è {somma}")


# # CONTA VOCALI IN UNA FRASE #

# In[14]:


# Chiedere all'utente d'inserire una frase o una parola

frase  = input("Inserisci una frase o una parola: ").lower() #Converti tutto in minuscolo per semplificare il contaggio

# Inizializzare il contatore delle vocali
conteggio_vocali = 0

# Definisci le vocali da cercare
vocali = "aeiou"

# scansione ogni carattere nella frase
for carattere in frase:
    # Verifica se il carattere è una vocale
    if carattere in vocali:
        conteggio_vocali += 1
    
# Stampare la somma
print(f"nella frase ci sono {conteggio_vocali} vocali")


# In[20]:


# Chiedere all'utente di inserire un nuerp intero positivo N
N = int(input("Inserisci un numero intero positivo N: "))
lista = []


# Calcolare la somma dei primi n numeri pari
for numero in range(2, 2 * N + 1,2):
    lista.append(numero)
    
print(lista)


# # IDNOVINA IL NUMERO DI DADO CASUALE (1 a 6) #

# In[60]:


import random

# Genera un numero casuale da 1 a 6(simulando un lanco di un dado)
numero_dado = random.randint(1, 6)

# Chiedi all'utente d'indovinare il numero
indovina = int(input("Indovina il numero del dado (da 1 a 6): "))

# Verifica se l'utente ha indovinato correttamente
if indovina <1 or indovina <0:
    print("numero non ammesso")
elif indovina == numero_dado:
    print(f"Complimenti il numero del dardo era {numero_dado}. Hai indovinato!")
else:
    print(f"Mi dispiae, il numero del dado era {numero_dado}. Meglio fortuna la prossima volta!")


# # SIMULAZIONE POPOLAZIONE #

# In[66]:


# Inizializza la popolazione e gli anni
popolazione = int(input("inserisci popolazione iniziale: "))
anni = int(input("Inserisci il numero di anni da simulare: "))
# Tasso di natalità e tasso di mortalità (% annuale)
tasso_natalità = float(input("Inserisci tasso natalità: "))
tasso_mortalità = float(input("Inserisci tasso mortalità: "))


# Simulazione della crescita della popolazione
for anno in range(anni):
    nascite = (popolazione * tasso_natalità) / 100
    morti = (popolazione * tasso_mortalità) / 100
    popolazione += (nascite - morti)
    
    print(f"Anno {anni}, Popolazione {int(popolazione)}")
    
print("Simulazione completata")


# # dire giorno ed ora con datetime #

# In[67]:


import datetime

today = datetime.datetime.today()
print(f"oggi è il giorno:{today: %d %m %y},  ore:{today: %H %M %S}")


# In[4]:


print("Benvenuto nel convertitore di misura!")
scelta = input("Cosa desideri convertire? (metri/piedi/chilograbbi/libbre): ").lower()

if scelta == "metri":
    valore = float(input("Inserisci il valore in metri: "))
    risultato = valore * 3.28034
    print(f"{valore} metri corrispondono = {risultato} piedi.")
    
elif scelta == "piedi":
    valore = float(input("Inserisci il valore in piedi: "))
    risultato = valore * 0.3048
    print(f"{valore} metri corrispondono = {risultato} metri.")
    
elif scelta == "chilogrammi":
    valore = float(input("Inserisci il valore in chilogrammi: "))
    risultato = valore * 2.2046
    print(f"{valore} metri corrispondono = {risultato} libbre.")
    
elif scelta == "libbre":
    valore = float(input("Inserisci il valore in libbre: "))
    risultato = valore * 3.28034
    print(f"{valore} metri corrispondono = {risultato} chilogrammi.")


# # FIBONACCI #

# In[69]:


# Chiedere all'utente d'inserire un numero n
n = int(input("Inserisci un numeor n per calcolare l'n-esimo numero di Fibonacci: "))
#inizializzare le variabili per i primi due numeri di fibonacci
a=0
b=1
c=1

# Calcolare l'n-esimo numero di fibonacci
if n <= 0:
    print("il numero deve essere maggiore di 0")
elif n == 1:
    risultato = a
else:
    for iterazione in range(n-3):
        a = b
        b = c
        c = a + b
    risultato = c
# Stampare l'n-esio numero di fibonacci
print("l'n-esimo numero di fibonacci è:", risultato)


# # FUNZIONI CUSTOM #

# In[79]:


def fibonacci(n):
    fib_series = [0, 1]
    
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
        
    return fib_series


# In[80]:


fibonacci(9)


# In[3]:


import math

def calcola_area_cerchio(raggio):
    return math.pi * (raggio ** 2)

def calcola_area_rettangolo(base, altezza):
    return base * altezza

def calcola_area_triangolo(base, altezza):
    return (base * altezza) / 2

print("Benvenuro nella calcolatrice di aree")

scelta = input("Vuoi calcolare l'area di un cerchio (c), rettangolo (r), triangolo (t): ").lower()

if scelta == 'c':
    raggio = float(input("Inserisci il raggio del cerchio: "))
    area = calcola_area_cerchio(raggio)
    print(f"L'area del cerchio è {area: .2f}")
elif scelta == 'r':
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    area = calcola_area_rettangolo(base, altezza)
    print(f"L'area del rettangolo è {area:.2f}")
elif scelta == 't':
    base = float(input("inserisci la base del triangolo: "))
    altezza = float(input("Inserisci l'altezza del triangolo: "))
    area = calcola_area_triangolo(base, altezza)
    print(f"l'area del triangolo è {area:-2f}")
else:
    print("Scelta non valida, riprova")


# In[ ]:




