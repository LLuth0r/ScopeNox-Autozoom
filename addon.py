import requests

# Kodi JSON-RPC API URL
kodi_url = 'http://localhost:8080/jsonrpc'  # Replace with your Kodi's IP and port

# Function to get the video width and height
def get_video_params():
    payload = {
        "jsonrpc": "2.0",
        "method": "Player.GetProperties",
        "params": {
            "playerid": 1,  # Assuming playerid 1 is the video player
            "properties": ["currentvideostream"]
        },
        "id": 1
    }

    response = requests.post(kodi_url, json=payload)

    data = response.json()
    if "result" in data and "currentvideostream" in data["result"]:
        video_info = data["result"]["currentvideostream"]
        width = video_info["width"]
        height = video_info["height"]
        return width, height
    else:
        return None, None

# Function to adjust zoom based on aspect ratio
def adjust_zoom_aspect_ratio():
    target_zoom_level = 0.77  # Set your desired target zoom level here

    width, height = get_video_params()

    if width is not None and height is not None:
        aspect_ratio = width / height

        if 1.35 <= aspect_ratio <= 1.85:  # 16:9 aspect ratio
            zoom_action = "zoomout"
        elif 2.00 <= aspect_ratio <= 2.40:  # 21:9 aspect ratio
            zoom_action = "zoomin"
        else:
            zoom_action = None

        if zoom_action:
            current_zoom_level = 1.0
            zoom_step = 0.01

            while abs(current_zoom_level - target_zoom_level) >= zoom_step:
                if zoom_action == "zoomout":
                    current_zoom_level -= zoom_step
                elif zoom_action == "zoomin":
                    current_zoom_level += zoom_step

                # Execute the zoom action
                payload = {
                    "jsonrpc": "2.0",
                    "method": "Input.ExecuteAction",
                    "params": {
                        "action": zoom_action
                    },
                    "id": 1
                }

                response = requests.post(kodi_url, json=payload)

                print(f"{zoom_action.capitalize()} - Current Zoom Level: {current_zoom_level:.2f}")

    else:
        print("Video width and height not available for this video.")

# Call the function to adjust zoom based on aspect ratio
adjust_zoom_aspect_ratio()
