class Lecturer:
    def __init__(self, LecturerFullname):
        self.LecturerFullname = LecturerFullname

    def __str__(self):
        return f"Lecturer : {self.LecturerFullname}"