#saving file
'''
	plt.savefig("filename.svg")
	plt.savefig("filename.svg",dpi=400)
	plt.savefig("filename.svg",dpi=400,bbox_inches='tight')
	facecolor,edgecolor
	format : png,pdf,ps,svg,eps...
'''	
from matplotlib import pyplot as plt
from io import BytesIO
buffer = BytesIO()
plt.savefig(buffer)
plot_data = buffer.getvalue()
plt.show()