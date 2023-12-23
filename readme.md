# Open Architects

#### Installing the Project
1. Clone or unzip the project to a folder of your choice and `cd` into the folder
2. Unzip app.zip to app.db (it should be in the same folder as `__init__.py`)
3. Build the Docker image `docker build -t oa-hiring-webdev .`
4. Create a volume for persistence between working sessions `docker volume create webdev_data`
5. Run the Docker container `docker run -d --name oa-hiring-webdev -v webdev_data:/app -p 80:80 oa-hiring-webdev`
6. The project should now be running and exposed on `127.0.0.1` (port 80)

