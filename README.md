# PyATEMAPI

Python Blackmagic Design ATEM REST API

## Purpose

To provide a web API for interfacing with ATEM Switchers. The API is designed to be as simple as possible and to be as flexible as possible.

Why build a web API for ATEM?

This API allows developers to interact with ATEM Switchers without having to write desktop code. Instead, developers can now interact with
an ATEM through the browser using simple web APIs with Javascript.

## Roadmap / Features

-   [x] Fully Documented in [Postman](https://documenter.getpostman.com/view/19380446/UzQpvT1y)
-   [x] Web Example
-   [x] Get tally data
-   [x] Fade to black
-   [x] Cut
-   [x] Auto transition
-   [x] Set preview
-   [x] Set program
-   [x] DSK Tie
-   [x] DSK Cut
-   [x] Ping switcher
-   [ ] Upload media
-   [x] Tested using ATEM Television Studio HD

## Usage

Clone PyATEMAPI to your machine by running:

`git clone https://github.com/mackenly/PyATEMAPI.git`

While in the directory of the project, run server.py to start the server. Pass in as parameters the IP address of the ATEM Switcher and a
simple passphrase for basic authentication.

`python server.py 127.0.0.1 Password1`

After starting the server, you can use the web API to interact with the ATEM Switcher.

#### Testing

If you would like to test this API, you can use a tool called [PyATEMSim](https://github.com/jonknoll/pyAtemSim). In the
directory of the simulator simply run `python atem_server.py` and you will be able to interact with the ATEM Switcher's provided path and
port via this API. This simulator doesn't provide all the functionality of a real switcher and seems to have issues with input numbers so
don't rely on it for important testing.

## Documentation

The API documentation is available through Postman at
[https://documenter.getpostman.com/view/19380446/UzQpvT1y](https://documenter.getpostman.com/view/19380446/UzQpvT1y).

## Demo

To demonstrate and test the API, a basic web example is provided. To run the example, enter the `web-example` directory, modify the const
in at the top of `script.js` with the values you're using to run the server, then open the `index.html` file in a browser.

<img src="./assets/example-screenshot.jpg" width="500">

## Docker

The application can be run via docker. This can be built using the repository defined container definition or using
the DockerHub registered container.

### Run from DockerHub

You can run the application from the built images in DockerHub.

```bash
docker run -d -p 5555:5555 nuvious/pyatemapi:latest [SERVER_IP] ([PASSPHRASE])
```

### Run with docker-compose

First define the parameters for the server in a `.env` file. A template is provided in `.env_template`.

```plaintext
SERVER_IP=192.168.1.42
PASSPHRASE=MySecretPassword
```

You can then start the service:

```bash
docker-compose up -d
```

You can also explicitly define the path to the env file if you are managing multiple configurations:

```bash
docker-compose --env-file .env_alt up -d
```

You can then bring the service down with a standard docker-compose down command:

```bash
docker-compose down
```

### Build and run Docker container from source

```bash
docker build -t pyatemapi .
docker run -d -p 5555:5555 pyatemapi [SERVER_IP] ([PASSPHRASE])
```

## Contributing

Contributions are welcome. Please open an issue or pull request on [mackenly/PyATEMAPI](https://github.com/mackenly/PyATEMAPI).

## License

[The MIT License (MIT)](./LICENSE.md)
