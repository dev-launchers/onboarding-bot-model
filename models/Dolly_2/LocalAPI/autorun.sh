# Install modules
# Check OS and install required packages
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    sudo apt-get update
    sudo apt-get install -y libgl1-mesa-glx libglib2.0-0
    pip install --no-cache-dir --upgrade \
        fastapi==0.104.0 \
        uvicorn==0.23.2 \
        accelerate==0.25.0 \
        altair==5.2.0 \
        numpy==1.26.0 \
        scikit-learn==1.3.1 \
        streamlit==1.29.0 \
        torch==2.1.1 \
        transformers==4.35.2 \
        typing_extensions==4.8.0 \
        tensorflow==2.14.0
    #
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS (Assuming Homebrew is used)
    #/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    #brew install apt
    #apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
    pip install --no-cache-dir --upgrade \
        fastapi==0.104.0 \
        uvicorn==0.23.2 \
        accelerate==0.25.0 \
        altair==5.2.0 \
        numpy==1.26.0 \
        scikit-learn==1.3.1 \
        streamlit==1.29.0 \
        torch==2.1.1 \
        transformers==4.35.2 \
        typing_extensions==4.8.0 \
        tensorflow==2.14.0
    #
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    pip install --no-cache-dir --upgrade \
        fastapi==0.104.0 \
        uvicorn==0.23.2 \
        accelerate==0.25.0 \
        altair==5.2.0 \
        numpy==1.26.0 \
        scikit-learn==1.3.1 \
        streamlit==1.29.0 \
        torch \
        transformers \
        typing_extensions==4.8.0 \
        tensorflow
else
    echo "Unsupported OS detected."
    exit 1
fi

# Start FastAPI
cd app
uvicorn main:app --reload