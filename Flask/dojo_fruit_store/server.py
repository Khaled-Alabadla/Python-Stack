from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

# Route for the home page
@app.route('/')         
def index():
    return render_template("index.html")

# Route for checkout, handles POST requests from the order form
@app.route('/checkout', methods=['POST'])         
def checkout():
    # Print the form data for debugging
    print(request.form)
    
    # Retrieve form data
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    student_id = request.form.get('student_id', '')
    
    # Convert quantities to integers
    strawberry = int(request.form.get('strawberry', 0))
    raspberry = int(request.form.get('raspberry', 0))
    apple = int(request.form.get('apple', 0))
    blackberry = int(request.form.get('blackberry', 0))
    
    # Calculate total fruits ordered
    total_fruits = strawberry + raspberry + apple + blackberry
    
    # Combine first and last name
    customer_name = f"{first_name} {last_name}".strip()
    
    # Print charging message
    print(f"Charging {customer_name} for {total_fruits} fruits.")
    
    # Get current date and time
    now = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    
    # Render checkout template with order details
    return render_template("checkout.html", 
                           first_name=first_name,
                           last_name=last_name,
                           student_id=student_id,
                           strawberry=strawberry,
                           raspberry=raspberry,
                           apple=apple,
                           blackberry=blackberry,
                           total_fruits=total_fruits,
                           customer_name=customer_name,
                           order_time=now)

# Route for displaying fruits
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

# Run the app in debug mode if this file is executed directly
if __name__=="__main__":   
    app.run(debug=True)    