# pipelinestraining2

# -------------------------------------------------------------------
# RestApp Solution File structure
# -------------------------------------------------------------------
<!-- 

root
  restApp/
  test/
    unit/
    integration/
  dockerfile
  requirements.txt

-->

# -------------------------------------------------------------------
# restApp prerequisites:
# -------------------------------------------------------------------
<!-- 

- python 3.13
- Redis server
- restApp connects to redis server using "redis" as hostname

 -->

# -------------------------------------------------------------------
# Commands to Run Unit tests and build the image:
# -------------------------------------------------------------------
<!-- 

# Run commands from project root

# Install required python libraries
pip install -r requirements.txt

# Run Unit Tests
python -m pytest test/unit -v

# Build Image
docker build -t restapp:1.0.0 .

 -->

# -------------------------------------------------------------------
# Commands to Run restapp image and redis service:
# -------------------------------------------------------------------
<!-- 

# If container "redisService" exists, stop it and delete it
docker stop "redisService"
docker rm  "redisService"

# Run a container with redis image
docker run --name "redisService" -p "6379:6379" -d redis:alpine

# Get redis container ip dinamically
$redisIP = (docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redisService)[1]

# If container "restapp" exists, stop it and delete it
docker stop "restapp"
docker rm  "restapp"

# Run a container with the "restapp" image we built previously.
# Use the redis container ip to add a host named "redis", this way 
# the restapp container can resolve "redis" hostname
docker run --name "restapp" --add-host "redis:$redisIP" -p "5000:5000" -d restapp:1.0.0

 -->

 # -------------------------------------------------------------------
# Command to run integration tests:
# -------------------------------------------------------------------
<!-- 

# Run integration tests
python -m pytest test/integration -v

 -->

 v1