# pythonQuestionVendingMachine
Here is my logic,
first, I need to define the price of the product in integer
then, I need to define the available bank notes in malaysia for comparison with the notes inserted to purchase the product. It will contain 100,50,20,10,5,1
then, the logic will start work like select product and select quantity
then the logic count the price. Eg 20
then key in amount that the user want to pay. Eg insert 100
then the logic will deduct 100 with the final amount
then take the final amount (which is the amount to return back to the user) compare with the available bank notes, if the final amount is larger than the available bank note. Eg 80 > 50
then 80 will deduct 50, and dispense 50 to the user
then continue to do until the smallest amount which is 1.
