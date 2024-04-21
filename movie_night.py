import cv2
from pyzbar.pyzbar import decode

def read_qr_codes_in_gif(gif_path):
    # Initialize an empty string to store the concatenated content
    combined_content = ''

    # Open the GIF file
    gif = cv2.VideoCapture(gif_path)

    # Iterate through each frame in the GIF
    while True:
        ret, frame = gif.read()
        
        if not ret:
            break

        # Decode QR code
        decoded_objects = decode(frame)

        # Append content of each QR code to the combined_content
        for obj in decoded_objects:
            combined_content += obj.data.decode('utf-8')

    # Release the video capture object
    gif.release()
    return combined_content

if __name__ == "__main__":
    # Path to the GIF file containing QR codes
    gif_path = '/home/max/Downloads/Movie.gif'

    # Read QR codes from the GIF and append their content
    combined_content = read_qr_codes_in_gif(gif_path)

    # Print the combined content
    print(combined_content)
