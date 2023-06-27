#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

   
    def testGutterGame(self):
        for i in range(0, 20):
            #error-1
            # self.game.rolls(0)
            # TypeError:rolls is a array storing all roll . its cant be called as method . to fix this we need to make following changes
            # call method roll 
            self.game.roll(0)
            #error-2
            # AttributeError arise score method called that StrikeScore attribute not defined , 
            # to fix this error we need to correct spelling mistake of method 'stickeScore' and change that method name to strikeScore in Bowling Game code            
            # error- 3
            # AssertionError: test Fail as the result value has to be 0 
            # in all 20 attempt, player score 0 in every attempt so final result has to be 0 but its not and result fails 
            # to compare actual score and assert  score ,change method to self.assertEqual instead of assert method
            # AssertionError: result value is 10 but expected value is 0 . now we have to find error in main code but first complete all test 
        self.assertEqual(self.game.score(),0)
    def testAllOnes(self):
        self.rollMany(1, 20)
        # Error-5:
        # AssertionError: test Fail as the result value has to be 20  
        # to compare actual score and assert  score ,change method to self.assertEqual instead of assert method
        # AssertionError: result value is 12 but expected value is 20 . now we have to find error in main code but first complete all test 
        self.assertEqual( self.game.score(),20)
    def testOneSpare(self):
        # self.game.rolls(5)
        # self.game.rolls(5)
        # self.game.rolls(3)
        # Error-10
        # TypeError:rolls is a array storing all roll . its cant be called as method . to fix this we need to make following changes
        # call method roll 
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        # assert self.game.score()==16      
         # Error-11
        # AssertionError: test Fail as the result value has to be 16  
        # to compare actual score and assert  score ,change method to self.assertEqual instead of assert method
        # AssertionError: result value is 18 but expected value is 16 . now we have to find error in main code but first complete all test 
        self.assertEqual( self.game.score(),16)
    def testOneStrike(self):
        # self.game.rolls(10)
        # self.game.rolls(4)
        # self.game.rolls(3)
        # Error-6
        # TypeError:rolls is a array storing all roll . its cant be called as method . to fix this we need to make following changes
        # call method roll 
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        # assert  self.game.score()==24
        # Error-7
        # AssertionError: test Fail as the result value has to be 24  
        # to compare actual score and assert  score ,change method to self.assertEqual instead of assert method
        # AssertionError: result value is 17 but expected value is 24 . now we have to find error in main code but first complete all test 
        self.assertEqual( self.game.score(),24)
    def testPerfectGame(self):
        self.rollMany(10,12)
        # assert self.game.score()==300
        # Error-8:
        # AssertionError: test Fail as the result value has to be 300  
        # to compare actual score and assert  score ,change method to self.assertEqual instead of assert method
        # AssertionError: result value is 30 but expected value is 300 . now we have to find error in main code but first complete all test 
        self.assertEqual( self.game.score(),300)
    def testAllSpare(self):
        self.rollMany(5,21)
        # assert self.game.score()==150
        # Error-9:
        # AssertionError: test Fail as the result value has to be 150  
        # to compare actual score and assert  score ,change method to self.assertEqual instead of assert method
        # AssertionError: result value is 20 but expected value is 150 . now we have to find error in main code but first complete all test 
        self.assertEqual( self.game.score(),150)
    def rollMany(self, pins,rolls):
        for i in range(rolls):
            # Error-4: 
            # TypeError: instead if method array is called , rectify error called roll method instead of rolls array
            self.game.roll(pins)
    
    def testRollInvalidPins(self):
        # boundary value testing 
        # roll for -1 for all 20 balls
        self.rollMany(-1,10)
        self.rollMany(11,10)
        # for invalid value result wil be 0
        self.assertEqual(self.game.score(),0)

    def testRollInvalidCharacter(self):
        # roll for character other then int
        self.rollMany('a',5)
        
        # float value will be converted to int 
        self.rollMany(2.0,5)
        self.rollMany(4.6,10)
        # for invalid value convert into integer and for invalid character result will be 0 
        self.assertEqual(self.game.score(),50)

        