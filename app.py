from flask import Flask, render_template, request, jsonify
import razorpay

app = Flask(__name__)

# Razorpay credentials
key_id = "rzp_test_TOPobtZmNgp0Bt"
key_secret = "kDjlWD0z6pZHWJ2XbQyaZO2e"
client = razorpay.Client(auth=(key_id, key_secret))


@app.route('/')
def home():
    return render_template("pay.html", key_id=key_id)


@app.route('/create-order', methods=['POST'])
def create_order():
    data = request.get_json()
    amount = int(data['amount']) * 100  
    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })
    return jsonify(payment)


@app.route('/thank-you')
def thank_you():
    return "<h2>✅ Payment Successful! Thank you.</h2>"


if __name__ == '__main__':
    app.run(debug=True)
