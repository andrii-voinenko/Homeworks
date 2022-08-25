casino_blacklist = ["Marta Wein", "John Dow"]
poker_blacklist = ["Jane Dow", "Ernest Siff", "John Dow"]
alcohol_blacklist = ["Marcus Cliff", "John Dow"]

for i in poker_blacklist:
    if i in alcohol_blacklist and casino_blacklist:
        print(i)
