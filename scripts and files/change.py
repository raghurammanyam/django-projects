def vend():
    """Simulate a vending machine, taking user input and returning remainder."""
    total = int(input("Enter the cost (in cents): "))
    inserted = 0
    while inserted < total:
        inserted += int(input("Deposit a coin or note (in cents): "))
    if inserted > total:
        return make_change(inserted - total)

def make_change(remainder):
    """Calculate the coins required to make change equal to amount."""
    coins = ["500", "100", "50", "10", "1"]
    amounts = [int(coin[:-1]) if coin.endswith("c") 
               else 100 * int(coin[1:]) 
               for coin in coins]
    counts = [0 for _ in coins]
    for index, amount in enumerate(amounts):
        counts[index] = remainder // amount
        remainder %= amount
    return ", ".join("{0} x {1}".format(count, coin) 
                     for count, coin in zip(counts, coins) 
                     if count)
