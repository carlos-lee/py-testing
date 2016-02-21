def cheese_and_crackers(cheese_counts, boxes_of_crackers):
    print "you have %d cheese!" % cheese_counts
    print "you have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "Or we can use variables from our scripts:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "we can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two,varibles and math:"

cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
