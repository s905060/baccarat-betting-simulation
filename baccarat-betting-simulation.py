#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import random
from enum import Enum

class NewShoe():
    def __init__(self, number_of_decks=8):
        cards = [2,3,4,5,6,7,8,9,0,0,0,0,1]
        deck = cards * 4
        shoe = deck * number_of_decks
        random.shuffle(shoe)
        self.shoe = shoe
        self.number_of_cards = len(shoe)

class Baccarat():
    def __init__(self, shoe):
        self.banker_value = 0
        self.player_value = 0
        self.banker_1st_card_value = 0
        self.banker_2nd_card_value = 0
        self.banker_3rd_card_value = 999
        self.player_1st_card_value = 0
        self.player_2rd_card_value = 0
        self.player_3rd_card_value = 999
        self.shoe = shoe
        self.number_of_player_win = 0
        self.number_of_banker_win = 0
        self.number_of_tie = 0

    def start_game(self):
        self.banker_1st_card_value = self.shoe.pop()
        self.banker_2nd_card_value = self.shoe.pop()
        self.player_value = self.convert_value(self.banker_1st_card_value + self.banker_2nd_card_value)
        self.player_1st_card_value = self.shoe.pop()
        self.player_2nd_card_value = self.shoe.pop()
        self.banker_value = self.convert_value(self.player_1st_card_value + self.player_2nd_card_value)
        self.check_player_rule()
        self.check_banker_rule()
        return self.player_value, self.banker_value, self.banker_1st_card_value, self.banker_2nd_card_value, self.banker_3rd_card_value, self.player_1st_card_value, self.player_2nd_card_value, self.player_3rd_card_value
    
    def convert_value(self, card_value):
        if card_value >= 10:
            card_value -= 10
        return card_value
    
    def check_player_rule(self):
        """
        Player Hand: When first two cards total:

        1-2-3-4-5-10 Draaws a card
        6-7 Stands
        8-9 Natural -- Stands
        """
        if self.player_value in [1,2,3,4,5,0]:
            self.player_3rd_card_value = self.shoe.pop()
            # print('Player Card Value: %s' % str(self.player_value))
            # print('Player 3rd Card Value: %s' % str(self.player_3rd_card_value))
            self.player_value = self.convert_value(self.player_value + self.player_3rd_card_value)
        elif self.player_value in [6,7,8,9]:
            self.player_value = self.player_value

    def check_banker_rule(self):
        """
        Banker Hand

        First two cards total: Draws when player's third card is: Stands when player's third card is:
        3	 1-2-3-4-5-6-7-9-10	8 
        4	 2-3-4-5-6-7	1-8-9-10 
        5	 4-5-6-7	1-2-3-8-9-10 
        6	 6-7	1-2-3-4-5-8-9-10 
        7	 Stands
        8-9	 Natural -- Stands
        0-1-2	 Always draws 
        """
        if self.banker_value in [0,1,2]:
            self.banker_3rd_card_value = self.shoe.pop()
            self.banker_value = self.convert_value(self.banker_value + self.banker_3rd_card_value)
        elif self.banker_value in [7,8,9]:
            self.banker_value = self.banker_value
        elif self.banker_value == 3:
            if self.player_3rd_card_value in [1,2,3,4,5,6,7,9,0]:
                self.banker_3rd_card_value = self.shoe.pop()
                self.banker_value = self.convert_value(self.banker_value + self.banker_3rd_card_value)
        elif self.banker_value == 4:
            if self.player_3rd_card_value in [2,3,4,5,6,7]:
                self.banker_3rd_card_value = self.shoe.pop()
                self.banker_value = self.convert_value(self.banker_value + self.banker_3rd_card_value)
        elif self.banker_value == 5:
            if self.player_3rd_card_value in [4,5,6,7]:
                self.banker_3rd_card_value = self.shoe.pop()
                self.banker_value = self.convert_value(self.banker_value + self.banker_3rd_card_value)
        elif self.banker_value == 6:
            if self.player_3rd_card_value in [6,7]:
                self.banker_3rd_card_value = self.shoe.pop()
                self.banker_value = self.convert_value(self.banker_value + self.banker_3rd_card_value)

def print_status():
    print('======== Result ========')
    print 'number_of_player_win: %s, Percentage: %f %%' % (str(number_of_player_win), float(number_of_player_win/number_of_hand)*100)
    print 'number_of_banker_win: %s, Percentage: %f %%' % (str(number_of_banker_win), float(number_of_banker_win/number_of_hand)*100)
    print 'number_of_tie: %s, Percentage: %f %%' % (str(number_of_tie), float(number_of_tie/number_of_hand)*100)
    print 'number_of_hand: %s' % str(number_of_hand)
    print 'bet: %s' % str(bet)
    print 'start_bankroll: %s' % str(start_bankroll)
    print 'final_bankroll: %s' % str(bankroll)
    print 'number_of_bet: %s' % str(number_of_bet)
    print 'Total_bet_value： %s' % str(number_of_bet*bet)
    print 'House edge： %s' % str(number_of_bet*bet*0.0106)
    print 'Real Loss： %s' % str(float(start_bankroll-bankroll))
    print 'i_bet_number_of_banker_win: %s' % str(i_bet_number_of_banker_win) 
    print 'i_bet_number_of_player_win: %s' % str(i_bet_number_of_player_win) 
    print 'number_of_win: %s' % str(number_of_win)
    print 'number_of_push: %s' % str(number_of_push) 
    print 'number_of_total_loss: %s' % str(number_of_total_loss)

