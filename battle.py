# __student_name__ = "Samantha Elliott"
# __student_ID__ = "30119057"

#import needed classes
from army import Army, Fighter, Archer, Cavalry, Soldier
from abc import ABC, abstractmethod
from stack import ArrayStack


class Battle(Army, ABC):
    def __init__(self):
        # time complexity: min and max O(1)
        Army.__init__(self)

    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        # time complexity: min and max O(1)
        # reads and creates an army for each player,
        army1 = Army.choose_army(self, "army1", 0)
        army2 = Army.choose_army(self, "army2", 0)
        # sets them in stack formation, and call
        self.__conduct_combat(army1, army2, 0)

    def fairer_combat(self, player_one: str, player_two: str) -> int:
        # time complexity: min and max O(1)
        # reads and creates an army for each player,
        army1 = Army.choose_army(self, "army1", 1)
        army2 = Army.choose_army(self, "army2", 1)
        # sets them in queue formation, and call
        self.__conduct_combat(army1, army2, 1)

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        # time complexity: min O(1) where formation != 0 or 1 and max O(nlog(n))
        if formation != 0 and formation != 1:
            raise ValueError("formation must be 0 for stack or 1 for queue")
        # While each army has at least one fighter unit in the stack:
        # army myst have at least one fighter
        if formation == 0:
            while len(army1.force) >= 1 and len(army2.force) >= 1:
                # pop a fighter from each army (say U1 and U2),
                U1 = army1.force.pop()
                U2 = army2.force.pop()

                # assign s, a and c
                s = Soldier()
                a = Archer()
                c = Cavalry()
                # assign which type to run
                if U1 == s.__str__():
                    U1 = Soldier()
                elif U1 == c.__str__():
                    U1 = Cavalry()
                elif U1 == a.__str__():
                    U1 = Archer()
                # assign which type to run
                if U2 == c.__str__():
                    U2 = Cavalry()
                elif U2 == a.__str__():
                    U2 = Archer()
                elif U2 == s.__str__():
                    U2 = Soldier()

                #follow rules from background
                #if U1.Speed is great that U2.speed U1 will attack first whilst U2 defends first
                if U1.SPEED > U2.SPEED:
                    DAMAGEU1 = U1.attack_damage()
                    U2.defend(DAMAGEU1)
                    #if U2 doesn't die it then attacks and U1 defends
                    if U2.life > 0:
                        DAMAGEU2 = U2.attack_damage()
                        U1.defend(DAMAGEU2)
                #if U2.Speed is great that U1.speed U2 will attack first whilst U1 defends first
                elif U2.SPEED > U1.SPEED:
                    DAMAGEU2 = U2.attack_damage()
                    U1.defend(DAMAGEU2)
                    if U1.life > 0:
                        # if U1 doesn't die it then attacks and U2 defends
                        DAMAGEU1 = U1.attack_damage()
                        U2.defend(DAMAGEU1)

                elif U1.SPEED == U2.SPEED:
                    #if their speeds are equal they both attack and defend at same time
                    DAMAGEU1 = U1.attack_damage()
                    DAMAGEU2 = U2.attack_damage()
                    U1.defend(DAMAGEU2)
                    U2.defend(DAMAGEU1)
                # end of combat both units alive both lose a life
                if U1.life > 0 and U2.life > 0:
                    U1.life = U1.life - 1
                    U2.life = U2.life - 1
                # if on unit alvie and other dead, alive unit gains experience
                elif U1.life > 0 and U2.life == 0:
                    U1.experience = U1.experience + 1
                elif U2.life > 0 and U1.life == 0:
                    U2.experience = U2.experience + 1

                #if the unit is alive push it back onto stack
                if U1.life > 0:
                    army1.force.push(U1)
                if U2.life > 0:
                    army2.force.push(U2)

            #if a stack is empty return who won
            if len(army2.force) == 0 and len(army1.force) == 0:
                # both die return 0
                score = 0
                return score
            elif len(army2.force) == 0 and len(army1.force) != 0:
                # player 1 wins as player 2 army empty
                score = 1
                return score
            elif len(army1.force) == 0 and len(army2.force) != 0:
                # player 2 wins as player 1 army empty
                score = 2
                return score

        # for queue
        elif formation == 1:
            while len(army1.force) >= 1 and len(army2.force) >= 1:
                # 1. pop a fighter from each army (say U1 and U2),

                U1 = army1.force.serve()
                U2 = army2.force.serve()
                # assign s, a and c
                s = Soldier()
                a = Archer()
                c = Cavalry()
                # assign which type to run
                if U1 == s.__str__():
                    U1 = Soldier()
                elif U1 == c.__str__():
                    U1 = Cavalry()
                elif U1 == a.__str__():
                    U1 = Archer()
                # assign which type to run
                if U2 == c.__str__():
                    U2 = Cavalry()
                elif U2 == a.__str__():
                    U2 = Archer()
                elif U2 == s.__str__():
                    U2 = Soldier()

                #follow rules from background
                if U1.SPEED > U2.SPEED:
                    DAMAGEU1 = U1.attack_damage()
                    U2.defend(DAMAGEU1)
                    # if U2 doesn't die it then attacks and U1 defends
                    if U2.life > 0:
                        DAMAGEU2 = U2.attack_damage()
                        U1.defend(DAMAGEU2)

                # if U2.Speed is great that U1.speed U2 will attack first whilst U1 defends first
                elif U2.SPEED > U1.SPEED:
                    DAMAGEU2 = U2.attack_damage()
                    U1.defend(DAMAGEU2)
                    if U1.life > 0:
                        # if U1 doesn't die it then attacks and U2 defends
                        DAMAGEU1 = U1.attack_damage()
                        U2.defend(DAMAGEU1)

                elif U1.SPEED == U2.SPEED:
                    # if their speeds are equal they both attack and defend at same time
                    DAMAGEU1 = U1.attack_damage()
                    DAMAGEU2 = U2.attack_damage()
                    U1.defend(DAMAGEU2)
                    U2.defend(DAMAGEU1)

                # end of combat both units alive both lose a life
                if U1.life > 0 and U2.life > 0:
                    U1.life = U1.life - 1
                    U2.life = U2.life - 1
                # if on unit alvie and other dead, alive unit gains experience
                elif U1.life > 0 and U2.life == 0:
                    U1.experience = U1.experience + 1
                elif U2.life > 0 and U1.life == 0:
                    U2.experience = U2.experience + 1

                # if the unit is alive push it back onto queue
                if U1.life > 0:
                    army1.force.append(U1)
                if U2.life > 0:
                    army2.force.append(U2)

            #if a stack is empty return who won
            if len(army2.force) == 0 and len(army1.force) == 0:
                # both die return 0
                score = 0
                return score
            elif len(army2.force) == 0 and len(army1.force) != 0:
                # player 1 wins as player 2 army empty
                score = 1
                return score
            elif len(army1.force) == 0 and len(army2.force) != 0:
                # player 2 wins as player 1 army empty
                score = 2
                return score
