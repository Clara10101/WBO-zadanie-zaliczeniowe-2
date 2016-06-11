# WBO-zadanie-zaliczeniowe-2

Schemat zastosowanej procedury, która dla danego zbioru proteomów pozwala na skonstruowanie
ich drzewa filogenetycznego.

1. Wybranie zbioru organizmów do analizy.

2. Pobranie genomów tych organizmów i wybranie z nich sekwencji kodujacych. Narzedzie:
skrypt downloadGenomes.py z pierwszego projektu zaliczeniowego.

3. Wyznaczenie podobienstwa kazdej pary sekwencji kodujacych. Narzedzie: BLAST+ NCBI.
Zbudowanie lokalnej bazy danych z sekwencji. Wywołania BLAST podane poniżej.

makeblastdb -in all_sequences.fasta -parse_seqids -dbtype prot (lokalna baza danych)
bin\blastp -db all_sequences.fasta -query all_sequences.fasta -out result_from_blast.out

4. Wyznaczenie rodzin sekwencji homologicznych przez poklastrowanie macierzy podobienstwa
uzyskanej programem BLAST. Narzedzie: MCL.
Wywołania podane poniżej.

perl local/bin/mcxdeblast result_from_blast.out --line-mode=abc >> do_mcl_file (przygotowanie danych do MCL)
mcl do_mcl_file --abc -I 1.2 -o podzial_na_rodziny_mcl.abc

5. Odfiltrowanie rodzin zawierajacych zbyt mało gatunków oraz wybranie losowych
przedstawicieli sekwencji w przypadku gdy w rodzinie wystepowała wiecej niz jedna
sekwencja dla danego gatunku.

Narzędzie: skrypt skryptOdfiltrowanie.py.
Do dalszej analizy wybrane zostala klastry zawierajace sekwencje z co najmniej 3 gatunkow.
Sekwencje dla każdej rodziny zapisane w folderze rodziny_homologow, pliki o nazwie wynik_i gdzie i odpowiada numerowi rodziny.

6. Uliniowienie rodzin genów.
Narzedzie: program MUSCLE i skrypt wywołujacy obliczenia równolegle
runMUSCLE.py. (biblioteka multiprocessing).

W plikach wynikowych z uliniowieniem, aby możliwa była dalsza analiza, nazwy sekwencji białkowych zostały zamienione na nazwy gatunków.
Skrypt msaHeader.py.

7. Rekonstrukcja drzew genów na podstawie uliniowien. Wyznaczenie dla kazdego uliniowienia
konsensusu drzew otrzymanych metoda bootstrapingu oraz eliminacja drzew zawierajacych
krawedzie o niewielkim wsparciu. Narzedzie: skrypt tree.py oraz runTree.py
do zrównoleglenia obliczen.

Dla każdego uliniowienia wielosekwencyjnego wyznaczono konsensus większościowy pięćdziesięciu drzew otrzymanych metodą bootstrappingu,
z pominięciem drzew zawierających krawędzie o wsparciu mniejszym niż 50. Drzewa tworzone były z wykorzystaniem metody neighbor joining.

8. Przygotowanie wyników do programu Fasturec - Retree PHYLIP i prosty plik wsadowy składający się z odpowiedniej liczby następującego ciągu
poleceń "B\n0\nR\nW\nA\nU\n+\n". Wywołanie retree < bat_file.bat > screenout &.
Wynikowe drzewo - plik drzewo_wynikowe.txt

8. Uzgodnienie drzew genów. Narzedzie: Fasturec.
