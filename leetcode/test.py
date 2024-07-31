event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]
a, b = map(int,event1[0].split(':'))
c, d = map(int,event1[1].split(':'))
m, n = map(int,event2[0].split(':'))
p, q = map(int,event2[1].split(':'))
print(a, b, c, d)
print(m, n, p, q)