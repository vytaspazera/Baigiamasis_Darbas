# Kelionės atvaizdavimas žemėlapyje

Programą paleidus per main.py atsiras langas su Lietuvos žemėlapiu ir Lietuvos miestais. Pasirinkus miestus iš sąrašo jie bus pridėti prie Jūsų kelionės maršruto. Kelionė pasibaigs pasirinkus pradinį miestą arba paspaudus "Užbaigti kelionę" Jūs busite gražinti į pradinį miestą ir bus išmetama kelionės užbaigimo žinutė su visu nukeliautų kilometrų skaičiumi. Programoje bandydami keliaujant į jau aplankytus miestus gausite pranešimus, kad jau tuos miestus aplankėte. Netyčia pasirinkus ne tuos miestus galite spausti pradėti kelionę iš naujo.

- miestai.py scrapina Lietuvos miestų sąrašą ir priskiria miestams koordinates ir visą gautą informaciją priskiria pickle failui miestai_ir_koordinates.pkl.
- map_function.py atlieka žemėlapių veiksmus, jame naudojame chromedriver.exe
