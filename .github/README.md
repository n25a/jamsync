<div align="center">
  <a rel="noreferrer noopener" href="https://user-images.githubusercontent.com/49960770/229376239-cb7f5104-fee8-4bd9-87d2-a5a97aa259ef.png">
    <img src="https://user-images.githubusercontent.com/49960770/229376239-cb7f5104-fee8-4bd9-87d2-a5a97aa259ef.png" 
        alt="Logo">

  </a>

  <p align="center">
    Logo made by 
    <a href="https://manne.ir/">Mann-E</a>.
    Courtesy of 
    <a href="https://haghiri75.com">Muhammadreza Haghiri</a>.
  </p>

  <h1 align="center">JamSync</h1>

  <h3 align="center">
    Sync your currently playing song on Spotify with your social media's bio!
  </h3>
</div>
<br>
<br>

Welcome to the "jamsync" repository! 
Using the Spotify API, "jamsync" retrieves the name of the song you're listening to and 
updates your bio to display the title of the song. This provides an easy way 
for your social media contacts to see what you're currently listening to and start a conversation 
about your music taste.  
With "jamsync", you can effortlessly share your favorite tunes with your social media community and 
make new music connections. The setup process is simple and the script runs in the background, 
so you can focus on enjoying your music while "jamsync" takes care of the rest.  

Thank you for checking out "jamsync"!

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)


## Features
JamSync is a Python script and can update Skype bio for now.  
I need to add more social media support with your contributions.


## Usage
To use "jamsync", you must have a Spotify account and a Spotify-Client-ID.
You can get a Spotify-Client-ID by following the instructions 
on [this video](https://developer.spotify.com/documentation/general/guides/app-settings/) and apply it 
to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).  

#### Note: set the redirect URI to `"http://localhost:8080/callback"`

Then you should clone the repository and install the dependencies. You can install "jamsync" dependencies
with the following command:

```bash
pip install -r requirements.txt
```

You need the config file to run the script and the `example.config.ini` file is an example of the config file.
After filling the config file, you can run the script with the following command:

```bash
CONFIG_PATH=./config.ini python jamsync.py
```

The environment variable `CONFIG_PATH` is the path to the config file.


### Config File
The config file is an INI file, and it has 2 sections:

- [Spotify]
    - `client_id`: Your Spotify-Client-ID (Required)
    - `client_secret`: Your Spotify-Client-Secret (Required)

- [Skype]
    - `enabled`: set it true for now (Required) :))
    - `username`: Your Microsoft-Account-Username (Required)
    - `password`: Your Microsoft-Account-Password (Required)


## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create.
Any contributions you make are **greatly appreciated**. You can contribute to this project by 
checking [the document](https://github.com/n25a/jamsync/blob/master/.github/CONTRIBUTING.md).


## Contact
You can contact me on [Email](mailto:n.twenty.five.a@gmail.com).
