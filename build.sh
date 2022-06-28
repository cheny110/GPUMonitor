
TargetDir="/home/chenyongqi/桌面/"
pyinstaller -F app.spec
cp ./license ./dist/
cp ./config.conf ./dist/
rm ./gpumonitor -r


