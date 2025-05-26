## 📢 SNS x Lambda: Event-Triggered Email Notification Project 

### ✉️ *Send Email Alerts in Real-Time Using AWS SNS and Lambda Functions*


### 📌 Project Description
This mini-project focused on building a lightweight event-driven architecture that sends automated email notifications using AWS Simple Notification Service (SNS) and AWS Lambda. 
The project demonstrates how to send alerts in response to events, showcasing a common pattern in serverless and decoupled system design.

![Alt Text](700x400_DIAGRAM_sns_lambda_lc.jpg)

---

## ✅ Project Goals

 - 📬  &nbsp;&nbsp;Send an email when an event occurs
 - 🟨  &nbsp;&nbsp;Use AWS Lambda to publish messages to SNS.
 - 🔔  &nbsp;&nbsp;Notify subscribers via email in real time.
 - 🔧  &nbsp;&nbsp;Confirm delivery by testing with a sample event.


---

## 🔧 What I Accomplished

- 🧵 &nbsp;&nbsp;Created an SNS Topic with Email Subscription.  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set up an SNS topic and subscribed using a verified email address, enabling the system to push email alerts.
- 🟨  &nbsp;&nbsp;Deployed a Lambda Function to Trigger Notifications.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wrote a basic AWS Lambda function that publishes a message to the SNS topic, simulating an event trigger.
- 🧪  &nbsp;&nbsp;Tested Lambda Execution and Verified Email Delivery.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manually triggered the Lambda function, which sent a notification through SNS. Received the email successfully,  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;confirming the setupworked.
- 📫  &nbsp;&nbsp;Handled Subscription Confirmation Flow.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Completed the email subscription confirmation process to activate delivery of messages to the subscriber’s inbox.

---

## 💡 Key Learnings & Outcomes

- ⚡  &nbsp;&nbsp;Understood the core mechanics of AWS SNS and its integration with Lambda.
- 📨  &nbsp;&nbsp;Learned how SNS topic subscriptions work and the importance of confirmation emails.
- 🔗  &nbsp;&nbsp;Strengthened familiarity with event-driven architectures and decoupled service communication.
- 🛠️  &nbsp;&nbsp;Practiced building serverless functions to support lightweight automation use cases.
