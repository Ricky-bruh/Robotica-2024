import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Carica il file CSV con il nuovo layout
df = pd.read_csv('C:/Users/Ricky/OneDrive/Desktop/CodiciPerScuola/Robotica/BOCKEMON/pokemon.csv', quotechar='"')

# Rimuovi le righe duplicate basate sulla colonna 'Name'
df = df.drop_duplicates(subset='Name')

# Crea il dizionario 'pokedex'
pokedex = df.set_index('Name').to_dict(orient='index')

# Funzione di ricerca
def search_pokemon():
    pokemon_name = entry.get()
    if pokemon_name in pokedex:
        details = pokedex[pokemon_name]
        display_pokemon_details(details)
    else:
        messagebox.showinfo('Pokemon non trovato', f'{pokemon_name} non trovato nel pokedex.')

# Funzione per visualizzare i dettagli del Pokemon
def display_pokemon_details(details):
    details_text.config(state=tk.NORMAL)
    details_text.delete(1.0, tk.END)
    for key, value in details.items():
        details_text.insert(tk.END, f'{key}: {value}\n')
    details_text.config(state=tk.DISABLED)

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title('BOCKEMON Search')

# Etichetta e campo di input
label = ttk.Label(root, text='Inserisci il nome del Pokemon:')
label.pack(pady=10)
entry = ttk.Entry(root)
entry.pack(pady=10)

# Pulsante di ricerca
search_button = ttk.Button(root, text='Cerca Pokemon', command=search_pokemon)
search_button.pack(pady=20)

# Casella di testo scorrevole per i dettagli
details_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=15)
details_text.pack(pady=10)
details_text.config(state=tk.DISABLED)

# Esecuzione dell'interfaccia grafica
root.mainloop()
