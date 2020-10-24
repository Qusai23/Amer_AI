from Player import Player
from Game import Action


class MyPlayer(Player):
    # 1. Add your UINs seperated by a ':'
    #    DO NOT USE A COMMA ','
    #    We use CSV files and commas will cause trouble
    # 2. Write your strategy under the play function
    # 3. Add your team's name (this will be visible to your classmates on the leader board)

    UIN = "126005610"

    global opActions
    opActions= []


    def play(self, opponent_prev_action):
        # Write your strategy as a function of the opponent's previous action and the error rate for prev action report
        # For example, the below implementation returns the opponent's prev action if the error is smaller than 0.5
        # else it returns the opposite of the opponent's reported action
        # Don't forget to remove the example...

        #My strategy starts with Silant Action then if the percentage of the
        #opponenet actions is more than 80% Silent then I return confess to take advantage of nice guy
        #If the percentage of the opponent action has between 20% and 80% Silent actions then I play Silent
        # To cooperate with tit for tart or similar agents
        # If tough guy always confess
        #If the error rate, uncertianity is more than 50% always confess

        global opActions

        if opponent_prev_action == Action.Noop:
            return Action.Silent

        #creat a list of the opponent privous action
        opActions += [opponent_prev_action]

        #Count the number of its actions
        numS = opActions.count(Action.Silent)
        numC = opActions.count(Action.Confess)
        #Get the fraction
        fracS = numS/(numC+numS)
        fracC = numC/(numC+numS)

        if opponent_prev_action == Action.Silent:

            if fracS>0.8:
                return Action.Confess

            elif fracS>0.2:
                return Action.Silent
        else:
            return Action.Confess

        if self.error_rate > 0.5:
            return Action.Confess




    def __str__(self):
        return "Blues"
