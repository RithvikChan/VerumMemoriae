import sublime, sublime_plugin, re, os, subprocess, json
from . import mosspy

def checkDuplicacy():
	print("CHECK")
def mossrun(filesToCheck, fileName):
	userid = 507632796
	#Add all other files
	print("FILES TO CHECK", filesToCheck)
	m = mosspy.Moss(userid, "javscript")
	for fileadd in filesToCheck:
		print("ADDED FILE", fileadd)
		m.addFile(fileadd)
		print("COMPARING WITH", fileName)
		m.addFile(fileName)
		url = m.send() # Submission Report URL
		print ("Report Url: " + url)			
		m.saveWebPage(url+"/match0-top.html", "/home/rithvikchan/Desktop/bleaksubmissions/reports.html")
		#mosspy.download_report(url, "/home/rithvikchan/Desktop/bleaksubmissions/report/", connections=8)
		regexp_link = r'''<A[\s]+([^>]+)>((?:.(?!(\<\/A\>)|IMG))*.)<\/A>'''
		pattern = re.compile(regexp_link)
		x = re.findall(pattern, open("/home/rithvikchan/Desktop/bleaksubmissions/reports.html","r").read())
		startEnd = []
		for i in range(1,len(x),2):
			startEnd.append(x[i][1].split("-"))
		print(startEnd)
		checkDuplicacy()
		print("NO MATCHES!! Good to go")
class BleakHighlighter(sublime_plugin.TextCommand):

	def __init__(self, view):
		self.view = view
		r = []
		#os.system("dir  > C:\\Users\\rithv\\Desktop\\a.txt")  
		log = open("/home/rithvikchan/Desktop/MiniProject/VerumMemoriae/sports/output/bleak_results.json", "r")
		with open("/home/rithvikchan/Desktop/MiniProject/VerumMemoriae/sports/output/bleak_results.json", "r") as content_file:
			content = content_file.read()
		js = json.loads(content)
		print(js["stackFrames"][0])
		run = False
		filex = self.view.window().active_view().file_name()
		listsplits = filex.split("/")
		directory = ""
		for i in range(0,len(listsplits)-1):
			directory+= listsplits[i]+"/"
		file = listsplits[-1]
		filesChecked = []
		issues = []
		for item in js["stackFrames"]:
			items = list(item)
			if(items[0] and file == items[0].split("/")[-1]):
				run = True
				issues.append((items[0].split("/")[-1], (items[1], items[2])))
				r.append(sublime.Region(view.text_point(items[1]-1, 0)+items[2], view.text_point(items[1]-1, 0)+ items[2]+5))
			if(items[0] and items[0].split("/")[-1].split(".")[-1]=="js"):
				filesChecked.append(directory+items[0].split("/")[-1])
		print("ISSUES : ", issues)
		if(run==False):
			mossrun(list(set(filesChecked)), self.view.window().active_view().file_name(), issues)
		self.view.add_regions("inset", r, "comment")

