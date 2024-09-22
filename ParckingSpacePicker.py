import cv2
import pickle



# the parking space dimensions
width, height = 106, 48
try:
    with open('assets/positions.pkl', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

# Function to get the coordinates of the mouse click
def mouse_click(event, x, y, flags, params):
    # if the left mouse button was clicked add the position to the list
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    # if the right mouse button was clicked remove the position from the list
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            if pos[0] <= x <= pos[0] + width and pos[1] <= y <= pos[1] + height:
                posList.pop(i)
    with open('assets/positions.pkl', 'wb') as f:
        pickle.dump(posList, f)
    

while True:
    # Load the image
    img = cv2.imread('assets/carParkImg.png')
    #cv2.rectangle(img, (51, 94), (157, 146), (0, 255, 0), 2)
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 2)

    cv2.imshow('image', img)
    cv2.setMouseCallback('image', mouse_click)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close the window
cv2.destroyAllWindows()