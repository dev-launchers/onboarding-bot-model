import os

def request_at(path, filename, response):
    # Check if the request was successful
    if response.status_code == 200:
        if not os.path.exists(path):
            os.makedirs(path)
        
        # Full path to the index.html file
        file_path = os.path.join(path, filename)

        # Write the content to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        
        print(f"The file {filename} has been saved in {path} successfully.")
    else:
        print(f"The request failed for {filename}.")
