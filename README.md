## ScopeNox-Autozoom

This script was written to automatically adjust the digital zoom needed while using a CIH (Constant Image Height) setup on a scope screen (2.35 or 2.40).  

This script will detect the playing media, by making a standard http POST request to the local server.  Once it has the video information, it determines the aspect ratio of the film based on the video width/height.

After it has this info, it executes the `zoomout` or `zoomin` action to adjust the digital zoom based on the aspect ratio.

For standard 16:9 films, this means the digital zoom would be `0.77`.

For 2.35 & 2.40 films, I zoom in a few steps (`1.03`) to ensure the picture fills my screen completely.  I typically have my projector zoomed so that there is a slight spill onto the border of the screen.

### Dependecies
This script relies on the Kodi Add-on `*requests*`.  Please follow this link to download the zip and install.  Yes, it's safe to download.
https://kodi.tv/addons/nexus/script.module.requests/

### **Things to Note**

The url used is set for the localhost, without authentication.  If you are using authentication, you would need to adjust this parameter so that it includes your username & password inside the url.  

*Example:*

`kodi_url = 'https://<username>:<password>@<kodi-ip-address>:port/jsonrpc `

There are some issues with back to back playback and the autozoom not working.  I'm still trying to figure out why there are issues and will update when I have it resolved.

### **Another Note for 4K Content**

This currently does not work on 4K Content.  4K Content always reports a `3840x2160` resolution, which makes it a 16:9 format.  I am exploring a work-around for this and will update the script when I have this resolved.