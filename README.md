<p align="center">
<img src="https://i.postimg.cc/XvHcvShj/NUB-logo.png" alt="N.U.B"/></p>



# North Underground Bands (N.U.B)
Welcome to this repository dedicated to my first side-project as a programming student.
I transformed the project into a web application akin to a social network. The primary goal of this network is to share groups from the Lille underground music scene. A user can authenticate to share various information about a music group, such as contact details, merchandise, and events using typical "CRUD" operations.


For now, I've named this interface N.U.B for "North Underground Bands". Feel free to explore the site and navigate through structured data.


I am open to any suggestions for improvement!

<hr>
Here you can find an overview from a new user's point of view:
- The user must create an account to access the content.
- He can also edit his account, add a profile photo, or delete it.
- He can also create objects (Bands / Merch / Events) and perform classic CRUD operations on the objects he owns.
<br><br>

https://github.com/user-attachments/assets/1569f255-e0df-4040-9c3f-5ab1dd054ae4

<br>

- By navigating through the lists of objects, the user will see that they are sorted by their first letter.
- A functional like counter is also implemented for the "Band" and "Merch" objects.<br>

- By accessing a "Band" object, a music player is visible if and only if the content creator downloads wav or mp3 files.
- When creating a "Band" or "Merch" object, the user can upload a photo, otherwise a default image is assigned to the object.<br>

- A “classified ads” system is also implemented on the home page. A user can respond directly to an ad via N.U.B's integrated messaging.
- The user can also access all their messages via a "social network messenger" type interface.
<br><br>


https://github.com/user-attachments/assets/0d6ff564-c7cf-4b53-8525-bcc96a6144a4

<br>

- Finally, the classic “About” and “Contact” pages allow the user to find out more about N.U.B, consult the terms of policy or contact the admin.

### Technologies Used
<hr>

- <b>Backend:</b> Django

- <b>Frontend:</b> HTML, CSS (no frameworks or templates)

- <b>Scripting:</b> JavaScript

- <b>Database:</b> SQLite

### Testing
<hr>
The project includes comprehensive testing to ensure functionality and reliability. Here is the summary of the test results:
<br><br>

```
----------------------------------------------------------------------
Ran 14 tests in 8.022s

OK
Destroying test database for alias 'default'...
```
### Authentication and Messaging
<hr>
N.U.B includes a robust authentication system and a messaging feature, allowing users to communicate securely within the platform.

### Dependencies and Environment
<hr>
The project relies on the following dependencies:
<br><br>

`asgiref==3.8.1`

`certifi==2024.7.4`

`charset-normalizer==3.3.2`

`cloudinary==1.40.0`

`Django==5.0.6`

`django-appconf==1.0.6`

`django-cloudinary-storage==0.3.0`

`django-imagekit==5.0.0`

`idna==3.7`

`numpy==2.0.0`

`opencv-python==4.10.0.84`

`pilkit==3.0`

`Pillow==10.0.0`

`requests==2.32.3`

`six==1.16.0`

`sqlparse==0.5.0`

`typing_extensions==4.12.2`

`urllib3==2.2.2`

### Features
<hr>
N.U.B offers a range of social network-like features, including:
<br><br>

- Authentication: Secure user authentication system.

- Messaging: In-app messaging for users to communicate.

- Sharing: Users can share band information, merchandise, events, and ads.

- Access Control: Limited access for non-logged-in users.

- Search Functionality: Quick search feature to find bands, events, and more.

### Future Enhancements and New Features
<hr>
N.U.B is continuously evolving, and here are some exciting features and improvements planned for the future:

- **Enhanced Music Player**: Improve the music player to allow navigation through the duration of audio files, providing a better user experience for listening to music.
- **Marketplace Integration**: Replace the Merch section with a full-fledged marketplace where users can buy and sell music-related products.
- **Customizable User Pages**: Allow users to create and customize their pages similar to MySpace or Bandcamp, giving them the freedom to express their personal or band identity.
- **Ticketing System**: Implement a ticketing system for events, making it easy for users to purchase tickets and attend concerts or other music events.
- **Social Wall**: Introduce a feature similar to Facebook's wall, where users can post updates, share content, and interact with each other.
- **News Feed and Stories**: Create a news feed and a short video feature akin to Instagram Stories, enabling users to share moments and stay connected with the community in real-time.

We are committed to enhancing the user experience and providing a platform that caters to the needs of the music community. Your feedback and suggestions are invaluable in shaping the future of N.U.B.
<hr><br>
Feel free to explore the code and contribute to the project.<br>Your feedback and contributions are highly appreciated!<br><br>
To run the application locally, execute these commands:<br>

- `git clone https://github.com/CLMNTDFR/N.U.B.git` <br>
- `pip install -r requirements.txt` <br>
- `cd django-web-app/merchex/` <br>
- `python3 manage.py runserver` <br>
<br><br>
You can now visit the website on the `localhost8000` and make an account.<br>
Have fun!
