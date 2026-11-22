# CLONE ME: freeze copies of yourself in the live camera picture, then save one photo with all of them.
# Run it from this folder:  python clone_me.py      (modnet.onnx must sit next to this file)
# Lines marked (given) are done for you. Your job is TODO 1 to TODO 4. Do them in order, and run the program after each one.
# Keys in the camera window: SPACE = 3-2-1 then freeze a copy   s = save   u = undo   c = clear   q = quit
# Errors appear in this terminal, not in the camera window.

import os
import time

import cv2
import numpy as np
import onnxruntime

# (given) A: load the AI model (MODNet). It answers "how much of this pixel is a person?" with a number from 0 to 1.
HERE = os.path.dirname(os.path.abspath(__file__))
model = onnxruntime.InferenceSession(os.path.join(HERE, "modnet.onnx"))
INPUT = model.get_inputs()[0].name
FONT = cv2.FONT_HERSHEY_SIMPLEX


def cut_out(frame, size=256):
    # TODO 1: get the matte (one number from 0 to 1 per pixel) for this frame from the AI.
    #   a) Shrink the frame to `size` pixels high. Its width must keep the shape AND be a multiple of 32.
    #   b) Change the colours from BGR (OpenCV's order) to RGB (the model's order), as float32 numbers.
    #   c) Scale the numbers from 0..255 to -1..1, and reorder to the shape (1, 3, height, width). Call it x.
    #   d) Run the model on x, take the one picture it returns, and resize it back to the frame's width and height.
    # Check: sit in front of the camera and press SPACE. After 3-2-1 the terminal says "you fill" more than 0% "of the picture".
    return np.zeros(frame.shape[:2], np.float32)    # (given) placeholder: says "no person anywhere". Replace it.


# (given) B: clean the matte. Keep only the biggest person, fill holes in them, shrink the edge 2 pixels and soften it.
def clean(matte):
    count, labels, stats, _ = cv2.connectedComponentsWithStats((matte > 0.35).astype(np.uint8))
    if count < 2:
        return np.zeros_like(matte)
    biggest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    outline, _ = cv2.findContours((labels == biggest).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    body = cv2.drawContours(np.zeros_like(matte), outline, -1, 1.0, -1)
    body = cv2.erode(body, np.ones((5, 5), np.uint8))
    return cv2.GaussianBlur(body, (9, 9), 0)


def paste(scene, person, matte):
    # TODO 2: blend the person onto the scene. Where the matte is 1 take the person's pixel, where it is 0 keep the scene,
    #   and mix them in between. The matte has one number per pixel, but a pixel has 3 colours, so give it a third axis first.
    #   Return whole numbers from 0 to 255 (uint8), like any picture.
    # Check: freeze a copy, then walk to the other side. Your frozen copy stays in the picture.
    return scene                                    # (given) placeholder: ignores the person. Replace it.


def final_photo(copies):
    # TODO 4: build the photo that is saved, from the frozen copies ONLY (never the live picture).
    #   Start from the newest copy's frame (the room as it was then). Paste every older copy on it.
    #   Then paste the newest you once more, so the newest you is in front.
    # Check: freeze 2 or 3 copies, press s, and open the saved clone_photo file: every copy of you is in it.
    return copies[-1][0]                            # (given) placeholder: only the newest frame. Replace it.


# (given) C: start the camera and the settings the loop needs.
video = cv2.VideoCapture(0)
copies = []
freeze_at = None
last_space = 0
message, message_until = "", 0

while True:
    # (given) D: read a frame, mirror it like a selfie, and get the cleaned matte of the live you.
    ok, frame = video.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)
    matte = clean(cut_out(frame))

    # (given) E: when the 3-2-1 is over, freeze a copy: the frame and a sharper matte (512 pixels high).
    if freeze_at and time.time() >= freeze_at:
        copies.append((frame, clean(cut_out(frame, 512))))
        print(f"Copy {len(copies)}: you fill {round(copies[-1][1].mean() * 100)}% of the picture")
        freeze_at = None

    # (given) F: the live room, then every frozen copy pasted on it.
    view = frame.copy()
    for old_frame, old_matte in copies:
        view = paste(view, old_frame, old_matte)
    # TODO 3: paste the live you on top, so the live you stays in front of your copies (one line, using paste()).
    # Check: walk in front of a frozen copy. You pass in front of it, it does not cover you.

    # (given) G: the countdown, the message and the help line, then show the picture.
    if freeze_at:
        centre = (view.shape[1] // 2 - 40, view.shape[0] // 2 + 50)
        cv2.putText(view, str(int(freeze_at - time.time()) + 1), centre, FONT, 5, (255, 255, 255), 10)
    if time.time() < message_until:
        cv2.putText(view, message, (10, view.shape[0] - 15), FONT, 0.7, (0, 255, 255), 2)
    cv2.putText(view, f"{len(copies)} copies  SPACE freeze  s save  u undo  c clear  q quit", (10, 25), FONT, 0.6, (255, 255, 255), 2)
    cv2.imshow("Clone Me", view)

    # (given) H: the keys. A held SPACE counts once. s saves only when there are 2 or more copies.
    code = cv2.waitKey(5)
    key = chr(code & 255).lower() if code != -1 else ""
    if key in ("q", "\x1b") or cv2.getWindowProperty("Clone Me", cv2.WND_PROP_VISIBLE) == 0:
        break
    if key == " ":
        if time.time() - last_space > 0.7 and not freeze_at:
            freeze_at = time.time() + 3
        last_space = time.time()
    if key == "u" and copies:
        copies.pop()
    if key == "c":
        copies.clear()
    if key == "s":
        if len(copies) < 2:
            message = "Freeze yourself at least 2 times first. Nothing saved."
        else:
            name = time.strftime("clone_photo_%H%M%S.jpg")
            cv2.imwrite(os.path.join(HERE, name), final_photo(copies))
            message = "Saved " + name
        message_until = time.time() + 2

video.release()
cv2.destroyAllWindows()
