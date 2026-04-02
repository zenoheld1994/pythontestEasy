#Operators works as they help with automation, Infra as code, and maanging cloud services
#Python scripts handle logic
# current_instances = 5
# additional_instances = 3
# total_instances = current_instances + additional_instances
# print(f"Total EC2 instances is {total_instances}")

# timeout=30
# load_factor =2
# timeout *= load_factor
# print(f"Updated timeout: {timeout}")
# cpu_utilization =85
# if cpu_utilization >80 :
#     print("CPU is above 80%, scale up!")
# else:
#     print("CPU is stable")
# memory_utilization =65
# if cpu_utilization > 80 and memory_utilization<70:
#     print("Deploy new instance")
# else:
#     print("Everything is okay")

minimum =18

age = int(input("Provide your age:"))

if (age>=18):
   print("You may drink")
else:
    print("You are not allowed to drink")