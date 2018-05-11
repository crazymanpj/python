rem 执行改批处理前先要目录下创建font_properties文件 

echo Run Tesseract for Training.. 
tesseract.exe code.Letter.exp0.tif code.Letter.exp0 nobatch box.train 
 
echo Compute the Character Set.. 
unicharset_extractor.exe code.Letter.exp0.box 
mftraining -F font_properties -U unicharset -O code.unicharset code.Letter.exp0.tr 


echo Clustering.. 
cntraining.exe code.Letter.exp0.tr 

echo Rename Files.. 
rename normproto code.normproto 
rename inttemp code.inttemp 
rename pffmtable code.pffmtable 
rename shapetable code.shapetable  

echo Create Tessdata.. 
combine_tessdata.exe code. 

echo Backup
copy e:\backup\better\code.Letter.exp0.box e:\backup\better\code.Letter.exp0.backup.box /y
copy d:\kuaipan\python\autopublishpackage\script\data\code.Letter.exp0.box e:\backup\better\code.Letter.exp0.box /y

echo Update Tessdata
copy d:\kuaipan\python\autopublishpackage\script\data\code.traineddata "d:\Program Files (x86)\Tesseract-OCR\tessdata\code.traineddata" /y

echo. & pause