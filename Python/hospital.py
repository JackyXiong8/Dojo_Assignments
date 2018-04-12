import random

# class Patient:
#     def __init__(self,name,allergies):
#         self.id = random.randint(10,99)
#         self.name = name
#         self.allergies = allergies
#         self.bed = None

# class Hospital:
#     def __init__(self,name,capacity):
#         self.patients = []
#         self.name = name
#         self.capacity = capacity
#         self.rooms = {}
#         for i in range (0, capacity):
#             self.rooms[i] = "available"

#     def admit(self,sick):
#         if len(self.patients) >= self.capacity:
#             print ("Hospital is full, sorry")
#             return self
#         else:
#             self.patients.append(sick)
#             print ("You have been admitted to",self.name,"hospital.")
#             for key, value in self.rooms:
#                 if value == "available":
#                     patient.bed = key
#                     self.rooms[key] = "unavailable"
#         return self
#     def discharge(self, sick):
#         for i in range(0, len(self.patients)):
#             if self.patients[i].name == sick.name:
#                 self.patients.remove(self.patients[i])
#                 self.rooms[sick.bed] = "available"
#                 return self

#     def info(self):
#         print (self.patients, self.name,self.capacity)
    

# jacky = Patient("Jacky","None")

# mercy = Hospital("Mercy",10)

# mercy.admit(jacky).info()


class Patient:
    def __init__(self,name,allergies):
        self.id = random.randint(0,10)
        self.name = name
        self.allergies = allergies
        self.bed = None

class Hospital:
    def __init__(self,name,capacity):
        self.name = name
        self.patients = []
        self.capacity = capacity
        self.rooms = {}
        for value in range(0,capacity):
            self.rooms[value] = "available"
        
    def Admit(self,patient):
        if len(self.patients) >= self.capacity:
            print ("The hospital is full, sorry.")
            return self
        else:
            self.patients.append(patient)
            for x, y in self.rooms.items():
                if y == "available":
                    patient.bed = x
                    self.rooms[x] = "unavailable"
                    return self
    def Discharge(self, patient):
        for z in range (0,len(self.patients)):
            if self.patients[z].name == patient.name:
                self.patients.remove(self.patients[z])
                self.rooms[patient.bed] = "available"
                return self
                


patient1 = Patient("Jacky","None")
patient2 = Patient("Jason", "none")
patient3 = Patient("Jackson", "none")

print (patient1.name, patient1.id)

hospital1 = Hospital("Mercy", 10)

print (hospital1.name, hospital1.capacity)

hospital1.Admit(patient1).Admit(patient2).Admit(patient3)

print (hospital1.patients[0].name, hospital1.patients[1].name, hospital1.patients[1].bed)

hospital1.Discharge(patient1)
