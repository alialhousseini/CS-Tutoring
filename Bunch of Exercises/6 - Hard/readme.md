# Beach Resort
The manager of a beach resort wants to implement a program to manage the seating (deck chairs and umbrellas) at his resort.

The beach area granted to the resort is organized in rows. The **first row** is the one **closest** to the sea; the last row is the farthest. Each row is equipped with a certain number of umbrellas and deck chairs. The **rental cost** for umbrellas and deck chairs <u>depends</u> on the row they are in: it decreases based on the distance from the sea (that is, the first row is the most expensive).

The resort's organization is stored in the file **"stabilimento.txt"**, in which **each line** corresponds to a row. The first line of the file corresponds to the first row of umbrellas (i.e., the one **closest** to the sea), and so on up to the last.

Each row indicates:

- the number of available umbrellas in that row,
- the cost to rent an umbrella in that row,
- the number of available deck chairs in that row,
- the cost to rent a deck chair in that row.
- Fields are separated by commas. The file is to be considered always correct.

Example file 'stabilimento.txt'


```
4, 30, 6, 15
4, 22, 8, 12
5, 16, 8, 8
6, 12, 12, 8
```

The program reads the information about customers entries and exits from the file "ingressi-uscite.txt". When a customer <u>enters</u> the resort, the file reports a line with the following information:

`unique customer name, number of umbrellas requested, number of deck chairs requested, budget willing to spend.`

Fields are separated by commas. The program should **indicate** which row the customer can go to, checking the availability of umbrellas and deck chairs and trying to **maximize** the booking cost (i.e., choosing the most expensive available row that fits within the customer's budget). The program **prints** the row assigned to the customer (**updating** its availability), or **reports the inability to satisfy the request**.

When a customer <u>exits</u> the resort, the file reports a line with **only** the customer's name. It is <u>guaranteed</u> that every customer who leaves has previously entered. The program should **report** the customer's exit and **update the availability** of the row where they were located.

***Example file 'ingressi-uscite.txt'***


```
Jerry, 2, 3, 100
Alba, 2, 4, 90
Teo, 3, 6, 110
Mauro, 1, 2, 30
Franco, 3, 4, 75
Alba
Eva, 2, 3, 130
Pier Maria, 2, 5, 100
Nathalie, 3, 4, 160
Mauro
Jerry
Pier Maria
Teo
Eva
```

At the end of the file reading, the program should print the daily revenue.

***Execution example***
```
Customer Jerry is in row 2
Customer Alba is in row 3
Customer Teo is in row 4
Customer Mauro is in row 4
Customer Franco didn't find a spot
Customer Alba has left
Customer Eva is in row 1
Customer Pier Maria is in row 3
Customer Nathalie didn't find a spot
Customer Mauro has left
Customer Jerry has left
Customer Pier Maria has left
Customer Teo has left
Customer Eva has left
Today's earnings are 633
```
