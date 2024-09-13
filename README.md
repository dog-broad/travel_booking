# 🧳 Travel Booking Application

Welcome to the **Travel Booking Application**! This Django-based project was developed as part of an assignment for the Software Engineer Intern position at Travel Lykke.

## 🌟 Project Motivation

This project was created to showcase proficiency in Django, building functional web applications, and understanding travel booking systems. It was created using Django for the backend, Bootstrap for the frontend, and MySQL as the database.

## 📦 Features

- **User Authentication**: Register, log in, and manage user profiles.
- **Travel Options**: Browse and book various travel options (Flights, Trains, Buses).
- **Booking Management**: Make, view, and cancel bookings.
- **Responsive Design**: Enhanced with Bootstrap for a clean, modern look.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Django
- Bootstrap
- MySQL (or your preferred database)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/dog-broad/travel_booking.git
   cd travel_booking
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

### Access the Application

- **Home Page**: [http://localhost:8000/](http://localhost:8000/)
- **Admin Interface**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 📄 Usage and Functionality

### User Registration

- **Endpoint**: `/register/`
- **Function**: Users can create an account, which logs them in and redirects to the travel options page.

### User Login

- **Endpoint**: `/login/`
- **Function**: Users log in to access the travel options page. Invalid credentials show an error message.

### User Logout

- **Endpoint**: `/logout/`
- **Function**: Logs out the user and redirects to the landing page.

### User Profile Management

- **Endpoint**: `/profile/`
- **Function**: Users can view and update their profile information.

### Viewing Travel Options

- **Endpoint**: `/travel-options/`
- **Function**: Displays available travel options for users to browse and book.

### Booking Tickets

- **Endpoint**: `/book-ticket/<travel_id>/`
- **Function**: Users can book tickets for a selected travel option, with total price calculated based on seats.

### Viewing Bookings

- **Endpoint**: `/view-bookings/`
- **Function**: Shows a list of the user’s bookings.

### Canceling Bookings

- **Endpoint**: `/cancel-booking/<booking_id>/`
- **Function**: Users can cancel a specific booking, updating its status and increasing available seats.

### Admin Panel

- **Function**: Superusers manage travel options through the Django admin interface.

## 🛠️ Tools & Technologies

- **Django**: Web framework for building the application.
- **Bootstrap**: Front-end framework for responsive design.
- **MySQL**: Database for storing data (configurable).
- **Python**: Programming language used for development.

## 📅 Upcoming Features

- **Advanced Search**: Implement advanced search for travel options.
- **Payment Integration**: Add payment gateway support for bookings.
- **User Dashboard**: Enhance user profile with booking history and preferences.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Feel free to contribute by submitting issues or pull requests. Your feedback and improvements are welcome!

