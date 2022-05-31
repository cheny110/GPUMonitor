
TargetDir="/home/chenyongqi/桌面/"
pyinstaller -F app.py
cp ./license ./dist/
cp ./config.json ./dist/
rm ./gpumonitor -r
mv ./dist/app ./gpu-monitor

