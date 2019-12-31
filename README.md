# video-n-pic
Turn a video into a sequence of frames or opposite.


#Dependency
Python 3.7.3

#Install requirement
Run
```
./src/install.sh
```



# video to pictures

1. Put your video in `input/` folder.
2. Run 

```
python video2pic.py --job v2p --video_name test.mp4 
```
3. Get the output pictures in `output/` folder.


# pictures to video

1. Put your pictures in `input/` folder.
NOTE: your pictures should be named in order. Ex: frame1.jpg, frame2.jpg, frame3.jpg ..... frameN.jpg
If type of picture is not jpg, please change the extension `'*.jpg'` in `line 32: pics = sorted(glob.glob(os.path.join(pics_dir, '*.jpg'))`.



2. Carefully check the `WIDTH`and `HEIGHT` of your input pictures.
3. Run 
```
python video2pic.py --job p2v --WIDTH 1280 HEIGHT 720
```
4. Get the output video in `output/` folder.
