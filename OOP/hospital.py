class patients():
    def __init__(self,Id_num,Name, Age, Allergies, Bed_num = None):
        self.Id_num = Id_num
        self.Name = Name
        self.Age = Age
        self.Allergies = Allergies
        self.Bed_num = Bed_num

    def info(self):
        print "ID number is: ", self.Id_num
        print "Name is: ", self.Name
        print "Known allergies are: ", self.Allergies
        print "Bed Number is: ", self.Bed_num

class Hospital():
    def __init__(self,name,capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        print "Hospital name: ", self.name

    def admit(self,new_patient):
        if (len(self.patients) >= self.capacity):
            print "Hospital full.Zero beds available."
        else:
            self.patients.append(new_patient)
            print "Successfully admitted patient number: " ,len(self.patients)
            new_patient.Bed_num = len(self.patients)
            print "Patient bed is: " ,new_patient.Bed_num
        return self

    def discharge(self,cured_patient):
        self.patients.remove(cured_patient)
        print "Patient", cured_patient.Name, "discharged"
        cured_patient.Bed_num = None
        print "patient bed reset to number: ", cured_patient.Bed_num
        return self

patient0 = patients(000000, " WORLD WAR Z ",00, ["NOISE", "MOVEMENT"])
patient0.info()

test = Hospital("Rush",5)
test.admit(patient0)
test.discharge(patient0)
