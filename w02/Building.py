class Building:
    def __init__(self,BuildingCode):
        self.BuildingCode = BuildingCode
        
    def __str__(self):
        return f"Building : {self.BuildingCode}"