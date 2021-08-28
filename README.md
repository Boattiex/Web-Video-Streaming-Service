# Web-Video-Streaming-Service
Use Django + Nginx + Javascript

This project was created for the Co-Operative Education (Year:2019)

at National Electronics and Computer Technology Center (NECTEC)
with Internet Innovation Research Team (INO) in Thailand

Especially my friend Thanawich In-um!

We learned about how to using linux (Ubuntu), docker, WebRTC (Kurento), GStreamer, try to use API from program "NxWitness", Node.Js, Python and Django.

In the End, We decided to use Django + Nginx!

We are divided into 2 parts
1. Media Server 
2. Application Server

1. Media Server 
  - It is the part that receives video and audio streams, including format conversion for viewing in each format.
  We use Nginx with RMTP Modules, which is an important part to work with application server.
  
  Config Nginx 
    - Address when start streaming (use on_publish such as on_publish http://172.0.0.1:5000/start_stream
    - Address when the strraming is end (use on_publish_done such as on_publish http://172.0.0.1:5000/stop_stream
    
  and make API to work with Application Server
    

2. Application Server
  - We use Django and create the system for generate stream key. The user must have a Stream key before they can streaming.
  - Before the straming will start, The system will check the stream key.
  If the stream key is unique or not used, The system will allow user to streaming and save start streaming datetime as well as start recording video clips.
  - When the streaming is over, the streaming history will be saved as a video clip on the server(stop_stream).


