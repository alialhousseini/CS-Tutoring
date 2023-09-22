## Management of Race Results

The task is to implement a Python program that automatically manages the results of a 10 km running race. The race-related information is recorded in the file ***risultati_gara.txt***.

Each line of the file contains the following participant information (separated by a semicolon):

```
<Name>;<Surname>;<Age>;<Category (M/F)>;<Time (min)>;<Athlete_ID>
```
Participants are listed in the order of arrival.

In a second file, ***database_atleti.txt***, the personal records (expressed as pace, in min/km) of each athlete are stored in this format:

```
<Athlete_ID>;<Personal Record>
```
The personal record is indicated with a floating-point number, where the integer digit indicates the minutes and the decimal digits indicate the seconds.

The following assumptions are made:

The number of athletes is not known in advance.
The ID of each athlete is unique.
The file format is correct.

The program must:

1. Load the information contained in the file ***risultati_gara.txt*** into an appropriate data structure

2. Calculate the pace of each athlete (min/km), according to the following formula:



  ```
  pace = time / km
  ```

If the division does not return an exact number of minutes, multiply the decimal digits by 0.6 to get the correct pace. For example:
```
    time = 32 minutes
    distance = 10 km
    
    temporary_pace = 32/10 = 3.2
    
    minutes: 3
    seconds: 0.2*0.6 = 0.12
    
    pace = minutes + seconds = 3.12 min/km
```

3. Print the list of athletes, separated by category (M or F), reporting name, surname, and pace (min/km, with two decimal places).

4. Print the list of athletes who have beaten their personal record (one athlete per line).

### Example

**File: risultati_gara.txt**
```
David;Coq;41;M;33;FR90M1
Jaxon;Reed;28;M;34;US74M2
Maximilian;Hofer;40;M;35;AT87M1
Lena;Bauer;31;F;35;DE90W2
Giuseppina;Sandberg;25;F;36;SE22W1
Maria;Gonzalez;28;F;44;SP00W2
Juan;Rodriguez;35;M;45;SP27M1
Nadia;Patel;37;F;48;GB59W2
```

**File: database_atleti.txt**
```
FR90M1;3.34
US74M2;3.57
AT87M1;4.15
DE90W2;3.25
SE22W1;3.40
SP00W2;4.20
SP27M1;4.28
GB59W2;4.20
```

**Output di stampa**
```
PARTICIPANTS RANKING

Category: M
David Coq, 3.18 min/km
Jaxon Reed, 3.24 min/km
Maximilian Hofer, 3.30 min/km
Juan Rodriguez, 4.30 min/km

Category: F
Lena Bauer, 3.30 min/km
Giuseppina Sandberg, 3.36 min/km
Maria Gonzalez, 4.24 min/km
Nadia Patel, 4.48 min/km

ATHLETES WHO BEAT THEIR PERSONAL RECORD

Jaxon Reed
Maximilian Hofer
Giuseppina Sandberg
```
