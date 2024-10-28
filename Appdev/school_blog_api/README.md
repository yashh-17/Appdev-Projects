
# School Blog API

The **School Blog API** is a simple web application built using FastAPI and MongoDB (motor) to create and manage a blog for a school community. This API allows users to create, read, update, and delete blog posts, while also providing data validation with Pydantic.

## Features

- **CRUD operations** for blog posts (Create, Read, Update, Delete).
- **Data validation** using Pydantic models.
- **MongoDB integration** using `motor` (an async MongoDB driver).
- **Static file serving** for HTML and CSS files.
- **Asynchronous processing** for better performance.

## Prerequisites

Before setting up the project, make sure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community) (Make sure MongoDB is running locally or accessible remotely)
- [Git](https://git-scm.com/)
- [FastAPI](https://fastapi.tiangolo.com/)

## Project Structure

```
school_blog_api/
├── app/
│   ├── main.py               # The main FastAPI application
│   ├── models/               # Pydantic models for data validation
│   ├── routes/               # API route definitions
│   └── schemas/              # Database schema definitions
├── static/
│   ├── index.html            # Sample HTML file for the blog
│   ├── styles.css            # CSS file for styling
└── README.md                 # Project documentation
```

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/school_blog_api.git
   cd school_blog_api
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, manually install the dependencies:

   ```bash
   pip install fastapi motor uvicorn
   ```

4. **Run MongoDB locally**

   Make sure MongoDB is running. If you're using MongoDB Compass, ensure it is connected to the default MongoDB URL: `mongodb://localhost:27017`.

5. **Start the FastAPI server**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**

   Visit `http://127.0.0.1:8000` in your web browser to see the welcome message. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- **GET /** - Welcome message.
- **POST /posts/** - Create a new blog post.
- **GET /posts/** - Retrieve all blog posts.
- **PUT /posts/{id}** - Update a blog post.
- **DELETE /posts/{id}** - Delete a blog post.

## Example HTML and CSS

The project includes basic HTML and CSS files located in the `static/` directory to provide a simple front-end interface for the blog.

- `index.html` - The main HTML file with a sample blog post structure.
- `styles.css` - Basic styling for the blog page.

## Running Tests

You can use tools like `pytest` for testing FastAPI applications. Make sure to install `pytest` if you plan to write tests.

```bash
pip install pytest
pytest
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License.
