<h1>S3 cross account access mini-projekt</h1>
<br> This PoC demonstrates secure cross-account access between two AWS accounts using an S3 bucket policy. 
<br> Account A hosts a bucket and grants explicit access to a user in Account B, permitting user B
<br>to download files to an S3 bucket in Account B. An IAM role was created in Account A to allow
<br>access to the files in Account A's S3 bucket. 
<br>
<br><h2>Example use case:</h2>
<br>A team from Account B requires read-only access to compliance logs stored in Account A's S3 bucket for 
<br>auditing purposes, using the principle of least privilege (PLP) to meet the business need for this use case.
<br>

![Alt Text](S3_cross_account_access_lc_WATERMARKED_lc.jpg)
