import os, os.path
import shutil

GameMgrFile = "../script/game_mgr.lua"
GameMgrContent = ("if not GameMgr then\n"
"	GameMgr = {}\n"
"end\n\n"

"function GameMgr:Init()\n"
"	\n"
"end\n\n"

"function GameMgr:OnLoop(delta)\n"
"	\n"
"end\n\n")

PreloadFile = "../script/preload.lua"
AppDelegateFile = "../../Classes/AppDelegate.cpp"

def replaceString(filepath, src_string, dst_string):
	content = ""
	f1 = open(filepath, "rb")
	for line in f1:
		strline = line.decode('utf8')
		if src_string in strline:
			content += strline.replace(src_string, dst_string)
		else: 
			content += strline
	f1.close()
	f2 = open(filepath, "wb")
	f2.write(content.encode('utf8'))
	f2.close()

def install():
	assert os.path.isfile(AppDelegateFile) == 1
	replaceString(AppDelegateFile, "hello.lua", "framework/main.lua")

	if os.path.isdir("../script") != 1:
		os.mkdir("../script")
	if os.path.isfile(GameMgrFile) != 1:
		fp = open("../script/game_mgr.lua", "w")
		fp.writelines(GameMgrContent)
		fp.close()
	if os.path.isfile(PreloadFile) != 1:
		fp = open(PreloadFile, "w")
		fp.close()

install()