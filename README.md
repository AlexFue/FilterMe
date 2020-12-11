# Project - *Filter Me* Application

**Filter Me** is a web application where users can apply filters to themselves with their computer’s camera. The user is able to apply to a filter by pressing a microphone icon and saying the filter name or pressing the random filter icon. If the user wants they can also save the image to their computer. 

Submitted by: **Prince Rios, Alex Espinoza Fuentes, Eric Chavez Velez, Edward Cluster & Aundre Labrador**

The following functionality is completed:

* [x] User can **view a list of all usable filters**
* [x] User can **successfully use a functioning microphone button** to ask for desired filter to use
* [x] User's **list of items persisted** upon modification and and retrieved properly on app restart
* [x] User can **tap a random button that generates a random filter** if they don't have 
* [x] and more!

## Video Walkthrough

Here's a walkthrough of our Filter Me Application:

<img src='AppDemo.gif'>

## Installation

OS X & Linux &:

```sh
git clone https://github.com/AlexFue/FilterMe.git
```

## Development Setup 
Make sure to have an environments when downloading these libraries needed. 

Flask, render_template, Response:
```sh
pip install Flask
```

cv2:
```sh
pip install opencv-python
```

Image:
```sh
pip install Pillow
```

sr:
```sh
pip install SpeechRecognition
```
## Usage example
For those who want to have fun and make some fun pictures that you can share with you and your friends. You can now take pictures using our app and have the ability to add filters using your voice! If you like the pictures, you can save them on your computer, CRAZY! Don't go off and have too much fun with this web app guys. 

## Release History
* 0.0.1
    * Created: able to open camera 
* 0.0.2
    * Created: connected voice recognition to camera filters
* 0.0.3
    * Created: Added some stylistic features 
    * Work in progress

## Contributors 
* Aundre Labrador – [Github](https://github.com/aundrelab) – [Linkedin](https://www.linkedin.com/in/aundrelabrador/)
* Alex Espinoza-Fuentes – [Github](https://github.com/AlexFue) – [Linkedin](https://www.linkedin.com/in/alex-espinoza-fuentes/)
* Edward Cluster – [Github](https://github.com/ecluster) – [Linkedin](https://www.linkedin.com/in/edward-cluster/)
* Prince Rios – [Github](https://github.com/princeriostheprodigy) – [Linkedin](https://www.linkedin.com/in/prince-rios-511639194/)
* Eric Chavez – [Github](https://github.com/ericchavez831) – [Linkedin](https://www.linkedin.com/in/echavezvelez/)

## Contributing
1. Fork it at (https://github.com/AlexFue/FilterMe.git)
2. Commit your changes (`git commit -m 'Add comment'`)
3. Push to the branch (`git push origin master`)
4. Create a new Pull Request

## License

    Copyright [2019] [Aundre Labrador, Prince Rios, Eric Chavez, Alex Fuentes, Edward Cluster]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
