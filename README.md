# prosodic-assistant
This project uses the Google Assistant SDK and a simple machine learning model to create a smart home assistant. This assistant is influenced by the emotion in the user's voice

## Getting Started

Download this project and unzip it in your desired location
Navigate to that location in a terminal

    python3 -m virtualenv env

Linux

    source env/bin/activate
    sudo apt-get install portaudio19-dev libffi-dev libssl-dev
    sudo python3 -m pip install -r requirements.txt
    
Windows

    source env/bin/activate
    python3 -m pip install -r requirements.txt
   

COMING -- Install Tensorflow and Keras

Follow (these instructions)[https://spotipy.readthedocs.io/en/latest/#getting-started] to set up the Spotify Python API

If you're running this on a Raspberry Pi, you're going to have to set up your audio devices. [This repo](https://github.com/binnes/tobyjnr/wiki/Getting-Sound-to-work-on-the-Raspberry-Pi) was really helpful for me to do that.

## Make your own emotion recognition model

I included a model trained with my own voice to recognize happy or sad, but you will get more accurate results if you train your own. You don't need a fancy GPU or computer, it'll just take longer.

#### Record your dataset

Run:
    
    python3 -m scripts/audio_manager.py
    
This will take you on a 5 x *number of emotions* minute journey of saying 100 2.5 second clips for each specified emotion.

To pause, hold 'p' until the script pauses. 
Press 'r' to resume.

This script will automatically augment your created dataset by including versions of each audio clip that are raised and lowered by 10 decibels. 

#### Train your model

Run:
    
    jupyter notebook
    
Navigate to [scripts/training.ipynb](https://github.com/samwestby/prosodic-assistant/blob/master/scripts/training.ipynb)
Edit the first line in the second cell to point to your dataset

'''python
data_path = 'PATH TO DATASET'
'''

Run every cell in the notebook. In the end you should have your very own emotion recognition model.

#### Check your model

Edit [scripts/valence.py](https://github.com/samwestby/prosodic-assistant/blob/master/scripts/valence.py) to point to your *model.json* and *weights.h5* files.

Run 

    python3 -m scripts/test_model.py
    
Hope that your model is accurately recognizing your vocal emotions.



## Running the Google Assistant SDK - copied from [here](https://github.com/googlesamples/assistant-sdk-python/blob/master/google-assistant-grpc/README.rst)

> **note**
>
> The Google Assistant Service is available for [non-commercial
> use](https://developers.google.com/assistant/sdk/terms-of-service).

Installing
----------

-   You can install using [pip](https://pip.pypa.io/).:

        python3 -m pip install --upgrade google-assistant-grp

Authorization
-------------

-   Follow the steps to [configure the Actions Console project and the
    Google
    account](https://developers.google.com/assistant/sdk/guides/service/python/embed/config-dev-project-and-account).
-   Follow the steps to [register a new device model and download the
    client secrets
    file](https://developers.google.com/assistant/sdk/guides/service/python/embed/register-device).
-   Generate device credentials using `google-oauthlib-tool`:

    > python3 -m pip install --upgrade google-auth-oauthlib[tool]
    > google-oauthlib-tool --client-secrets
    > path/to/client\_secret\_\<client-id\>.json --scope
    > <https://www.googleapis.com/auth/assistant-sdk-prototype> --save
    > --headless

-   Load the device credentials using
    [google.oauth2.credentials](https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.credentials.html). Store them in [scripts/oauth](https://github.com/samwestby/prosodic-assistant/blob/master/oauth).

        import io
        import google.oauth2.credentials

        with io.open('/path/to/credentials.json', 'r') as f:
            credentials = google.oauth2.credentials.Credentials(token=None,
                                                                **json.load(f))

-   Initialize the gRPC channel using
    [google.auth.transport.grpc](https://google-auth.readthedocs.io/en/latest/reference/google.auth.transport.grpc.html).





## Run the Assistant

Now you can finally get the assistant up and running. Pull up your project from [console.actions.google.com](console.actions.google.com)
Run:

    python3 -m scripts/execute.py --device-id <your device id> --project-id <your project id>
    
Say "*Hey buddy*" followed by your desired command. It only uses the emotion model when you say "play music".


## Author

* **Sam Westby** 

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* [Google](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/grpc)
* [Mitesh Puthranneu](https://github.com/MITESHPUTHRANNEU/Speech-Emotion-Analyzer/)
