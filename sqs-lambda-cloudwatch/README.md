### 📦 SQS x Lambda: Bi-Directional Message Exchange Project

🔁 Send and Receive Messages Seamlessly Using AWS SQS and Lambda

![Alt Text](700x400_sqs_lambda_cloudwatch_lc.jpg)

---

### 📌 Project Description

This mini-project demonstrates a foundational event-driven workflow by enabling an AWS Lambda function to both **send messages to** and **receive messages from** an Amazon Simple Queue Service (SQS) queue. It showcases a **bi-directional communication pattern**, commonly used in decoupled microservice architectures.

The Lambda function is triggered manually (or by another service) and performs the following actions:

1. ✅ **Sends a message** to the SQS queue.
2. 📥 **Receives messages** from the queue.
3. 🗑️ **Deletes the messages** after processing.
4. 🧾 Logs key events such as sending, receiving, and deleting for full traceability.

This project is a great introduction to designing reliable, loosely coupled, and asynchronous systems using native AWS services.

---

Let me know if you'd like to extend the description to include CloudWatch Logs, IAM permissions, or even SNS integrations for alerting 👀

