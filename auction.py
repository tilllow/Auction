# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import welcome
import time


def tie(array,user_ids):
    winner_list=[]
    winner_list_ids=[]
    maximum_bid=float('-inf')
    print('There is a tie between',end=' ')
    for i,val in enumerate(array[:-1]):
        print(f'{val} with user_id {user_ids[i]}, ',end='' )
    print(f'and {array[-1]} with user id {user_ids[-1]}')
    print(f'As a result we would have these {len(array)} bidders bid again')
    i=0
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    while i<len(array):
        print(welcome.auction)
        bid = input(f'Please enter the amount you want to bid {array[i]} with id {user_ids[i]}: $ ')
        assertion=True
        while assertion:
            try:
                bid = float(bid.strip())
                assertion=False
            except:
                bid=input('Invalid amount. Please enter a valid amount : $ ')
        if i<len(array)-1:
            print(f'You made a bid of $ {bid}\n Please pass it on to the next bidder')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if bid>maximum_bid:
            maximum_bid=bid
            winner_list=[array[i]]
            winner_list_ids=[user_ids[i]]
        elif bid==maximum_bid:
            winner_list.append(array[i])
            winner_list_ids.append(user_ids[i])
        i+=1
    if len(winner_list)==1:
        return [winner_list[0],winner_list_ids[0],maximum_bid]
    return tie(winner_list,winner_list_ids)
# print(tie(['Tilow','Debrah','Steve'],['Tilow0','Debrahko2','Daniel3']))




def blind_auction():
    max_bid=float('-inf')
    user_names = []
    user_ids = []
    count=0
    another_bidder = True
    os.system('cls' if os.name == 'nt' else 'clear')
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
        if bid>max_bid:
            max_bid=bid
            user_names=[name]
            user_ids=[user_id]
        elif bid==max_bid:
            user_names.append(name)
            user_ids.append(user_id)
        print(f'Please take note.Your user id is {user_id}')
        time.sleep(2)
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
            
    if len(user_names)==1:
        print(f'The winner of the auction is {user_names[0]} with user id {user_ids[0]} and an amount of $ {max_bid}')
        print(welcome.winner)
        return
    winner_details=tie(user_names,user_ids)
    print(f'The winner of the auction is {winner_details[0]} with user id {winner_details[1]} and an amount of $ {winner_details[2]}')
    print(welcome.winner)
    









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
