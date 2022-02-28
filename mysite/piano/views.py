from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse
from piano.camera import Webcam
# Create your views here.  IPWebCam, MaskDetect,LiveWebCam

def indexView(request):
	if request.method == 'POST':
		return redirect(pianoView)
	return render(request, 'piano/index.html')		

def pianoView(request):
	if request.method == 'POST':
		return redirect(indexView)
	return render(request, 'piano/piano.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
	detection = Detection(image)	
	# initialise switch
	switch = True
	while True:
		# use motion detection to get active cell
		cell = detection.get_active_cell(image)
		if cell == None: continue
		# if switch on, play note
		if switch:
			winsound.Beep(NOTES[cell], 1000)			
		# alternate switch    
		switch = not switch

def video_feed(request):
	return StreamingHttpResponse(gen(Webcam()),
					content_type='multipart/x-mixed-replace; boundary=frame')