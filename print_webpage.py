import pickle

data = pickle.load( open( 'contact_info_dict.pkl' , 'rb' ) , encoding='iso-8859-1' )


# Machine Learning Research, CNeRG
# [Department of Computer Science and Engineering](http://cse.iitkgp.ac.in/) <br>
# [Indian Institute of Technology Kharagpur](http://www.iitkgp.ac.in/) <br>

print('# Machine Learning Research, CNeRG')
print('[Department of Computer Science and Engineering](http://cse.iitkgp.ac.in/) <br>')
print('[Indian Institute of Technology Kharagpur](http://www.iitkgp.ac.in/) <br>\n\n')
for key in data.keys():
	print(key,'\n')
	print( 'Supervisor: ', data[key]['Sup'],'\n')





