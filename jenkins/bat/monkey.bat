rem call gradle -g d:\gradle\.gradle\
call gradle clean
call gradle assembleRelease --stacktrace
python monkey.py