if __name__ == '__main__':
    number_of_player_win = 0
    number_of_banker_win = 0
    inner_hand = 0
    number_of_tie = 0
    number_of_hand = 0
    number_of_hand = 0
    bankroll = 1500
    start_bankroll = bankroll
    bet = 100
    number_of_win = 0
    number_of_total_loss = 0
    i_bet_number_of_banker_win = 0
    i_bet_number_of_player_win = 0
    number_of_push = 0
    number_of_bet = 0
    max_number_of_hand = 1000
    running_count_threhold = 30

    # 若前二手之差距递减，则下一手下注于最后胜的一方；若差距递增，则下一手下注于最后输的一方。

    while number_of_hand < max_number_of_hand:
        shoe = NewShoe(number_of_decks=8)
        inner_hand = 0
        bet_banker = 0
        bet_player = 0
        bet_tie = 0
        last_winner = 0
        last_hand_value = 0
        last_2_hand_value = 0
        inner_shoe_win = 0
        inner_shoe_loss = 0
        running_card_counting = 0
        while len(shoe.shoe) >= 14:
            # print 'running_card_counting: %s' % str(running_card_counting)
            game = Baccarat(shoe.shoe)
            if bankroll < bet:
                print('I\'m broke... Money: %s' % str(bankroll))
                print_status()
                exit(1)
            else:
                if running_card_counting <= -running_count_threhold:
                    bankroll -= bet
                    number_of_bet += 1
                    bet_player = 1
                    # print 'Bet $%s on Player' % str(bet)
                elif running_card_counting >= running_count_threhold:
                    bankroll -= bet
                    number_of_bet += 1
                    bet_banker = 1
            # elif inner_hand > 1:
            #     pass
                # if inner_shoe_win - inner_shoe_loss >= 1000:
                #     bet_banker = 0
                #     bet_player = 0
                # elif last_2_hand_value > last_hand_value:
                #     # Bet last_winner
                #     if last_winner == 1:
                #         bet_banker = 1
                #     elif last_winner == 2:
                #         bet_player = 1
                # elif last_2_hand_value < last_hand_value:
                #     # Bet last_loser
                #     if last_winner == 1:
                #         bet_player = 1
                #     elif last_winner == 2:
                #         bet_banker = 1
                # if bet_player == 1:
                #     bankroll -= bet
                #     number_of_bet += 1
                #     # print 'Bet $%s on Player' % str(bet)
                # elif bet_banker == 1:
                #     bankroll -= bet
                #     number_of_bet += 1
                #     # print 'Bet $%s on Banker' % str(bet)
            # else:
            #     pass
                # print 'Skip Bet...'

            player_value, banker_value, banker_1st_card_value, banker_2nd_card_value, banker_3rd_card_value, player_1st_card_value, player_2nd_card_value, player_3rd_card_value = game.start_game()
            if player_value > banker_value:
                # print('Player WIN B: %s, P: %s' % (str(banker_value), str(player_value)))
                number_of_player_win += 1
                last_winner = 2

                if bet_player == 1:
                    bankroll += (bet * 2)
                    #print "I won"
                    number_of_win += 1
                    i_bet_number_of_player_win += 1
                    inner_shoe_win += 1
                elif bet_banker == 1:
                    #print "I lost"
                    number_of_total_loss += 1
                    inner_shoe_loss += 1

            elif player_value < banker_value:
                # print('Banker WIN B: %s, P: %s' % (str(banker_value), str(player_value)))
                number_of_banker_win += 1
                last_winner = 1

                if bet_banker == 1:
                    bankroll += (bet * 1.95)
                    # print "I won"
                    number_of_win += 1
                    i_bet_number_of_banker_win += 1
                    inner_shoe_win += 1
                elif bet_player == 1:
                    # print "I lost"
                    number_of_total_loss += 1
                    inner_shoe_loss += 1

            elif player_value == banker_value:
                # print('It\'s a TIE B: %s, P: %s' % (str(banker_value), str(player_value)))
                number_of_tie += 1
                last_winner = 3

                if bet_tie == 1:
                    bankroll += (bet * 8)
                    # print "I won"
                    number_of_win += 1
                elif bet_player == 1 or bet_banker == 1:
                    bankroll += bet
                    number_of_push += 1

            bet_player = 0
            bet_banker = 0
            bet_tie = 0

            if (inner_hand % 2) == 0:
                last_2_hand_value = abs(banker_value-player_value)
                # print 'last_2_hand_value: %s' % str(last_2_hand_value)
            elif (inner_hand % 2) == 1:
                last_hand_value = abs(banker_value-player_value)
                # print 'last_hand_value: %s'  % str(last_hand_value)

            '''
            DEALT CARD WHAT TO DO

            A, 2, 3 Add (+) 1
            4 Add (+) 2
            5, 7, 8 Subtract (-) 1
            6 Subtract (-) 2
            9, 10, J, Q, K
            Neutral – don’t do anything
            '''
            for card in [banker_1st_card_value, banker_2nd_card_value, banker_3rd_card_value, player_1st_card_value, player_2nd_card_value, player_3rd_card_value]:
                if card in [1,2,3]:
                    running_card_counting += 1
                elif card in [4]:
                    running_card_counting += 2
                elif card in [5,7,8]:
                    running_card_counting -= 1
                elif card in [6]:
                    running_card_counting -= 2
            # print "Bankroll %s" % str(bankroll)
            inner_hand += 1
            number_of_hand += 1

            # game.reset()
            # print len(shoe.shoe)
    print_status()