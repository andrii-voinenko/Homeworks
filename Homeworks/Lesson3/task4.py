vip = ["Artur", "Clara", "Sam", "Vital"]
vip_zone_space = 4

main = ["Sam", "Josh", "Vivien", "Helen"]
main_zone_space = 100

if len(vip) >= vip_zone_space:
    print("Sorry there is no free place in VIP box")
else:
    print("You can take a seat!")
if len(main) >= main_zone_space:
    print("Sorry there is no free place in main zone")
else:
    print("You can take a seat!")
