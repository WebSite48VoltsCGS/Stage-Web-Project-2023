# Web Development Internship 2023

# Syntax
-> : One-to-many field / URL
<-> : One-to-one field

# Urls
- Home
- News
- Studios
- Bar
- Booking
    - Book a studio for a rehearsal
    - Book a concert date
- Contact
- Buttons
    - -> Sign In / Sign Up
    - Dropdown
        - -> Profile
        - -> My groups
        - -> My bookings
        - Log out

- Profile
    - Personal information
        - Username
        - E-mail
        - Last name
        - First name
        - Password
    - Buttons
        - -> Edit profile
        - -> Log out

- Edit profile
    - Username
    - Password
    - E-mail
    - Last name
    - First name
    - Phone
    - Confirm password (Required)
    - Buttons
        - Undo changes -> Edit profile (Empty form)
        - Confirm my changes -> Profile

- My groups
    - Group tables
        - Approval
        - Group name
        - Edit group
        - Delete group
    - Add a group

- My bookings
    - Booking tables and history
        - Type (Rehearsal / Concert)
        - Date
        - Studio
        - Duration
        - Payé (Oui / Non)
    - Add a booking
    - Cancel a reservation

# Models
- Auth user
    - Username
    - Password
    - E-mail
    - Last name
    - First name

- User
    - User <-> Auth User (One to one)
    - Phone
    - History
    - User <-> Groups (One to many)

- Group
    - Group name
    - E-mail
    - Phone
    - Members
    - Musical style
    - Facebook
    - Instagram
    - Twitter
    - Biography
    - Approval

## Readme

Main: /README.md
- https://github.com/WebSite48VoltsCGS/Web-Development-Internship-2023/blob/main/README.md

Web architecture: /README_ARCHITECTURE.md
- https://github.com/WebSite48VoltsCGS/Web-Development-Internship-2023/blob/main/README_ARCHITECTURE.md

OpenClassrooms: /OpenClassrooms/README_OpenClassrooms.md
- https://github.com/WebSite48VoltsCGS/Web-Development-Internship-2023/blob/main/OpenClassrooms/README_OpenClassrooms.md
