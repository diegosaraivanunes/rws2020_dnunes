#!/usr/bin/env python
import rospy
from std_msgs.msg import String


class Player:
    def __init__(self, player_name):
        self.player_name = player_name

        red_team = rospy.get_param('/red_team')
        green_team = rospy.get_param('/green_team')
        blue_team = rospy.get_param('/blue_team')

        print('red_team = ' + str(red_team))
        print('green_team = ' + str(green_team))
        print('blue_team = ' + str(blue_team))

        if self.player_name in red_team:
            self.my_team, self.prey_team, self.hunter_team = 'red', 'green', 'blue'
            self.my_players, self.preys, self.hunters = red_team, green_team, blue_team

        elif self.player_name in green_team:
            self.my_team, self.prey_team, self.hunter_team = 'green', 'blue', 'red'
            self.my_players, self.preys, self.hunters = green_team,blue_team, red_team

        elif self.player_name in blue_team:
            self.my_team, self.prey_team, self.hunter_team = 'blue', 'red', 'green'
            self.my_players, self.preys, self.hunters = blue_team, red_team, green_team

        else:
            rospy.logger('My name is not in any team. I want to play!')
            exit(0)

        rospy.logwarn('I am ' + self.player_name + ' and I am on team ' + self.my_team + ' . ' + self.prey_team + ' are going to die ')
        rospy.loginf('I am ' + str(self.hunters))

    def makeAPlayCallBack(self):
        print('Received make a play ...')


def callback(msg):
    print("Received msg containing string" + msg.data)


def main():

    print("Hello player node!")

    rospy.init_node('dnunes', anonymous=False)

    player = Player('dnunes')

    rospy.Subscriber("chatter", String, callback)
    rospy.spin()


if __name__ == '__main__':
    main()