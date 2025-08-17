# Event Manager — CS50x Final Project

##Introduction
**Event Manager** is a web application developed as my final project for **CS50x: Introduction to Computer Science (2025)**.  
The platform allows users to **discover, create, and manage events** within their local communities. Its main purpose is to connect people through activities in their neighborhoods, such as book clubs, sports events, cultural gatherings, or community meetings.

The idea came from the need to have a simple and accessible tool that promotes **community engagement** and encourages people to participate in real-life activities instead of being disconnected.

---

## Technologies Used

This project was built using the following technologies:

- **Python** (main programming language)
- **Django Framework** (backend & logic)
- **SQLite3** (database system)
- **HTML5, CSS3 ** (frontend)
- **Bootstrap** (styling and responsiveness)
- **GitHub** (version control and project hosting)

---

## Features

The main features of the **Event Manager** application include:

1. **User Authentication**

   - Sign up, login, and logout functionality.
   - Secure password handling with Django authentication.

2. **Event Creation**

   - Users can create their own events by providing title, description, date, time, and location.

3. **Event Registration**

   - Any logged-in user can register for available events.
   - Events display a list of participants.

4. **Leave Event Functionality**

   - Users can unregister from an event they previously joined.

5. **Event Browsing**

   - Homepage shows all active events.
   - Events can be filtered by neighborhood or category.

6. **User Dashboard**

   - Users can see the events they created or registered for.

7. **Responsive UI**
   - Designed with Bootstrap for desktop and mobile accessibility.

---

## Project Structure

Here is an overview of the most important files and directories:

event_manager/ # Main Django project folder
│
├── manage.py # Django management script
│
├── db.sqlite3 # SQLite database
│
├── README.md # Project documentation (this file)
│
├── events/ # Django app handling event logic
│ ├── models.py # Database models (Event, Registration, etc.)
│ ├── views.py # Application views (event list, details, create, register, leave)
│ ├── urls.py # URL routing for events app
│ ├── templates/ # HTML templates
│ │ ├── base.html
│ │ ├── event_confirm_delete.html
│ │ ├── event_detail.html
│ │ ├── event_edit.html
│ │ ├── event_form.html
│ │ ├── event_list.html
│ │ ├── event_registrations.html
│ │ ├── event_register.html
│ └── forms.py # Django forms for event creation & registration
│
├── users/ # Django app for user authentication
│ ├── models.py # User model (extended if needed)
│ ├── views.py # Authentication views (login, register, logout)
│ ├── urls.py # URL routing for users app
│ ├── templates/ # HTML templates for authentication
│ │ ├── login.html
│ │ ├── register.html

---

## Design Choices

Some important design decisions made during development:

- **Django Framework** was chosen because it provides an integrated authentication system, ORM, and a structured way of building web apps.
- **SQLite3** was selected as the database because it is lightweight, file-based, and sufficient for a student project.
- **Bootstrap** was used to save time on CSS design and ensure responsiveness.
- **Separate apps (`events`)** were created to keep code modular and easier to maintain.

---

## How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/Olsion23/event-manager.git
   cd event-manager
   ```

Create and activate a virtual environment

python -m venv venv
source venv/bin/activate # On Linux/Mac
venv\Scripts\activate # On Windows

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Create a superuser (admin account)

python manage.py createsuperuser

Start the development server

python manage.py runserver

Open the app in your browser:

http://127.0.0.1:8000/

## Video Demo

As part of CS50x’s final project requirements, I have also prepared a short video demo showcasing the main functionality of Event Manager.

## YouTube Link: https://youtu.be/sEF-Kyey_ko

## GitHub Repository

The source code is available here:
https://github.com/Olsion23/event-manager.git

## Conclusion

This project helped me practice full-stack web development with Django, apply principles of software design, and learn how to organize, test, and deploy a real-world application.

It was both a challenging and rewarding experience, and I am proud to present it as my final project for CS50x 2025.

## License

This project is free to use under the MIT License.
See the [LICENSE](LICENSE) file for details.

## Author

Olsion Bejleri

CS50x 2025 Student

Passionate about Full-Stack Development, AI, Software Engineering, and Data Engineering.

GitHub Profile
https://github.com/Olsion23

## Acknowledgments

Special thanks to Harvard University’s CS50 staff for providing one of the best learning experiences in computer science, and to the online community for continuous support and inspiration.
