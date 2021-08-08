# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import welcome



def blind_auction():
    count = 0
    user_names = []
    user_ids = []
    bids = []
    another_bidder = True
    print(welcome.auction)
    while another_bidder:
        name = input('Please enter your name: ')
        name = name.strip()
        user_id = name+str(count)
        bid = input('Please enter the amount you want to bid: $ ')
        assertion=True
        while assertion:
            try:
                bid = float(bid.strip())
                assertion=False
            except:
                bid=input('Invalid amount. Please enter a valid amount : $ ')
        user_names.append(name)
        user_ids.append(user_id)
        bids.append(bid)
        print(f'Your user id is {user_id}')
        another_bidder = input('Does anyone else want to bid?(yes/no): ')
        another_bidder = another_bidder.lower()
        while another_bidder != 'yes' and another_bidder != 'no':
            another_bidder = input('Invalid Option. Please enter a valid option (yes/no): ')
            another_bidder = another_bidder.lower()

        if another_bidder == 'yes':
            another_bidder = True
        else:
            another_bidder = False
        count += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        if another_bidder:
            print(welcome.auction)
    max_bid=max(bids)
    new_list=[]
    for i,bid in enumerate(bids):
        if bid==max_bid:
            new_list.append(i)
    if len(new_list)==1:
        print(f'The winner of the auction is {user_names[new_list[0]]} with user id {user_ids[new_list[0]]} and an amount of $ {bids[new_list[0]]}')
        print(welcome.winner)
    else:
        return
    
    











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
