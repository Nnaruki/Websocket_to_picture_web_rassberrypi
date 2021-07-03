import cv2

def processImage(img):
  cv2.imwrite('test.jpg', img)

def input_with_timeout(timeout):
  (ready, _, _) = select.select([sys.stdin], [], [], timeout)
  if ready:
    return sys.stdin.readline()
  else:
    return ''

if __name__ == "__main__":
  vc = cv2.VideoCapture(0)
  while True:
    result, img = vc.read()
    cv2.imshow('frame', img)
    key = cv2.waitKey(50) & 0xFF
    if key == ord('q'):
      break
    if key == ord('c'):
      processImage(img)
    
  vc.release()
  cv2.destroyWindow('frame')
