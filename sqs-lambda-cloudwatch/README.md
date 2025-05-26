### 📦 SQS x Lambda: Bi-Directional Message Exchange Project

---

🔁 Send and Receive Messages Seamlessly Using AWS SQS and Lambda


### 📌 Project Description

This mini-project demonstrates a foundational event-driven workflow by enabling an AWS Lambda function to both **send messages to** and **receive messages from** an Amazon Simple Queue Service (SQS) queue. It showcases a **bi-directional communication pattern**, commonly used in decoupled microservice architectures.

The Lambda function is triggered manually (or by another service) and performs the following actions:

1. ✅ **Sends a message** to the SQS queue.
2. 📥 **Receives messages** from the queue.
3. 🗑️ **Deletes the messages** after processing.
4. 🧾 Logs key events such as sending, receiving, and deleting for full traceability.

This project is a great introduction to designing reliable, loosely coupled, and asynchronous systems using native AWS services.

![Alt Text](700x400_sqs_lambda_cloudwatch_lc.jpg)

---

##  ✅ Project Goals

 - 📨 &nbsp;&nbsp;Send a message to an SQS queue from a Lambda function
-  📥 &nbsp;&nbsp;Retrieve and process messages from the same SQS queue
-  🟨 &nbsp;&nbsp;Use AWS Lambda as both producer and consumer in the messaging pipeline
-  🧼 &nbsp;&nbsp;Automatically delete messages from the queue after processing
-  🪵 &nbsp;&nbsp;Log all send/receive/delete actions in CloudWatch for observability
-  🔧 &nbsp;&nbsp;What I Accomplished

📦 Created an Amazon SQS Queue
    Set up a standard SQS queue with appropriate access policies to allow message sending and receiving.

🧑‍💻 Wrote and Deployed a Dual-Purpose Lambda Function
    Developed a Python-based Lambda function that sends a message to the queue, receives a message, and deletes it—executing the full SQS workflow.

🔐 Configured Environment Variables and IAM Permissions
    Used the SQS_QUEUE_URL environment variable for queue targeting and attached precise IAM policies to grant SendMessage, ReceiveMessage, and DeleteMessage permissions.

🧪 Manually Triggered the Lambda Function
    Used the Lambda Console's "Test" feature to simulate an event, verify end-to-end message delivery, and observe logs in CloudWatch.

📄 Logged Message Lifecycle Events
    Printed out sent message IDs, received message bodies, and confirmation of deletion steps for full operational visibility.
💡 Key Learnings & Outcomes

🔁 Learned how Lambda can act as both a producer and consumer in an SQS-backed workflow
🔑 Gained hands-on experience with IAM policies for SQS operations
🪝 Improved understanding of decoupled, event-driven architectures and async communication
🛠️ Practiced structuring Python code for message lifecycle management (send → receive → delete)
📊 Strengthened ability to troubleshoot using CloudWatch Logs and confirm functional behavior step-by-step



