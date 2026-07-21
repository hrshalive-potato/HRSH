# Project Resources & Official Documentation

This document contains links to the official documentation and learning resources for all the technologies, libraries, and tools used in your Django blog project.

## Core Technologies

*   **Python:** The programming language used for the backend.
    *   [Official Documentation](https://docs.python.org/3/)
    *   [Real Python (Tutorials & Articles)](https://realpython.com/)
*   **Django:** The high-level Python web framework used to build the core of the application.
    *   [Official Documentation](https://docs.djangoproject.com/)
    *   [Django Girls Tutorial](https://tutorial.djangogirls.org/) - Fantastic for beginners.
    *   [Mozilla Developer Network (MDN) Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - Highly structured and comprehensive.

## Frontend Technologies

*   **HTML:** For structuring the web pages (used heavily in your `templates/` folder).
    *   [MDN HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
*   **CSS:** For styling the web pages (like your `style.css` file).
    *   [MDN CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
*   **JavaScript:** For adding dynamic interactivity to the browser.
    *   [MDN JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Third-Party Django Packages

These are the additional libraries installed via `pip` to add specific features to your project.

*   **django-allauth:** Used for user authentication, registration, account management, and social login integrations (like Google OAuth).
    *   [Official Documentation](https://docs.allauth.org/en/latest/)
*   **django-ckeditor:** Provides the rich text WYSIWYG (What You See Is What You Get) editor for formatting blog posts and uploading images.
    *   [Official Documentation / GitHub](https://django-ckeditor.readthedocs.io/)
*   **WhiteNoise:** Used to serve static files (CSS, JS, images) efficiently, especially critical when preparing for production deployment.
    *   [Official Documentation](https://whitenoise.readthedocs.io/)
*   **python-decouple:** Used for managing environment variables (like your `SECRET_KEY`, `DEBUG` mode, or database credentials) safely in a `.env` file so secrets aren't exposed in the code.
    *   [Official Documentation / GitHub](https://github.com/HBNetwork/python-decouple)
*   **Pillow:** The standard Python Imaging Library. It is required by Django and CKEditor to handle image uploads and image processing.
    *   [Official Documentation](https://pillow.readthedocs.io/)

## Database

*   **SQLite:** The default, lightweight, file-based database used for local development (`db.sqlite3`).
    *   [Official Documentation](https://www.sqlite.org/docs.html)
    *   [Django Database Setup Docs](https://docs.djangoproject.com/en/stable/ref/databases/)

## Additional Recommended Learning Resources

*   **Corey Schafer's Django Tutorials (YouTube):** An excellent, highly-praised, comprehensive video series on building a Django blog from scratch.
    *   [Link to Django Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
*   **Django for Beginners (Book):** By William S. Vincent. A highly recommended, up-to-date book for getting started with Django.
    *   [Website](https://djangoforbeginners.com/)
*   **Stack Overflow:** The best place for troubleshooting specific errors. Tag your searches with `[django]` or `[python]`.
