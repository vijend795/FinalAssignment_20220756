#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        '''
        this function will run while initializing the code and will create a empty list variable to store all roll data 

        Args: 
        None 

        Return:
        None

        '''
        self.rolls=[]

    def roll(self,pins):
        '''
        this function will append pins data to rolls list

        Args: 
        Arg(int): will append all result value from 0 to 10 

        Return:
        None
        '''
        self.rolls.append(pins)

    def score(self):
        '''
        this function start the game with result and rollIndex value 10.
        total no of roll one player can ball is 10
        this main function  will provide the score according to score pin value , 
        if score is strike (10)then provide one extra strike and bonus point in next two balls
        if score is Spare (10 in two balls ) then bonus point awarded in next one balls
        and then add score in rolls list

        Args:
            None

        Return :
            final actual result value as int between 0  to 301
        '''
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            # Refactoring-1
            # if frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.StrikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                #error- 3 
                # updated value of roll index is out of if statement range, set rollIndex value update inside the if statement 
                rollIndex +=2
            # Refactoring-2
            # return result
            # return statement has to be outside the for loop
        return result

    def isStrike(self, rollIndex):
        '''
        this function is check that if player score 10 in first balls 

        Args:
        rollIndex(int): the first argument between 0 to 11

        Return:
         return as bool: true or false,is checking index value of rolls list is 10 or not
        '''
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        '''
        this function is check that if player score 10 in two continues balls 

        Args:
        rollIndex(int): the first argument between 0 to 11

        Return:
         return as bool: true or false ,is checking sum of two continues index value in rolls list is 10 or not 
        '''
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    #error-2
    #AttributeError arise score method called that StrikeScore attribute not defined , 
    #error in method name so correct spelling to "StrikeScore" instead of "stickeScore"
    def StrikeScore(self,rollIndex):
        '''
        this function run of player score strike and add bonus point for next two balls to actual result which is 10

        Args:
        rollIndex(int): index of roll for strike as the first argument between 0 to 11

        Return:
         int :adding bonus points as pins scored in next two balls after scoring 10 in first ball
        '''
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        '''
        this function run of player score spare ( sum of pins on first ball and 2nd ball is 10 ) and 
        add bonus point for next balls (3rd Ball) to actual result which is 10

        Args:
        rollIndex(int): index of roll for spare as the first argument between 0 to 11

        Return:
         int:adding bonus points on 3rd balls as pins scored after scoring 10 in first and 2nd ball
        '''
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        '''
        this function run when player is score total pins less than 10 in first and 2nd ball

        Args:
        rollIndex(int): index of first roll as the first argument between 0 to 11

        Return:
         int: adding pins for 1st ball and 2nd ball
        '''
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		