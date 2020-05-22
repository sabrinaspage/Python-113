#Sabrina Reyes
'''
Design the classes based on the UML diagram given below, including string
representation and the initialization of the each class. You must pay attention to the
classes and their relationship as well as the variables and the methods in the classes.
'''
class SchedulerSPM():
	def __init__(self):
		pass
	def __str__(self):
		pass
	def Configure():
		pass
SPM = SchedulerSPM()

class SchedulerAedesAegypti(SchedulerSPM):
	def __init__(self):
		pass
	def __str__(self):
		pass

AA = SchedulerAedesAegypti()

class SchedulerMammal(SchedulerSPM):
	def __init__(self):
		pass
	def __str__(self):
		pass

M = SchedulerMammal()

class SchedulerVegetation(SchedulerSPM):
	def __init__(self):
		pass
	def __str__(self):
		pass

V = SchedulerVegetation()


class SchedulerContainer(SchedulerSPM):
	def __init__(self):
		pass
	def __str__(self):
		pass

C = SchedulerContainer()

class SchedulerMeteorology(SchedulerSPM):
	def __init__(self):
		pass
	def __str__(self):
		pass

M = SchedulerMeteorology()

print("Mosquito class:")
class AedesAegypti(SchedulerAedesAegypti):
	def __init__(self, lifeStage, energyLevel):
		self.lifeStage = lifeStage
		self.energyLevel = energyLevel
	def __str__(self):
		return "Life Stage: {}\nEnergy Level: {}/10\n".format(self.lifeStage, self.energyLevel)
	def Birth():
		pass
	def Metamorphosis():
		pass
	def Death():
		pass
	def FlyingRandomly():
		pass
	def LookForRestingPlace():
		pass
	def LookForPlant():
		pass
	def Feeding():
		pass
	def Mating():
		pass
	def Ovipositing():
		pass

AedesAegypti_one = AedesAegypti("larvae", 4)
print(AedesAegypti_one.__str__())

print("Mammal class:")
class Mammal(SchedulerMammal):
	def __init__(self, traceIntensity):
		self.traceIntensity = traceIntensity
	def __str__(self):
		return "Trace Intensity: {}\n".format(self.traceIntensity)
	def MovingRandomly():
		pass
	def UpdateTrace():
		pass

Mammal_one = Mammal(20)
print(Mammal_one.__str__())

print("Vegetation class:")
class Vegetation(SchedulerVegetation):
	def __init__(self, trace_intensity):
		self.trace_intensity = trace_intensity
	def __str__(self):
		return "Trace Intensity: {}\n".format(self.trace_intensity)
	def UpdateTrace():
		pass

Vegetation_one = Vegetation(54)
print(Vegetation_one.__str__())

print("Container class:")
class Container(SchedulerContainer):
	def __init__(self, percentageLiquid, volatilityLiquid, percentageExposure, traceIntensity):
		self.percentageLiquid = percentageLiquid
		self.volatilityLiquid = volatilityLiquid
		self.percentageExposure = percentageExposure		
		self.traceIntensity = traceIntensity
	def __str__(self):
		return "Percentage Liquid: {}%\nVolatility Liquid: {}σ\nPercentage Exposure: {}%\nTrace Intensity: {}\n"\
			.format(self.percentageLiquid, self.volatilityLiquid, self.percentageExposure, self.traceIntensity)
	def MovingRandomly():
		pass
	def UpdateTrace():
		pass

Container_one = Container(33, 45, 10, 55)
print(Container_one.__str__())

print("Meteorology class:")
class Meteorology(SchedulerMeteorology):
	def __init__(self, windDirection, windDirectionMaxSpeed, accumRainfall, accumSolarRadiation,
				 globalSolarRadiation, airTemp, highAirTemp, lowAirTemp, airRelativeHumidity,
				 windSpeed, highWindSpeed):
		self.windDirection = windDirection
		self.windDirectionMaxSpeed = windDirectionMaxSpeed
		self.accumRainfall = accumRainfall
		self.accumSolarRadiation = accumSolarRadiation
		self.globalSolarRadiation = globalSolarRadiation
		self.airTemp = airTemp
		self.highAirTemp = highAirTemp
		self.lowAirTemp = lowAirTemp
		self.airRelativeHumidity = airRelativeHumidity
		self.windSpeed = windSpeed
		self.highWindSpeed = highWindSpeed
	def __str__(self):
		return "windDirection: {}\nwindDirectionMaxSpeed: {} m/s\naccumRainfall: {} inches \naccumSolarRadiation: {} K\
				\nglobalSolarRadiation: {} K\nairTemp: {} F\nhighAirTemp: {} F \nlowAirTemp: {} F \nairRelativeHumidity: {} F\
				\nwindSpeed: {} m/s\nhighWindSpeed: {} m/s\n".format(self.windDirection, self.windDirectionMaxSpeed, self.accumRainfall, self.accumSolarRadiation,
			self.globalSolarRadiation, self.airTemp, self.highAirTemp, self.lowAirTemp, self.airRelativeHumidity,
			self.windSpeed, self.highWindSpeed);
	def updateData():
		pass

Meteorology_one = Meteorology("north-west", 90, 80, 70, 80, 30, 80, 10, 35, 50, 95)
print(Meteorology_one.__str__())