import sublime, sublime_plugin, re, os, subprocess, json

class MarkdownLinksCommand(sublime_plugin.TextCommand):
	def __init__(self, view):
		self.view = view    
		stopWords = ['word1', 'word2', 'word3'] 
		r = []
		#os.system("dir  > C:\\Users\\rithv\\Desktop\\a.txt")  
		log = open("/home/rithvikchan/Desktop/MiniProject/VerumMemoriae/sports/output/bleak_results.json", "r")
		with open("/home/rithvikchan/Desktop/MiniProject/VerumMemoriae/sports/output/bleak_results.json", "r") as content_file:
			content = content_file.read()
		js = json.loads(content)
		print(js["stackFrames"][0])
		for item in js["stackFrames"]:
			file = self.view.window().active_view().file_name().split("/")[-1]
			items = list(item)
			if(items[0] and file == items[0].split("/")[-1]):			
				 r.append(sublime.Region(view.text_point(items[1]-1, 0)+items[2], view.text_point(items[1]-1, 0)+ +items[2]+5))
		self.view.add_regions("inset", r, "comment")
