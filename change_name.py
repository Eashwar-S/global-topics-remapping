import os
import re
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def process_file(file_path, file_extension):
    encoding = detect_encoding(file_path)
    
    with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
        content = file.read()

    # Update publisher patterns for Python
    content = re.sub(r'rospy\.Publisher\(\s*["\']/(.*?)["\']', r'rospy.Publisher("\1"', content)

    # Update subscriber patterns for Python
    content = re.sub(r'rospy\.Subscriber\(\s*["\']/(.*?)["\']', r'rospy.Subscriber("\1"', content)

    # Update publisher patterns for C++
    content = re.sub(r'>\(\s*["\']/(.*?)["\']', r'>("\1"', content)

    # Update subscriber patterns for C++
    content = re.sub(r'subscribe\(\s*["\']/(.*?)["\']', r'subscribe("\1"', content)

    with open(file_path, 'w') as file:
        file.write(content)

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, file_extension = os.path.splitext(file_path)

            if file_extension in [".py", ".cpp"]:
                process_file(file_path, file_extension)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    folder_path = "/home/ros/Desktop/Transbot_Code/jetson/transbot_ws/src"
    process_folder(folder_path)


