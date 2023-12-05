import xbmc
import json

current_zoom_level = 1.00

def check_current_zoom():
    global current_zoom_level
    response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.GetViewMode", "id": 1}')
    data = json.loads(response)

    if "result" in data and "zoom" in data["result"]:
        current_zoom_level = data["result"]["zoom"]
        
        if current_zoom_level < 1.00:
            zoom_in()

        else:
            print("Current zoom level is already at 1.00")

def zoom_in():
    target_zoom_level = 1.00
    global current_zoom_level
    zoom_step = 0.01

    while current_zoom_level < target_zoom_level:
        current_zoom_level += zoom_step
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "zoomin" }, "id": 1}')

def adjust_zoom_aspect_ratio():

    for _ in range(23):  
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "zoomout" }, "id": 1}')

    print("Autozoom completed")

# Call the function to check current zoom level first
check_current_zoom()

# Call the function to adjust zoom based on aspect ratio
adjust_zoom_aspect_ratio()
