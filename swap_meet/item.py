class Item:
    def __init__(self, category="", condition=0) -> None:
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Very Poor"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Very Good"
        elif self.condition == 5.0:
            return "Exceptional"
