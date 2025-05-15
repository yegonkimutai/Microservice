<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->

## 🚀 Features

- ✅ Start/Stop node processes with optional config
- 📡 Query node status
- 🔐 API key protected endpoints
- 📝 Simple action/error logging
- 🐳 Docker support
- 🏠 Welcome homepage on root `/`

<!-- PROJECT DESCRIPTION -->

# 📖 Node Agent Microservice <a name="about-project"></a>

- FastAPI microservice that enables the users to start, stop and check the status of the node process.

## 🛠 Built With <a name="built-with"></a>

- Python (FastAPI)

## Note
The Dummy script is located under scripts folder.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Video Demo <a name="live-demo"></a>

- [Video Link](https://www.loom.com/share/d141717491c641a99819a6b833429511?sid=21913a1f-3f89-4de6-a1b6-4797da6927bb)

## Key Features

- Start node process
- Check status of the node
- Stop the node process
- View the logs with timestamps as well as the status
- Dockerized

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Setup

Clone this repository to your desired folder:

Example commands:

```sh

  git clone https://github.com/yegonkimutai/Microservice.git
  cd microservice


```

### Install dependencies

Install the dependencies of this project with:

Example command:

```sh
pip install -r requirements.txt
```

### Run microserver

To run the project, execute the following command:

Example command:

```sh
uvicorn main:app --reload
```

### Run microserver tests

To run tests to ensure that the microserver is working, run the following command in a new terminal (ensure the other terminal is still running):

Example command:

```sh
python test_endpoints.py
```

### Run docker

To run the docker container for this project, first ensure that the docker application is running in the background. Then run the command to build the docker container:

Example command:

```sh
docker build -t microservice .
```

After the build has been succesful, one can run the container in the server in port 8000

Example command:

```sh
docker run -p 8000:8000 microservice
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank Zola Tap.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
