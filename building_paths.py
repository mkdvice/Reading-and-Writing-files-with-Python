from pathlib import Path # importing standard library pathlib

path = Path('primeira_pasta/segunda_pasta') # creating a relative path

for name in ['arquivo1.txt','arquivo2.txt','arquivo3.txt',]: # listing files
    path_file = path / name
    print(path_file)