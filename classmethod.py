class Student:
    subject="python"
    @classmethod
    def get_subject(cls):
        return cls.subject

    @classmethod
    def set_subject(cls,new_subject):
        cls.subject=new_subject

print(Student.get_subject())
Student.set_subject("flutter")
print(Student.get_subject())

