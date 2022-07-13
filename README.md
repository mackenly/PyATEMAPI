# PyATEMAPI
 Python ATEM REST API

## Purpose
To provide a web API for interfacing with ATEM Switchers. The API is designed to be as simple as possible and to be as flexible as possible.

Why build a web API for ATEM?

This API allows developers to interact with ATEM Switchers without having to write desktop code. Instead, developers can now interact with an ATEM through the browser using simple web APIs with Javascript.

## Roadmap / Features
- [x] v0.1 Get list of inputs and their tally data
- [x] v0.1 Get individual input's tally data
- [x] v0.2 Implement [connection methods](https://clvlabs.github.io/PyATEMMax/docs/methods/connect/)
- [ ] v0.2 Implement [execute methods](https://clvlabs.github.io/PyATEMMax/docs/methods/exec/)
- [ ] v0.2 Implement [get methods](https://clvlabs.github.io/PyATEMMax/docs/data/)
- [ ] v0.2 Implement [set methods](https://clvlabs.github.io/PyATEMMax/docs/methods/set/)

## Usage
Clone PyATEMAPI to your machine by running:

```git clone https://github.com/mackenly/PyATEMAPI.git```

While in the directory of the project, run setup.py to start the server. Pass in as parameters the IP address of the ATEM Switcher and simple passphrase for basic authentication.

```python server.py 127.0.0.1 Password1```

After starting the server, you can use the web API to interact with the ATEM Switcher.

<br>**Testing**<br>
If you would like to test this API, you can use a tool called [PyATEMSim](https://github.com/jonknoll/pyAtemSim).
In the directory of the simulator simply run `python atem_server.py` and you will be able to interact with the ATEM Switcher's provided path and port via this API.

## Documentation
The API documentation is available through Postman at [https://documenter.getpostman.com/view/19380446/UzQpvT1y](https://documenter.getpostman.com/view/19380446/UzQpvT1y).

## Contributing
Contributions are welcome. Please open an issue or pull request on [mackenly/PyATEMAPI](https://github.com/mackenly/PyATEMAPI).
