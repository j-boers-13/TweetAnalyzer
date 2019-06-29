from collections import Counter
import operator
import re	
import matplotlib.pyplot as plt

def main():

		# Creating the dictionaries per month
		may = open('maytags.txt','r')
		words = may.read().split('\n')
		maydict = {}
		
		for word in words:
			maydict[word] = maydict.get(word, 0) + 1
		may.close()
		
		june = open('junetags.txt','r')
		words2 = june.read().split('\n')
		junedict = {}
		
		for word in words2:
			junedict[word] = junedict.get(word, 0) + 1
		
		july = open('julytags.txt','r')
		words3 = july.read().split('\n')
		julydict = {}
		
		for word in words3:
			julydict[word] = julydict.get(word, 0) + 1
		
		dicts = [maydict,junedict,julydict]
		months = ['may','june','july']	
		
		# Visualization per month
		
		for d,month in zip(dicts,months):
			print(month)
			d = dict((k, d[k]) for k in d if k)
			hashtagdict = dict((k, d[k]) for k in d if k[0] == '#')
			keyworddict = dict((k, d[k]) for k in d if k[0] != '#')

			sorted_hash = sorted(hashtagdict.items(), key=operator.itemgetter(1), reverse=True)
			sorted_key = sorted(keyworddict.items(), key=operator.itemgetter(1), reverse = True)

			for sortedx in [sorted_hash,sorted_key]:
				xword = [x[0] for x in sortedx[0:10]]
				yfreq = [x[1] for x in sortedx[0:10]]
				plt.figure(figsize=(20,10))
				if sortedx == sorted_hash:
					plt.title(month + " " + "hashtags")
				else:
					plt.title(month + " " + "keywords")

				plt.bar(range(len(yfreq)), yfreq, align = 'center')
				plt.xticks(range(len(xword)), xword)

				print("Close the window of the plot to show the next one.")
				plt.show()

		
		print("Data analysis completed.")
			


main()
			


