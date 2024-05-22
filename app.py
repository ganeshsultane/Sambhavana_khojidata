from flask import Flask, render_template, request, send_file, redirect, url_for
import csv
import os
from datetime import datetime
from io import StringIO

app = Flask(__name__)

# In-memory storage for data
data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        sr_no = request.form.get('sr_no')
        khoji_id = request.form.get('khoji_id')
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        last_name = request.form.get('last_name')
        mobile = request.form.get('mobile')
        gender = request.form.get('gender')
        address = request.form.get('address')
        tejsthan = request.form.get('tejsthan')
        zone = request.form.get('zone')
        pincode = request.form.get('pincode')
        current_shivir = request.form.get('current_shivir')
        updated_on = datetime.now().strftime('%Y-%m-%d')

        # Append data to in-memory list
        data.append([sr_no, khoji_id, first_name, middle_name, last_name, mobile, gender, address, tejsthan, zone, pincode, current_shivir, updated_on])
        
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/download')
def download():
    # Create a CSV file in memory
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Sr No.', 'Khoji ID', 'First Name', 'Middle Name', 'Last Name', 'Mobile', 'Gender', 'Address', 'Tejsthan', 'Zone', 'Pincode', 'Current Shivir', 'Updated on'])
    cw.writerows(data)
    output = si.getvalue()
    si.close()

    return send_file(StringIO(output), 
                     mimetype='text/csv', 
                     as_attachment=True, 
                     attachment_filename='data.csv')

if __name__ == '__main__':
    app.run(debug=True)
