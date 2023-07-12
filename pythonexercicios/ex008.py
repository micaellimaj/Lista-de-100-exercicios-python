medida = float(input(' uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dam = medida/10
hm = medida/100
km = medida/1000
print(' A medida de {}m corresponde a {}mm e a {}dam' .format(medida,mm,dam))
print('A medida de {}m corresponde a {}hm e a {}km'.format(medida,hm,km))

