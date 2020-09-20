from Utils.constants import Action, NAV_ACTIONS
#from BestFirstSearch.py
class SingleAgentState:

    def __init__(self, p, robot, g, action):
        self.robot = robot
        self.p = p
        self.g = g
        self.action = action

        # TODO: Your job - Set a better heuristic value
        #Here I am using the Manhattan Distance as a heuristic
        #When a corner is dedected I'm adding 3 to account for the missed steps that corners take

        if (abs(self.robot.position_x - self.robot.goal_x))!=0 and (abs(self.robot.position_y - self.robot.goal_y))!=0:
            self.h = abs(self.robot.position_x - self.robot.goal_x) + abs(self.robot.position_y - self.robot.goal_y) + 3
        else:
            self.h = abs(self.robot.position_x - self.robot.goal_x) + abs(self.robot.position_y - self.robot.goal_y)







    def expand(self):
        successors = []
        for action in Action:
            if action.value not in NAV_ACTIONS:
                continue  # Lift, drop, and process are not part of the path planning
            child_robot = self.robot.copy()
            child_robot.plan = [action, action]
            try:
                occupies = child_robot.step()
            except ValueError:
                continue  # Ignore illegal actions
            if child_robot.warehouse.are_open_cells(occupies[0], self.robot.carry):
                successors.append(SingleAgentState(self, child_robot, self.g + 1, action))
        return successors

    def get_plan(self, plan):
        if self.p is not None:
            plan.append(self.action)
            self.p.get_plan(plan)
        return

    def is_goal(self):
        return self.robot.at_goal()

    def __eq__(self, other):
        return self.robot == other.robot

    def __hash__(self):
        return hash(self.robot)

    def __lt__(self, other):
         return self.g + self.h < other.g + other.h

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return self.g + self.h <= other.g + other.h

    def __str__(self):
        return "%d,%d" %(self.robot.position_x, self.robot.position_y)