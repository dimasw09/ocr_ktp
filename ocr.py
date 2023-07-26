import cv2
import pytesseract
import os

def read_image(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

    result = pytesseract.image_to_string(threshed, lang="ind")

    final = []
    for word in result.split("\n"):
        if "”—" in word:
            word = word.replace("”—", ":")
      
        if "NIK" in word:
            nik_char = word.split()
        if "?" in word:
            word = word.replace("?", "7") 
      
        final.append(word)
    return final

if __name__ == "__main__":
    if not os.path.exists("KTPscan"):
        os.makedirs("KTPscan")
        
    image_files = [f for f in os.listdir("KTPscan") if os.path.isfile(os.path.join("KTPscan", f))]

    for image_file in image_files:
        image_path = os.path.join("KTPscan", image_file)
        extracted_text = read_image(image_path)

        with open(f"KTPscan/{image_file}.txt", "w") as file:
            file.write("\n".join(extracted_text))
