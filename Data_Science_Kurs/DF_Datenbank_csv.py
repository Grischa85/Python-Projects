import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# 2: Das geladene Dataframe wird jedesmal neu geladen und zeigt den aktullen stand an
df = pd.read_csv('Dataframe.csv')
print(df)
name = input('Name eingeben: ')
Geschlecht = input('Geschlecht eingeben: ')
alter = input('Alter eingeben: ')

# 1: Erst muss ein Dataframe erzeugt werden und dann kann es immer wieder neue geladen werden
df = pd.DataFrame(df, columns=['Name', 'Geschlecht', 'Alter'])
df = df.append({'Name': name, 'Geschlecht': Geschlecht, 'Alter': alter}, ignore_index=True)
df.to_csv('Dataframe.csv')
print(df)
