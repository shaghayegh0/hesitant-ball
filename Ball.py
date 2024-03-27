class Ball:
    def __init__(self, size, weight, direction, speed, height, kinetic, gpe):
        self.size = size            # 0.1
        self.weight = weight        # 10
        self.direction = direction  # (0,-1) 
        self.speed = speed          # 10
        self.height = height        # 5
        self.kinetic = kinetic      # 500 
        self.GPE = gpe              # 500
    
    def setKinetic(self):
        self.kinetic = (1/2) * self.weight * self.speed
    
    def setGPE(self):
        self.GPE =  self.weight * 9.8 * self.height

    
    
