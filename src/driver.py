from kinematic_chain import Chain

arm = Chain()

print(arm.Get_Num_Joints())
print(arm.Get_Num_Links())

arm.Add_Joint("revolute")
arm.Add_Link()

print(arm.Get_Num_Joints())
print(arm.Get_Num_Links())

arm.Add_Joint("revolute")
arm.Add_Link()

print(arm.Get_Num_Joints())
print(arm.Get_Num_Links())