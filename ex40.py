class Song(object):

	politia = ["Cu de astea-mi umbli tu?", "Mama, garcea ma bate", "Nu da, nu da"]

	def __init__(self, lol, haha):
		self.lyrics = lol
		self.ceaifrate = haha
		self.politia = "ma-ta"

	def cantafmm(self):
		for k in self.lyrics:
			print k
		for m in self.ceaifrate:
			print m

	def tacifmm(self):
		for j in self.lyrics:
			print j
		for i in self.politia:
			print i

parazitii = Song(["Ce-ai acolo?", "Ce-am aicea", "Ce-i asta?"], ["Ahahaha", "Loool"])
politia = Song(["Ha ha"], "Poate..")


parazitii.cantafmm()

#politia.cantafmm()

#politia.tacifmm()

parazitii.tacifmm()
