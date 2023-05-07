# Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.

def frames_in_minuets(mins, fps):
    mins = mins
    fps = fps * 60 

    total_fps = mins * fps

    return f"The total FPS is {total_fps}"

print(frames_in_minuets(10,25))