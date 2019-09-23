# source file for chain class
from joint import Joint
from link import Link

class Chain:

    def __init__(self):
        self.exists = True
        self.num_links = 0
        self.num_joints = 0
        self.joint_list = []
        self.link_list = []

    def Get_Num_Joints(self):
        return self.num_joints

    def Get_Num_Links(self):
        return self.num_links

    def Add_Joint(self, joint_type):
        j_tmp = Joint()
        j_tmp.Set_Joint_Type(joint_type)
        self.joint_list.append(j_tmp)
        self.num_joints += 1
        return 0

    def Add_Link(self):
        l_tmp = Link()
        self.link_list.append(l_tmp)
        self.num_links += 1
        return 0

    def Remove_Joint(self):
        return 0

    def Remove_Link(self):
        return 0