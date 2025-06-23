import cv2 as cv
import time
import webbrowser
from detectors.gesture_detector import HandDetector
from config.gesture_config import CONFIG
from core.gesture_manager import handle_gesture
from utils.always_on_top import set_always_on_top
from logs.gesture_log import log_action
from core.mode_manager import setmode, getmode
from utils.window_utils import snap_browser_to_side, snap_opencv_window


def main():
    cap = cv.VideoCapture(0)
    detector = HandDetector()
    prev_time = 0
    last_action_time = 0
    action = ""
    action_timestamp = 0
    window_visible = True

    # Load config
    cooldown = CONFIG["gesture_delay"]
    win_w, win_h = CONFIG["frame_width"], CONFIG["frame_height"]
    pos_x, pos_y = CONFIG["window_position"]
    window_name = "Zesture"

    # Setup OpenCV window
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.resizeWindow(window_name, win_w, win_h)
    cv.moveWindow(window_name, pos_x, pos_y)
    set_always_on_top(window_name)
    snap_opencv_window(window_name, side="left")

    flag1 = False
    flag = False
    show_text = False
    img = cv.imread('utils/gestures.png')
    img = cv.resize(img, (700, 700))

    while True:
        success, frame = cap.read()
        if not success:
            continue

        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame)
        current_time = time.time()


        cv.putText(frame, "Press 'i' for instructions, 'd' to exit",(30,70),cv.FONT_HERSHEY_SIMPLEX, 0.9, (48, 25, 52), 2)
 
        # Mode switch keys
        key = cv.waitKey(1) & 0xFF
        if key == ord('i'):
            flag1 = not flag1
        elif key == ord('y'):
            webbrowser.open("https://www.youtube.com/watch?v=X1DRDcGlSsE&list=RDX1DRDcGlSsE&start_radio=1&rv=X1DRDcGlSsE")
            setmode("youtube")
            snap_browser_to_side("YouTube", side="right")
            flag = True
        elif key == ord('s'):
            webbrowser.open("https://open.spotify.com/album/4eCFWvtSHO4MWsCfJzyNR4?si=rq7plmWRRSeMfpKW13sDFw&nd=1&dlsi=738afdfe1f054796")
            setmode("spotify")
            snap_browser_to_side("Spotify", side="right")
            flag = True
        elif key == ord('t'):
            setmode("system")
            flag = True
        elif key == ord('r'):
            show_text = not show_text

            if(show_text == False):
                cv.destroyWindow("Gestures")

        if flag1:
            cv.putText(frame, "Press 'y' for YouTube,",(30,90),cv.FONT_HERSHEY_SIMPLEX, 0.65, (48, 25, 52), 2)
            cv.putText(frame, "      's' for Spotify,",(30,110),cv.FONT_HERSHEY_SIMPLEX, 0.65, (48, 25, 52), 2)
            cv.putText(frame, "      't' for System,",(30,130),cv.FONT_HERSHEY_SIMPLEX, 0.65, (48, 25, 52), 2)
            cv.putText(frame, "      'r' for Gestures List,",(30,150),cv.FONT_HERSHEY_SIMPLEX, 0.65, (48, 25, 52), 2)
            cv.putText(frame, "      'i' again to close",(30,170),cv.FONT_HERSHEY_SIMPLEX, 0.65, (48, 25, 52), 2)
        
        if show_text:
            cv.putText(frame, "Press 'r' again to close",(30,190),cv.FONT_HERSHEY_SIMPLEX, 0.65, (48, 25, 52), 2)
            cv.putText(frame, "Close gestures and access modes",(30,210),cv.FONT_HERSHEY_SIMPLEX, 0.65, (48, 25, 52), 2)
            cv.imshow('Gestures', img)
            cv.moveWindow('Gestures', 700, 180)

        
        if(flag == True):
            # Show current mode
            mode = getmode()
            cv.putText(frame, f"Mode: {mode}", (30, 230), cv.FONT_HERSHEY_SIMPLEX, 0.65, (153, 0, 76), 2)

        # Gesture detection
        if lmList:
            fingers = detector.fingersUp(lmList)
            print("Fingers:", fingers)

            if current_time - last_action_time > cooldown:
                action = handle_gesture(fingers)

                if action == "Fullscreen":
                    window_visible = not window_visible
                    if not window_visible:
                        cv.destroyWindow(window_name)
                    else:
                        cv.namedWindow(window_name, cv.WINDOW_NORMAL)
                        cv.resizeWindow(window_name, win_w, win_h)
                        cv.moveWindow(window_name, pos_x, pos_y)
                        set_always_on_top(window_name)
                        snap_opencv_window(window_name, side="left")

                if action:
                    action_timestamp = current_time
                    last_action_time = current_time
                    log_action(action)

        # Display action text temporarily
        if current_time - action_timestamp < 1.5 and window_visible:
            cv.putText(frame, action, (30, 250), cv.FONT_HERSHEY_SIMPLEX, 0.65, (51, 0, 25), 2)

        # FPS display
        fps = 1 / (time.time() - prev_time + 1e-5)
        prev_time = time.time()

        if window_visible:
            cv.putText(frame, f"FPS: {int(fps)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            cv.imshow(window_name, frame)

        if key == ord('d'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
