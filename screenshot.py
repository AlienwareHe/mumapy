import send_pic_task

def screen_shot(file_name='screen_shot',file_type='png'):
	print u'screen shot by 3sec'
	time.sleep(3)
	ret = commands.getstatusoutput('scrot '+file_name+'tmp.'+file_type)
	if ret[0]!=0:
		print u'not support'
		return 
	with open(file_name + 'tmp.'+ file_type,"rb") as fp:
		send_pic_task(fp.read(),file_name,file_type)

	os.remove(file_name+'tmp.'+file_type)
	


