# source file for chain class

class Chain:

    def __init__(self, num_links, num_joints):
        self.exists = True
        self.num_links = num_links
        self.num_joints = num_joints

    def Get_Num_Joints(self):
        return self.num_joints
    
    def Get_Num_Links(self):
        return self.num_links