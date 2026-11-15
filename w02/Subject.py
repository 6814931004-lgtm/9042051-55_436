class Subject:
    def __init__(self,SubjectCode,SubjectName,SubjectUnits):
        self.SubjectCode = SubjectCode
        self.SubjectName = SubjectName
        self.SubjectUnits = SubjectUnits

    def __str__(self):
        return f"Subject : {self.SubjectCode} - {self.SubjectName} ({self.SubjectUnits} units)"