# Basic Tkinter App with SQLite

- [Basic Tkinter App with SQLite](#basic-tkinter-app-with-sqlite)
  - [Overview](#overview)
  - [Setup](#setup)
  - [Files](#files)
  - [Database](#database)

## Overview

A basic Tkinter application that uses an SQLite database to store and visualize data.

## Setup

~~1. Install dependencies: `pip install tkinter`~~

2. Run `python app.py` to start the application.

## Files

- `app.py`: Main application entry point.
- `config.ini`: Configuration file for database path.
- `gui/`: Contains GUI-related code.
- `utils/`: Contains database helper functions.
- `tests/`: Contains unit tests.

## Database

An SQLite database (`data.db`) is used to store data.

# Active Directory Management App Development Checklist

## 1. Project Setup

- [ ] **Create a New Project Repository**
  - Initialize a Git repository.
  - **Interacting with**: `/.gitignore`
- [ ] **Set Up Virtual Environment**
  - Create and activate a virtual environment.
  - **Interacting with**: `/env/`, `requirements.txt`
- [ ] **Define Project Structure**
  - Create folders: `src/`, `tests/`, `config/`, `data/`, `logs/`, `docs/`, `resources/`, `scripts/`.
  - **Interacting with**: Project root (creating these directories)
  - Add `__init__.py` to necessary directories.
  - **Interacting with**: `/src/`, `/tests/`, `/gui/`, `/utils/` (adding `__init__.py`)

## 2. Design & Requirements

- [ ] **Specify Functional Requirements**
  - Document features and functions.
  - **Interacting with**: `/docs/` (adding documentation)
- [ ] **Specify Non-functional Requirements**
  - Document security, performance, and scalability requirements.
  - **Interacting with**: `/docs/` (adding documentation)

## 3. Technology Selection

- [ ] **Choose Libraries and Frameworks**
  - Select and document libraries for LDAP, database, UI, testing, and logging.
  - **Interacting with**: `requirements.txt`, `/docs/` (document choices)

## 4. Implementation

### 4.1 Core Functionality

- [ ] **Active Directory Queries**

  - Implement function to query users in a directory.
  - **Interacting with**: `/src/` (implementing query functions), `/utils/`
  - Store queried data in a local cache/database.
  - **Interacting with**: `/data/`, `/utils/db_helper.py` (implementing caching functions)

- [ ] **User Management**
  - Implement password reset functionality.
  - **Interacting with**: `/src/`, `/utils/`
  - Implement user creation function.
  - **Interacting with**: `/src/`, `/utils/`
  - Implement "Member Of" management.
  - **Interacting with**: `/src/`, `/utils/`
  - Implement user disabling function.
  - **Interacting with**: `/src/`, `/utils/`

### 4.2 UI Development

- [ ] **Main Window**

  - Design the main window to display user data.
  - **Interacting with**: `/gui/windows/main_window.py`, `/gui/style/styles.py`
  - Add functionality to filter and search users.
  - **Interacting with**: `/gui/windows/main_window.py`, `/src/`
  - Implement buttons for user actions (e.g., reset password, disable user).
  - **Interacting with**: `/gui/windows/main_window.py`, `/src/`

- [ ] **"Member Of" Management Window**

  - Design a window to display and manage the "Member Of" attribute.
  - **Interacting with**: `/gui/windows/`, `/gui/style/`, `/src/`

- [ ] **Settings Window**
  - Implement a settings window to configure displayed user attributes.
  - **Interacting with**: `/gui/windows/`, `/gui/style/`

### 4.3 Caching & Optimization

- [ ] **Local Database Setup**

  - Set up SQLite or PostgreSQL database for caching.
  - **Interacting with**: `/data/data.db`, `/utils/db_helper.py`
  - Implement CRUD operations for caching user data.
  - **Interacting with**: `/utils/db_helper.py`

- [ ] **Optimization**
  - Minimize database queries by using cache effectively.
  - **Interacting with**: `/src/`, `/utils/`

## 5. Error Handling & Logging

- [ ] **Implement Error Handling**
  - Add try-except blocks to handle exceptions gracefully.
  - **Interacting with**: `/src/`, `/utils/`
  - Ensure meaningful error messages for users.
  - **Interacting with**: `/gui/windows/`, `/src/`
- [ ] **Set Up Logging**
  - Configure logging for debugging and tracking application behavior.
  - **Interacting with**: `/logs/`, `/src/`, `/utils/`

## 6. Testing

- [ ] **Write Unit Tests**

  - Write tests for each function.
  - **Interacting with**: `/tests/`
  - Ensure coverage for edge cases and exceptions.
  - **Interacting with**: `/tests/`

- [ ] **Write Integration Tests**

  - Test integration between the app and Active Directory.
  - **Interacting with**: `/tests/`, `/src/`
  - Test UI functionality.
  - **Interacting with**: `/tests/`, `/gui/`

- [ ] **Continuous Integration**
  - Set up CI/CD pipeline.
  - **Interacting with**: `/scripts/`, `/tests/`, CI/CD configuration files

## 7. Documentation

- [ ] **Create Documentation**
  - Add `README.md` with project overview, setup instructions, and usage.
  - **Interacting with**: `README.md`
  - Document API endpoints if applicable.
  - **Interacting with**: `/docs/`
  - Write user manual for the UI.
  - **Interacting with**: `/docs/`, `/gui/`

## 8. Deployment

- [ ] **Prepare for Deployment**
  - Package the application.
  - **Interacting with**: `/src/`, `/scripts/`
  - Create Dockerfile if containerizing.
  - **Interacting with**: `/scripts/`, `/Dockerfile`
  - Set up deployment pipeline.
  - **Interacting with**: CI/CD configuration files, `/scripts/`

## 9. Maintenance & Updates

- [ ] **Monitor Application**
  - Set up monitoring for errors and performance.
  - **Interacting with**: `/logs/`, `/scripts/`
- [ ] **Plan for Updates**
  - Regularly update dependencies.
  - **Interacting with**: `requirements.txt`, `/src/`, `/utils/`
  - Plan feature enhancements based on user feedback.
  - **Interacting with**: `/docs/`, `/src/`, `/gui/`

## 10. Final Review

- [ ] **Code Review**
  - Conduct code reviews to ensure quality and adherence to best practices.
  - **Interacting with**: `/src/`, `/tests/`, `/utils/`
- [ ] **Refactoring**
  - Refactor code for readability and performance.
  - **Interacting with**: `/src/`, `/utils/`, `/gui/`
- [ ] **Final Testing**

  - Perform thorough testing before release.
  - **Interacting with**: `/tests/`, `/src/`, `/gui/`

- [ ] **Release**
  - Tag version and release.
  - **Interacting with**: Git, version tags, `/docs/`
