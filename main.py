from app import app

# For local development
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
# For Vercel serverless deployment
# The import app is necessary for Vercel to detect the Flask app as the lambda handler
