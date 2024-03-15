# Create caches
mkdir -p app/offload app/cache  # Combine mkdir commands for efficiency

# Install modules (within the activated environment)
pip install --no-cache-dir --upgrade -r requirements.txt

# Install modules 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Execute Python script
if python download.py; then
    echo "Download script executed successfully."
else
    echo "Error executing download script. Exiting."
    exit 1
fi

# Start FastAPI
cd app
uvicorn main:app --reload