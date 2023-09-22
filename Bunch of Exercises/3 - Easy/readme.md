## Degree Requirements Check

A university monitors its students academic careers using an application that tracks data related to taken exams. Specifically, the data is reported in a file named *"exams.log"*, which saves the data related to the exams taken in the following format:

	matricola,data_esame,codice_esame,voto

Where:

- student_id: is unique per student and is in the format S+Number on 6 digits
- exam_date: is a string in the format DD/MM/YYYY
- exam_code: is an alphanumeric string of 3 characters that uniquely identifies an exam (for example INF, for computer science or AM1 for Mathematical Analysis 1).
- grade: can have any value between 18 and 30L (18, 19, ... 30, 30L), or it can be the letter "R" (indicating a failing student) or the letter "A" (indicating an absent student).

Since an exam can be taken more than once, it is possible that a student may appear in multiple rows with the same exam code; in this case, the latest grade should be considered for a student's grade average. The data appears in the file in no particular order.

In a second file named "cfu.data" the data related to each exam is saved in the following format:

	codice_esame,CFU,obbligatorio


Where:

- exam_code: has the same format described above.
- CFU: integer number between 1 and 10
- mandatory: is 0 (False) or 1 (True)

The program must process the file containing all the exams taken (exams.log) and print on screen the list of student ids of students who can be admitted to the final graduation exam. The admission conditions are to have accumulated at least 30 total CFU of which at least 10 mandatory CFU.
A student earns the CFU only if the exam is passed.

The list printed on screen must contain the following accessory information:

- CFU obtained, with indications of the mandatory ones
- Weighted average for the CFU (sum of the products between grade and CFU of each exam, divided by the number of total CFU). For average purposes 30L counts as 33, while A and R are to be excluded.

***Execution Example***

Given the log file


	s000001,01/01/2022,in1,A
	s000001,01/01/2022,am1,30
	s000001,20/01/2022,in1,30
	s000001,30/01/2022,scZ,20
	s000002,01/01/2022,am1,30
	s000002,20/01/2022,in2,30
	s000002,30/01/2022,scA,30

and the file cfu.dati

	in1,10,1
	in2,10,1
	am1,10,1
	am2,10,1
	scA,6,0
	scZ,15,0

Output result

	STUDENTE s000001
	Student with total 35 CFU; 20 CFU mandatory, 25.71 of average 
	STUDENTE s000002
	Student with total 26 CFU; 20 CFU mandatory; 30.00 of average ; no graduation
