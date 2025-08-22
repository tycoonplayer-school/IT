import math
prices = {
  12: 8,
  17: 12,
  64: 15,
  math.inf : 10
}
def get_ticket_price(age):
    for req, price in sorted(prices.items()):
        if age <= req:
            return price
def input_number(req):
    res = None
    while not res:
        res = input(req)
        if not res.isdigit():
            print("That's not a valid option, please try again.")
            res = None
    return int(res)
def request_ticket():
    name = input("Enter your name: ")
    age = None
    while not age:
        age = input_number("Enter your age: ")
        if 0 > age or age > 120:
            print("Invalid age entered.")
            age = None
    price = get_ticket_price(age)
    print(f"Hello {name}! Your ticket price is ${price}.")
    return price
def get_payment(req):
    entered = None
    while not entered:
        entered = input_number("Enter your payment amount: $")
        if entered < req:
            print("That's not enough money!")
            entered = None
    return entered - req
def get_ticket_amt():
    ticket_amt = None
    while not ticket_amt:
        ticket_amt = input_number("Enter the amount of tickets you want: ")
        if ticket_amt < 1:
            print("That's too low!")
            ticket_amt = None
    return ticket_amt
        
ticket_amt = get_ticket_amt()
ticket_prices = []
for x in range(1, ticket_amt + 1):
    print(f"Ticket {x}")
    ticket_prices.append(request_ticket())
end_price = sum(ticket_prices)
change = get_payment(end_price)
if change > 0:
    print(f"Here is your change: ${change}")


    
  
    
