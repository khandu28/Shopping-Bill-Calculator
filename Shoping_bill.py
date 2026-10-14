# Function to calculate Electronic GST (18%)
def CalculateElectronicGST(A, B):
    amount = A + B
    gst = amount * 18 / 100
    return amount + gst


# Function to calculate Fashion GST (13%)
def CalculateFashionGST(C, D):
    amount = C + D
    gst = amount * 13 / 100
    return amount + gst


# Function to calculate Food GST (7%)
def CalculateFoodGST(E):
    gst = E * 7 / 100
    return E + gst


# Function to calculate Total Bill
def totalBill(A, B, C, D, E):
    electronic = CalculateElectronicGST(A, B)
    fashion = CalculateFashionGST(C, D)
    food = CalculateFoodGST(E)

    return electronic + fashion + food


# Function to calculate Discount and Final Payable Amount
def CalculateDiscountBill(A, B, C, D, E):
    total = totalBill(A, B, C, D, E)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Main function call with predefined values
A = 100
B = 100
C = 100
D = 100
E = 100

total = totalBill(A, B, C, D, E)
final_amount = CalculateDiscountBill(A, B, C, D, E)

print("Electronic Bill (including 18% GST):", CalculateElectronicGST(A, B))
print("Fashion Bill (including 13% GST):", CalculateFashionGST(C, D))
print("Food Bill (including 7% GST):", CalculateFoodGST(E))
print("Total Bill:", total)
print("Final Payable Amount after 20% Discount:", final_amount)