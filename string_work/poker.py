hand = [[i[0:-1], i[-1]] for i in input().split()]
# print(hand)

suit = hand[0][1]
same_suit = True
for i in hand:
    if i[1] != suit:
        same_suit = False
royal_chain = ["A", "K", "Q", "J", "10"]
street_hands = [["9", "K", "Q", "J", "10"],
                ["9", "8", "Q", "J", "10"],
                ["9", "8", "7", "J", "10"],
                ["9", "8", "7", "6", "10"],
                ["9", "8", "7", "6", "5"],
                ["4", "8", "7", "6", "5"],
                ["4", "3", "7", "6", "5"],
                ["4", "3", "2", "6", "5"],
                ["4", "3", "2", "A", "5"],
                ["A", "K", "Q", "J", "10"]]

hand_values = [hand[j][0] for j in range(5)]
dict_hand_values = {}

if same_suit and all(i in [hand[j][0] for j in range(5)] for i in royal_chain):
    print("Royal Flush")
elif (all(i in hand_values for i in street_hands[0]) or
      all(i in hand_values for i in street_hands[1]) or
      all(i in hand_values for i in street_hands[2]) or
      all(i in hand_values for i in street_hands[3]) or
      all(i in hand_values for i in street_hands[4]) or
      all(i in hand_values for i in street_hands[5]) or
      all(i in hand_values for i in street_hands[6]) or
      all(i in hand_values for i in street_hands[7]) or
      all(i in hand_values for i in street_hands[8]) or
      all(i in hand_values for i in street_hands[9])):

    if same_suit:
        print("Straight Flush")
    else:
        print("Straight")
elif same_suit:
    print("Flush")
else:
    for i in hand_values:
        if i in dict_hand_values:
            dict_hand_values[i] += 1
        else:
            dict_hand_values[i] = 1

    if 4 in dict_hand_values.values():
        print("Four of a Kind")
    elif all(m in dict_hand_values.values() for m in [3, 2]):
        print("Full House")
    elif 3 in dict_hand_values.values():
        print("Three of a Kind")
    elif 2 in dict_hand_values.values():
        if len(dict_hand_values.values()) == 3:
            print("Two Pairs")
        else:
            print("Pair")
    else:
        print("High Card")
