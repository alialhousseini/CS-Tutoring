# Exam Text "Lotto Drawings"

A devoted player of the Lotto game intends to devise a "winning" strategy based on the statistics of the numbers drawn in the past. All his friends and acquaintances with a minimum of competence in mathematics, statistics, or common sense have tried to convince him that gambling games are always losing, but he decides to continue his crusade.

The file "storico01-oggi.txt" contains all the Lotto draws, on all the 'wheels' (10 wheels corresponding to the city where the draw takes place, plus the eleventh 'national' wheel). Each draw contains 5 unique integers, between 1 and 90 (inclusive).

The file contains one line for each draw, in the format illustrated by the following snippet:

    2022/09/03	TO	17	71	21	9	1
    2022/09/03	VE	38	69	75	87	29
    2022/09/06	BA	80	82	9	26	3
    2022/09/06	CA	79	49	72	35	1

There are 7 fields separated by spaces, where the first is the draw date (in the year/month/day format), the second is the wheel (the acronym of the city, or the RN acronym for the National Wheel), and the next 5 fields are the drawn numbers.

The program should verify the 'overlaps' between the different wheels. Specifically, the user must enter from the keyboard the codes of two Wheels, and the program, analyzing all the draws present in the file, must determine:

- which numbers were drawn, on the same date, in the two specified wheels. In this case print the number and the date.
- calculate the frequency of each of these numbers calculated in the previous point, and print them in descending order of frequency.

## Example of program execution
```
Available wheels BA, CA, FI, GE, MI, NA, PA, RM, RN, TO, VE
Enter the first wheel: TO
Enter the second wheel: MI

Common number  6 on date 2001/01/27
Common number 36 on date 2001/02/10
Common number 22 on date 2001/02/14
Common number 81 on date 2001/02/17
. . .
. . .
Common number  7 on date 2022/08/27
Common number 18 on date 2022/08/30
Common number 17 on date 2022/09/03
Common number 38 on date 2022/09/06
    
Number    Frequency
--------  ---------
      90         19
      82         16
      38         16
      18         15
       1         15
      53         15
      30         15
. . .
. . .
      28          5
       4          3
      74          3
      63          1
```
