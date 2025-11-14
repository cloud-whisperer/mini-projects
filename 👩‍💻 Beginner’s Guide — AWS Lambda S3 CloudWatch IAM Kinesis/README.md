# 🧭 AWS Event-Driven Mini Project: Orders Processing

🔁 *Process incoming orders with Lambda, store in DynamoDB, and notify high-value orders via SNS*  

---

## 📌 Project Description

This Proof of Concept (PoC) demonstrates a **basic serverless, event-driven workflow** in AWS:

- 💾 **Amazon DynamoDB** stores order records.  
- 🧠 **AWS Lambda** processes order events automatically.  
- 🔔 **Amazon SNS** notifies stakeholders for high-value orders.  
- 📬 **Amazon SQS** queues messages for downstream processing.  
- 📊 **CloudWatch Logs** captures Lambda execution and event details.  

Designed to highlight practical skills in **serverless compute**, **database operations**, **messaging**, and **monitoring**, ideal for **DVA-C02 exam domains**: Compute, Database, Messaging, Permissions, and Monitoring & Logging.  

---

## 🚀 Key Steps Simulated in This Project

- 💾 **Create a DynamoDB table** named `OrdersTable`.  
- 🧠 **Create a Lambda function** to process orders.  
- 🔐 **Attach an IAM role** granting Lambda `dynamodb:PutItem`, `sns:Publish`, `sqs:SendMessage`, and `kinesis:PutRecord` permissions.  
- 🔔 **Publish to SNS** automatically for high-value orders (`Amount > 300`).  
- 📬 **Send messages to SQS** for durable downstream processing.  
- 📊 **Stream records to Kinesis** for analytics.  
- 📤 **Send test events** to Lambda to simulate incoming orders.  
- 📈 **Inspect logs in CloudWatch** to validate order processing.  
- 🧹 **Clean up resources** to avoid charges.  

![Workflow Diagram](900x500_Step_Functions_DynamoDB_SNS_WATERMARK_lc.jpg)
![Workflow Diagram](900x500_Step_Functions_DynamoDB_SNS_WATERMARK_lc.jpg)

---

## 🧱 Core Infrastructure

| Component                | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 💾 DynamoDB Table         | Stores order records (`OrderId`, `Amount`, S3 key, timestamp)               |
| 🧠 AWS Lambda Function    | Processes order events and triggers SNS, SQS, Kinesis                        |
| 🔔 Amazon SNS Topic       | Notifies on high-value orders                                               |
| 📬 Amazon SQS Queue       | Receives SNS notifications for durable downstream processing                |
| 📊 Amazon Kinesis Stream  | Streams order records for analytics                                         |
| 🔐 IAM Role               | Provides least-privilege permissions for Lambda (DynamoDB + SNS + Kinesis) |
| 📊 CloudWatch Logs        | Monitors Lambda execution and captures event details                        |
| 🪣 Amazon S3 Bucket       | Source of object-created events triggering Lambda                            |

---

## 🧪 Testing & Validation

### ✅ Summary Table

| 🔢 Step | Goal                                | Tool                    |
|--------|-------------------------------------|------------------------|
| 1️⃣     | Create DynamoDB table               | AWS Console / DynamoDB |
| 2️⃣     | Create Lambda function              | AWS Console / Lambda   |
| 3️⃣     | Attach IAM role with permissions    | IAM Console            |
| 4️⃣     | Configure Lambda environment vars   | Lambda → Configuration |
| 5️⃣     | Send test event to Lambda           | Lambda → Test Event    |
| 6️⃣     | Verify DynamoDB record creation     | DynamoDB Console       |
| 7️⃣     | Verify SNS notification (Amount > 300) | Email / SNS Console |
| 8️⃣     | Inspect Lambda execution logs       | CloudWatch Logs        |
| 9️⃣     | Verify SQS message delivery         | SQS Console            |
| 🔟      | Verify Kinesis stream record        | Kinesis Console        |

---

### 🧠 Event Behavior Confirmations

| 🔍 What to Confirm                       | 📌 Status | 🧾 Evidence Provided                          |
|----------------------------------------|-----------|---------------------------------------------|
| Lambda triggered by S3 event            | ✅        | CloudWatch Logs shows event details          |
| IAM permissions allow DynamoDB write    | ✅        | No `AccessDenied` errors                     |
| IAM permissions allow SNS publish       | ✅        | SNS email received for high-value order      |
| IAM permissions allow SQS send          | ✅        | Message visible in HighValueQueue           |
| IAM permissions allow Kinesis put       | ✅        | Kinesis IncomingRecords metric increments    |
| Order JSON saved in DynamoDB            | ✅        | DynamoDB console shows `OrderId` & `Amount` |
| CloudWatch logs show structured output  | ✅        | Logs include JSON request + Lambda response |

---

## 🛡️ Permissions & Security (IAM Role)

### 🔐 What Was Implemented

- ✅ **Role Name**: `ProcessOrderFunction-role`  
- 👤 **Assigned to Lambda**  
### 🧾 Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "sns:Publish",
        "sqs:SendMessage",
        "kinesis:PutRecord",
        "kinesis:PutRecords",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:dynamodb:us-east-1:<account-id>:table/OrdersTable",
        "arn:aws:sns:us-east-1:<account-id>:HighValueOrderTopic",
        "arn:aws:sqs:us-east-1:<account-id>:HighValueQueue",
        "arn:aws:kinesis:us-east-1:<account-id>:stream/OrdersStream",
        "arn:aws:s3:::lambda-kinesis-demo-<suffix>/*"
      ]
    }
  ]
}
```


### 🎯 Learning Outcomes

| 🔢 Step | Outcome                                                                 | Tool / Evidence                       |
|--------|-------------------------------------------------------------------------|--------------------------------------|
| 1️⃣     |🔁 Build a serverless event-driven workflow with Lambda → DynamoDB → SNS → SQS → Kinesis | AWS Console / Lambda / DynamoDB / SNS / SQS / Kinesis |
| 2️⃣     |💾 Apply DynamoDB CRUD operations for real-time event processing          | DynamoDB Console                     |
| 3️⃣     |🔔 Implement SNS notifications for high-value orders                      | SNS Console / Email Notifications    |
| 4️⃣     |📬 Send messages to SQS for downstream decoupled processing               | SQS Console                          |
| 5️⃣     |📊 Stream order records to Kinesis for analytics                           | Kinesis Console / CloudWatch Metrics |
| 6️⃣     |🧠 Configure IAM roles with least privilege for Lambda functions          | IAM Console / Lambda Execution Role  |
| 7️⃣     |📈 Monitor execution and event processing using CloudWatch Logs           | CloudWatch Logs                       |
| 8️⃣     |🧹 Practice clean-up best practices to minimize cost                       | AWS Console / Resource Deletion      |
| 9️⃣     |🚀 Reinforce core DVA-C02 domains: Compute, Database, Messaging, Permissions, Monitoring | All relevant AWS services            |



