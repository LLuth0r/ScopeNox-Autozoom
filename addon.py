import xbmc

def adjust_zoom_aspect_ratio():

    for _ in range(23):  
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "zoomout" }, "id": 1}')

    print("Autozoom completed")

# Call the function to adjust zoom based on aspect ratio
adjust_zoom_aspect_ratio()
