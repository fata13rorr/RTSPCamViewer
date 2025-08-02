• This project came about to solve a problem for a friend who owns a bar, the security cam NVRs monitors only show tha channels currently being recorded by that NVR. 
You cant add feeds to any other zone you need eyes on. In order to get around this I suggested we use the RTSP feeds that many NVRs are capable of putting out, grab one for each needed channel, and stream them to a Raspberry pi or other SBC/Minicomp with a monitor attached. 

•This litle script allows you to do that. 

• Just fill in the URL for the 4 feeds you want to show, (make sure you get the syntax right for your particular NVR as they all have their own little thing going on.)  

• The easiest way to do this is using a Windows machine to run <a href="https://sourceforge.net/projects/onvifdm/">ONVIF ODI</a> and scan your local network for your RTSP feeds, 
(<a href="https://www.cameraftp.com/CameraFTP/software/Download_Virtual_Security_System.aspx">Camera FTP</a> also works well.)
This will give you the correct URL syntax you can then copy/paste into the config.py 
