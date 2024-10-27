from flask import Flask, render_template, request, redirect, url_for, send_file
import json
import os
import pandas as pd

app = Flask(__name__)

# Function to load data from the JSON file
def load_employees():
    if os.path.exists("employees.json"):
        with open("employees.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Function to save data to the JSON file
def save_employees(employees):
    with open("employees.json", "w", encoding="utf-8") as file:
        json.dump(employees, file, ensure_ascii=False, indent=4)

# Route to export data to Excel
@app.route('/export_excel')
def export_to_excel():
    # Load employees
    employees = load_employees()
    
    # Convert data to DataFrame
    df = pd.DataFrame(employees)
    
    # Save to Excel
    excel_path = "employees.xlsx"
    df.to_excel(excel_path, index=False, engine="openpyxl")
    
    # Return the Excel file for download
    return send_file(excel_path, as_attachment=True)

# Main page to display the list of employees and the form
@app.route('/')
def index():
    employees = load_employees()
    return render_template('index.html', employees=employees)

# Route to add a new employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    # Get form data
    first_name = request.form['name']
    last_name = request.form["surname"]
    age = request.form['age']
    city = request.form['city']
    
    # Load existing employees
    employees = load_employees()
    
    # Add new employee to the list
    new_employee = {"first_name": first_name, "last_name": last_name, "age": int(age), "city": city}
    employees.append(new_employee)
    
    # Save the updated list of employees to the JSON file
    save_employees(employees)
    
    return redirect(url_for('index'))

# Route to delete an employee by index
@app.route('/delete_employee/<int:index>', methods=['POST'])
def delete_employee(index):
    employees = load_employees()
    
    # Check if index exists in the employee list
    if 0 <= index < len(employees):
        # Delete the employee at the specified index
        employees.pop(index)
        
        # Save the updated list of employees to the JSON file
        save_employees(employees)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
