## ScopeNox-Autozoom

This script was written to automatically adjust the digital zoom needed while using a CIH (Constant Image Height) setup on a scope screen (2.35 or 2.40).  

This script will detect the playing media, by checking the playing video aspect ratio on load.  Once it has the video information, if it meets the conditions of a non-scope format film, it'll automatically zoom the content out.

For standard 16:9 films, this means the digital zoom would be `0.77`.


### **Things to Note**

This currently does not work on 4K Content.  4K Content always reports a `3840x2160` resolution, which makes it a 16:9 format.  I am exploring a work-around for this and will update the script when I have this resolved.