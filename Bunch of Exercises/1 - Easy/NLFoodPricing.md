## Price Basket in Newfoundland

The Canadian province of Newfoundland is conducting an analysis of the prices of its inhabitants' main food items to monitor the increase in the cost of living. For this reason, it has gathered in a .csv file the price of different foods over time in various locations and in stores of different supermarket chains. The data is collected in the *NLFoodPricing.csv* file which reports the following information:

```
Date,Place,Grocery store,Food item,Essential/optional,$/kilo
```

where **Date** is the date in the format dd/mm/yyyy, **Place** is the location, **Grocery store** is the store chain, **Food item** is the name of the food, **Essential/optional** is a letter indicating whether the food is considered essential (**E**) or optional (**O**), **$/kilo** is the price per kilo of the food on the date and in the indicated location. The fields are separated by commas, and each row refers to a different survey (different product and/or date and/or store).

A second file, called **shops.txt**, lists the chains under observation, listed one per line. 

Assume that the format of the two files is correct, and that the data is consistent (for example, it is not necessary to verify that the rows of the .csv file are actually different from each other).

Write a Python program that supports the province's analysis. The program must:

- list the food items considered essential in alphabetical order
- indicate for each chain reported in the file **shops.txt** (in alphabetical order), the minimum price detected for each of the food items considered essential (reported in alphabetical order)
- finally, it must allow the user to indicate one of the essential food items and respond with the minimum price detected and the store chain where this price was found; the input ends if the user enters a control character (for example 'q'), while if the product is not among those essential, an error message must be returned and the input can continue


## Esempio

***NLFoodPricing.csv (sample)***

```
Date,Place,Grocery store,Food item,Essential/optional,$/kilo
08/10/2020,Clarenville,Sobeys,Apple,E,5.49
08/10/2020,Clarenville,Coop,Apple,E,6.59
08/10/2020,Clarenville,Coop,Black tea,E,18.70
08/10/2020,Clarenville,Sobeys,Black tea,E,19.07
08/10/2020,Clarenville,Sobeys,Bread whole wheat,O,4.54
08/10/2020,Clarenville,Coop,Carrot,O,3.85
08/10/2020,Clarenville,Sobeys,Carrot,O,2.64
```

***File shops.txt***

```
Colemans
Walmart
Sobeys
```

**Program output (printed on the monitor, Apple, Ground beef, Bread and q are entered by the user)**

```
Products: 
- Apple
- Black tea
- Ground beef
- Peanut butter
- Tomato
- Tuna canned

Colemans: 
- Apple: 3.30 $/chilo
- Black tea: 11.40 $/chilo
- Ground beef: 10.99 $/chilo
- Peanut butter: 10.58 $/chilo
- Tomato: 4.38 $/chilo
- Tuna canned: 10.00 $/chilo

Sobeys: 
- Apple: 3.30 $/chilo
- Black tea: 13.17 $/chilo
- Ground beef: 10.10 $/chilo
- Peanut butter: 10.98 $/chilo
- Tomato: 12.10 $/chilo
- Tuna canned: 10.53 $/chilo

Walmart: 
- Apple: 2.92 $/chilo
- Black tea: 13.61 $/chilo
- Ground beef: 11.00 $/chilo
- Peanut butter: 3.27 $/chilo
- Tomato: 2.14 $/chilo
- Tuna canned: 10.70 $/chilo

Which food do you want to search for? (q to quit)
*Apple*
Minimum price: 2.92 $/chilo at Walmart

Which food do you want to search for? (q to quit) 
*Ground beef*
Minimum price: 10.10 $/kilo at Sobeys

Which food do you want to search for? (q to quit) 
*Bread*
Product not available

Which food do you want to search for? (q to quit) 
*q*
Goodbye

```
