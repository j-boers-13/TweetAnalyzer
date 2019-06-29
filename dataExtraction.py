import json
from nltk.tokenize import word_tokenize
import re
import os
import json

def main():

	months = ["may.txt","june.txt","july.txt"]

	may = open('maytags.txt','w+')
	june = open('junetags.txt','w+')
	july = open('julytags.txt','w+')
	keywords = """actonclimate,sustainabilitygo100percent,renewableenergy,agw,algae,arra,biodiesel,biodiversity,bioenergy,biofuels,biomass,biopower,carbonprice,cleanairact,cleanair,cleanenergy,cleantech,
	climatecrisis,climatehawks,climatezombies,solar,solarenergy,spill,sustainableagriculture,sustainability,susty,saveourseas,rainforest,recycle,renewables,
	responsibletravel,reuse,plastic,pollution,peakoil,permaculture,pesticides,publictransit,pv,oceans,offsets,oil,oilspill,organic,nature,marinelife,greentravel,
	greenjobs,greenisgood,greenict,gmo,ghg,gas,geothermal,gogreen,fuelcell,econews,ecosystem,ecofriendly,eco,earthtweet,renewables,climatechange,offgrid,shellno,parisclimateaccord,parisaccord,paris,parisclimateagreement,pca,trump,dumptrump,climatedenier,climate,climateaction,arctic,globalwarming,	environment,carbon,methane,parisagreement,cop21,greenhouseeffect,solar,solarenergy,oceans,co2,notmypresident,#climatesummit,climatemarch,divestforparis,keepitintheground,natgas,emissions,uniting4climate,cop22,cop23""".split(",")
	hashkeys = [('#' + str(keyword)) for keyword in keywords]

	for filename in months:
		print(filename + "-"*70)
		monthfile = open(filename,"r")
		lines = [line.rstrip('\n') for line in monthfile]
		
		tweetamount = 0
		
		for actFile in lines:
			data = []

			f = open(actFile, 'r')
			for line in f:
				try:
					tweet = json.loads(line)
					if tweet['lang'] == 'en':
						data.append(tweet)
				except:
					continue
					
			f.close()
			
			
			for tweet in data:
			
				tweetamount += 1
				
				if len(tweet['text']) <= 140:
					tweettxt = tweet['text']
					tweettxt = tweettxt.replace('#',' #')
					for punct in '.!",;:%<>/~`()[]{}?…@\n':
						tweettxt = tweettxt.replace(punct,'')
					tweettxt = tweettxt.split()
					
					for word in tweettxt:

						if word[0] == "#" and word in hashkeys or word in keywords:
								match = word.lower()
								match = match.split('\'')[0] 
							
								if len(match)>0:
									if filename == "may.txt":
										may.write(match + "\n")
									if filename == "june.txt":
										june.write(match + "\n")
									if filename == "july.txt":
										july.write(match + "\n")
		t = open('totalamounts.txt','a')
		t.write(filename + " " + str(tweetamount) + "\n")
		t.close()								
		monthfile.close()
		
	may.close()
	june.close()
	july.close()
		       
main()

