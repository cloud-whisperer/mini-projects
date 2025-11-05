# 📦 Serverless Orders Pipeline (Lambda → DynamoDB → SNS → SQS)

🔁 *Process Orders Securely in a Serverless Event-Driven Architecture on AWS*

---

## 📌 Project Description

This mini-project demonstrates a **fully serverless workflow** that ingests order events, stores them, and triggers notifications for high-value orders. It simulates a real-world e-commerce processing pipeline using:

- **AWS Lambda** – event-driven compute  
- **DynamoDB** – persistent storage  
- **SNS** – notifications  
- **SQS** – queued message delivery  

It is ideal for learning **serverless best practices**, **event-driven design**, and **IAM security** in AWS.

---

## 🚀 Key Steps Simulated in This Project

- 💾 &nbsp;&nbsp;**Create DynamoDB Table** for order storage.  
- 🔔 &nbsp;&nbsp;**Create SNS Topic** for high-value order notifications.  
- 📬 &nbsp;&nbsp;**Create SQS Queue** to receive SNS messages.  
- 🔗 &nbsp;&nbsp;**Subscribe SQS to SNS** to enable message flow.  
- 🔐 &nbsp;&nbsp;**Create IAM Role for Lambda** with least privilege access.  
- 🪄 &nbsp;&nbsp;**Deploy Lambda Function** to process incoming orders.  
- 🧪 &nbsp;&nbsp;**Test Lambda Execution** with a sample high-value order event.  
- 🔍 &nbsp;&nbsp;**Verify end-to-end flow**: DynamoDB writes, SNS publishes, SQS receives messages.  

---

## ✅ Project Goals

- 💾 &nbsp;&nbsp;Store incoming order data in DynamoDB.  
- 🔔 &nbsp;&nbsp;Trigger notifications for orders above a threshold.  
- 📬 &nbsp;&nbsp;Deliver messages to a downstream queue for processing.  
- 🔐 &nbsp;&nbsp;Use least privilege IAM policies for Lambda function.  
- 🧭 &nbsp;&nbsp;Monitor and validate workflow using CloudWatch Logs.  

---

## 🔧 What I Accomplished

- 🧑‍💻 &nbsp;&nbsp;**Created a DynamoDB Table (`OrdersTable`)**  
      Partition key: `OrderId` (String) | Billing mode: On-demand.

- 🔔 &nbsp;&nbsp;**Created SNS Topic (`HighValueOrderTopic`)**  
      Configured to notify when orders exceed $100.

- 📬 &nbsp;&nbsp;**Created SQS Queue (`HighValueQueue`)**  
      Subscribed to SNS Topic for message delivery.

- 🔗 &nbsp;&nbsp;**Connected SNS → SQS**  
      Confirmed subscription to automatically deliver messages.

- 🔐 &nbsp;&nbsp;**Created IAM Role (`ProcessOrderFunction-role`)**  
      Inline policy allowed: `dynamodb:PutItem` & `sns:Publish` on specific resources.

- 🪄 &nbsp;&nbsp;**Deployed Lambda Function (`ProcessOrderFunction`)**  
      Processes incoming orders, writes to DynamoDB, and publishes high-value notifications to SNS.

- 🧪 &nbsp;&nbsp;**Tested with a sample event**  
      ```json
      { "OrderId": "ORD-1001", "Amount": 250 }
      ```

- 🔍 &nbsp;&nbsp;**Verified end-to-end flow**  
      DynamoDB shows order, SNS logs one message published, SQS shows one message received.

---

## 💡 Key Learnings & Outcomes

- ☁️ &nbsp;&nbsp;Implemented a **serverless event-driven workflow** on AWS.  
- 💾 &nbsp;&nbsp;Practiced **DynamoDB CRUD operations** and understanding partition keys.  
- 🔔 &nbsp;&nbsp;Learned **SNS publish/subscribe** patterns for notifications.  
- 📬 &nbsp;&nbsp;Configured **SQS queues** to receive and buffer messages.  
- 🔐 &nbsp;&nbsp;Applied **IAM least privilege** policies for secure Lambda execution.  
- 🧭 &nbsp;&nbsp;Monitored and debugged using **CloudWatch Logs**.  
- 🧹 &nbsp;&nbsp;Practiced **resource clean-up** to avoid unnecessary AWS charges.

---

![AWS Serverless Pipeline](800x500_serverless_pipeline_lc_WATERMARKED_lc.jpg)

