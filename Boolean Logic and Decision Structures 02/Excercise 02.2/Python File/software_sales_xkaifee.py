"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 02.2 -  Software Sales
Date: 09/10/2023

Description:
    This program will calculate the total cost of a software purchase.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    quantity = int(input("How many packages will be purchased: "))

    package_price = 880
    discount = 0
     
    if (quantity < 0):
        print("  Invalid Input!")
    
    else:
    
    
    
     if (quantity >= 4 and quantity <= 39):
        discount = 0.1
     elif (quantity >= 40 and quantity <= 199): #discounts
        discount = 0.15
     elif (quantity >= 200 and quantity <= 999): #discounts
            discount = 0.3
     elif (quantity >= 1000):
          discount = 0.42
      
      
     total = quantity * package_price * (1 - discount) #total price
     formated_total = "{:,.2f}".format(total)  #total price
     discount_formated = int(discount * 100) #discount percentage
    
     if (discount > 0):
        print(f"  {discount_formated}% discount applied.")
        print(f"  The total price to purchase {quantity} packages is ${formated_total}.") #total price
     else:
        print("  No discount applied.")
        print(f"  The total price to purchase {quantity} packages is ${formated_total}.")  #total price

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
