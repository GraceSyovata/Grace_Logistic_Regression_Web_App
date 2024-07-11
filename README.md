### Deploying a Logistic Regression ML Model as a Web Application on Docker

**Last Updated**: 20 Feb, 2024

### Overview
This project demonstrates how to deploy a Logistic Regression machine learning model as a web application using Docker. Docker ensures that the application can run consistently across different environments by using containerization.

### Key Components
1. **Logistic Regression**: A supervised learning algorithm used for binary classification problems, modeling the probability of a binary outcome.
2. **Docker**: A platform that uses OS-level virtualization to deliver software in containers, which bundle the software with its dependencies and configuration files.

### Steps to Deploy
1. **Train the Logistic Regression Model**:
   - **Dataset**: Use an appropriate dataset for binary classification (e.g., Titanic dataset).
   - **Features**: Select relevant features from the dataset.
   - **Model Training**: Using `scikit-learn`, the model is trained and saved with `pickle`.

2. **Build the Flask Web Application**:
   - **Flask**: Used to create a simple web interface.
   - **Routes**: A form to input data and a route to handle predictions.

3. **Dockerize the Flask App**:
   - **Dockerfile**: Specifies the environment, dependencies, and commands to run the app.
   - **Requirements.txt**: Lists required Python libraries.

4. **Build and Run Docker Image**:
   - **Build Image**: `docker build -t logistic-regression-web-app .`
   - **Run Container**: `docker run -p 5000:5000 logistic-regression-web-app`

5. **Test the Application**:
   - Access the application via `http://localhost:5000`, input data, and receive predictions.

### Prerequisites
- **Python 3.6+**
- **PIP**
- **Docker**
- **Python Libraries**: Flask, NumPy, Pandas, scikit-learn, Pickle

### Project Structure
```
/your-flask-app
    /templates
        index.html
    app.py
    requirements.txt
    Dockerfile
    ...
```

### Example Workflow

**Training the Model**:
1. **Dataset Loading**: Load the binary classification dataset.
2. **Feature Selection**: Choose features that are relevant to the prediction task.
3. **Data Splitting**: Split the dataset into training and testing sets.
4. **Model Training**: Train the logistic regression model using `scikit-learn`.
5. **Model Saving**: Save the trained model to disk using `pickle`.

**Flask Application**:
1. **Home Route**: Renders the HTML form for user input.
2. **Predict Route**: Accepts POST requests, uses the model to predict the outcome based on user inputs, and displays the prediction.

**Dockerization**:
1. **Dockerfile Creation**: Define the environment, dependencies, and execution command for the Flask app.
2. **Requirements Installation**: List all required Python libraries in `requirements.txt`.

**Build and Run**:
1. **Docker Image**: Build the Docker image from the Dockerfile.
2. **Docker Container**: Run the Docker container, mapping the necessary ports to access the web application.

### Conclusion
Deploying a Logistic Regression model as a web application involves training the model, creating a Flask application to use the model, dockerizing the Flask app for easy deployment, and testing to ensure everything works as expected. This process demonstrates how machine learning models can be made accessible and useful in real-world applications, providing valuable insights or predictions based on user input.
