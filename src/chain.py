# source file for chain class

class Chain:

    def __init__(self):
        self.exists = True
        self.num_links = 1
        self.num_joints = 2

    def Get_Num_Joints(self):
        return self.num_joints

    def Get_Num_Links(self):
        return self.num_links

    def Add_Joint(self, joint_type):
        return 0

    def Add_Link(self):
        return 0

    def Remove_Joint(self):
        return 0

    def Remove_Link(self):
        return 0