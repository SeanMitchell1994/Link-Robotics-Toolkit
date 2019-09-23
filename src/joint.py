# source file for joint class

class Joint:

    def __init__(self):
        self.exists = True
        self.joint_type = ""
        self.joint_angle = 0

    def Get_Joint_Type(self):
        return self.joint_type

    def Set_Joint_Type(self, joint_type):
        self.joint_type = joint_type
        return 0