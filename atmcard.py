def sum_digits(n) :
      s = 0
      while n > 0 :
            t = n % 10
            s += t
            n = int(n / 10)
      return s
n = input("Enter the credit card number : ")
sumn = 0
for i in range(len(n) - 2, -1, -2) :
      t = int(n[i]) * 2
      if t >= 10 :
            t = sum_digits(t)
      sumn += t
for i in range(len(n) - 1, -1, -2) :
      sumn += int(n[i])
if sumn % 10 == 0 :
     print("\nVALID")
else :
     print("\nINVALID")