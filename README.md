# gpa_calculator
script to calculate total GPA out of 4 based on input gpa.csv

to use, create a total.csv file containing only one integer showing the total number of units, and a gpa.csv containing rows like this:

```"name of course", number of its units(eg. 3) , its mark, either A or B or C or D or G```

examples are shown in gpa_sample.csv and total_sample.csv

### to know which mark you got (from 20 scale):

- 16-20 -> A
- 14-15.99 -> B
- 12-13.99 -> C
- 10-11.99 -> D
- <10 -> F
