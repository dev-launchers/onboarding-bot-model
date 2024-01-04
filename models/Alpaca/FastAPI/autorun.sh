# Create caches
cd app
mkdir -p offload
mkdir -p cache
cd ..

# Execute Python script
echo "Download of model..."
if python3 download.py; then
    echo "Download script executed successfully."
else
    echo "Error executing download script. Exiting."
    exit 1
fi

# Check that Docker is running
while true; do
    if docker info &> /dev/null; then
        echo "Docker is launched."
        break
    else
        echo "On hold the start of Docker..."
        sleep 1
    fi
done

# Image and container name
image_name="myimage"
container_name="mycontainer"

# Checks if the container exists and deletes it if it exists
if docker ps -a --filter "name=$container_name" | grep $container_name &> /dev/null; then
    echo "Deleting the existing container: $container_name"
    docker stop $container_name
    docker rm $container_name
fi

# Checks if the image exists and deletes it if it exists
if docker images | awk -v name="$image_name" 'NR>1 && $1 == name { print $3 }' | grep -v '<none>' &> /dev/null; then
    echo "Deleting the existing image: $image_name"
    docker rmi $image_name
fi

# Builds the image
docker build . -t $image_name

# Run the container
docker run -d --name $container_name -p 80:80 $image_name