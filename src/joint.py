# source file for joint class

class Joint:

    def __init__(self):
        self.exists = True
        self.joint_type = ""
        self.joint_angle = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def Get_Joint_Type(self):
        return self.joint_type

    def Set_Joint_Type(self, joint_type):
        self.joint_type = joint_type
        return 0

    def Set_x(self, x):
        return 0

    def Get_x(self, x):
        return 0

    def Set_y(self, x):
        return 0

    def Get_y(self, y):
        return 0

    def Set_z(self, x):
        return 0

    def Get_z(self, z):
        return 0