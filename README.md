# Doctor Appointment Booking System API

Welcome to the **Doctor Appointment Booking System API** repository! This API provides a seamless way for patients to book, manage, and cancel doctor appointments. The system also supports different user roles, including admins, managers, doctors, and patients.

## Features

- **User Registration**: Register as a **patient**, **doctor**, **manager**, or **admin**.
- **Patient Appointment Booking**: Patients can view available time slots and book appointments.
- **Appointment Management**: Patients can manage (view, cancel, reschedule) their appointments.
- **Doctor's Dashboard**: Doctors can view, accept, or decline appointments.
- **Manager Role**: Managers can manage doctor availability and patient appointments.
- **Admin Role**: Admins have full control over the system, including user management and role assignments.
- **Automated Reminders**: Send email and/or SMS reminders to patients and doctors about upcoming appointments.
- **Search and Filters**: Patients can search doctors by specialty, location, or availability.

## Table of Contents

- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [User Management](#user-management)
  - [Appointments](#appointments)
  - [Doctor Dashboard](#doctor-dashboard)
  - [Admin and Manager Roles](#admin-and-manager-roles)
- [Example Requests](#example-requests)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To use this API, you need a REST client like Postman or Insomnia.

### Base URL
https://127.0.0.1:8000/api/v1/


### Authentication

All endpoints require an **API Key** or **JWT Token** for authentication. After registration, users will receive a JWT token, which should be included in the `Authorization` header as a Bearer token.

### Roles

The system supports the following user roles:
- **admin**: Full system access, including user management.
- **manager**: Manages doctors' schedules and patient appointments.
- **doctor**: Medical professional who manages their appointments.
- **user (patient)**: Patient who can book and manage their own appointments.

### Environment Variables

Make sure to set the following environment variables:
- `DB_URI`: Database connection URI
- `JWT_SECRET`: Secret key for signing JWT tokens
- `MAIL_API_KEY`: For sending email notifications
- `SMS_API_KEY`: For sending SMS notifications

## API Endpoints

### Authentication

#### POST /auth/register

Register a new user (admin, manager, doctor, or patient).

- **Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "strongpassword",
  "role": "user"
} 
```
Response:
```json 
{
  "email": "john.doe@example.com",
  "password": "strongpassword"
}
```
