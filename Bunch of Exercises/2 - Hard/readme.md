## Weather Station Management

The file contains a record for each line and the fields are separated by ; and are considered as float values.

The first line of the file contains the names of the meteorological variables measured by the weather station. The number and names of the variables are <u>not known in advance</u>: the only known column is the first one containing the date and time of the measurement. The maximum length of each variable is 25 characters.

The center wants a Python program that takes the name of the file to be processed as input and returns for each measured variable the maximum, minimum and average.

Example of the file of input:
```
Torino.csv
```

```
Data;Temp;Rugiada;Pressione;Umidita'
01-01-17 00:00;4.6;2.1;1028;84
01-01-17 00:14;4.6;2.1;1027.7;84
01-01-17 00:29;4.6;2.1;1027.7;84
01-01-17 00:44;4.5;2.1;1027.7;84
01-01-17 01:00;4.5;2.2;1027.7;85
...
03-01-17 22:29;1.9;1.1;1008;94
03-01-17 22:44;1.9;1.1;1007.3;94
03-01-17 22:59;1.9;1.1;1007;94
03-01-17 23:14;1.9;1.1;1007;94
03-01-17 23:29;1.9;1.1;1006.7;94
03-01-17 23:44;2.1;1.2;1006.7;94
03-01-17 23:59;2.1;1.2;1006.3;94

```

```
Pinerolo.csv
```
```
Data;Pressione;DirVento;VelVento;Umidita';Pioggia;Radiazione
01-06-17 00:29;1013.8;306;1.6;90;0;0
01-06-17 00:59;1013.8;0;0;90;0;0
01-06-17 01:29;1013.8;0;0;90;0;0
01-06-17 01:59;1013.4;0;0;90;0;0
01-06-17 02:29;1013.4;0;0;90;0;0
01-06-17 02:59;1013.4;0;0;91;0;0
01-06-17 03:29;1013.4;42;1.6;90;0;0
01-06-17 03:59;1013.1;349;1.6;90;0;0
01-06-17 04:14;1013.1;337;1.6;90;0;0
...
04-06-17 21:44;1013.1;106;1.6;92;0;0
04-06-17 21:59;1013.1;0;0;92;0;0
04-06-17 22:14;1013.4;0;0;92;0;0
04-06-17 22:29;1013.4;253;3.2;92;0;0
04-06-17 22:44;1013.8;252;1.6;92;0;0
04-06-17 22:59;1013.8;261;1.6;92;0;0
04-06-17 23:14;1013.8;269;3.2;92;0;0
04-06-17 23:29;1013.8;260;1.6;92;0;0
04-06-17 23:44;1013.8;245;1.6;91;0;0
04-06-17 23:59;1014.1;245;0;91;0;0

```


Example of output:
```
Report meteorologico per la stazione di Torino
             Temp     Rugiada  Pressione   Umidita' 
01-01-17
   media     4.62     2.11     1026.59     83.82
 massimo     5.60     2.80     1028.00     88.00
  minimo     3.60     1.70     1024.60     79.00

02-01-17
   media     3.49     1.92     1019.11     89.52
 massimo     4.70     2.40     1024.60     93.00
  minimo     2.60     1.40     1012.80     82.00

03-01-17
   media     2.28     1.34     1010.31     93.43
 massimo     2.90     1.90     1012.80     94.00
  minimo     1.80     0.80     1006.30     93.00

```

```
Report meteorologico per la stazione di Pinerolo
             Pressione   DirVento   VelVento Umidita'  Pioggia  Radiazione 
01-06-17
   media     1012.83     171.30     3.08     73.50     0.00     311.38
 massimo     1013.80     349.00     8.00     91.00     0.00     1294.00
  minimo     1011.40     0.00       0.00     56.00     0.00     0.00

02-06-17
   media     1010.86     170.82     1.82     78.13     0.13     131.81
 massimo     1012.80     355.00     4.80     87.00     2.80     561.00
  minimo     1009.40     0.00       0.00     68.00     0.00     0.00

03-06-17
   media     1010.54     182.77     1.65     79.32     0.32     178.25
 massimo     1011.40     353.00     6.40     93.00     7.60     1034.00
  minimo     1009.00     0.00       0.00     57.00     0.00     0.00

04-06-17
   media     1011.95     161.22     2.64     85.99     0.57     145.10
 massimo     1014.10     347.00     9.70     93.00     13.50    1320.00
  minimo     1010.70     0.00       0.00     69.00     0.00     0.00
```