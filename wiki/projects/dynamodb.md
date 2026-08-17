---
title: DynamoDB
type: project
status: active
confidence: high
cluster: data
domain: [data]
sources: []
updated: 2025-02-27
tags: [AWS, Database]
---

In 2021, there was a 66-hour Amazon Prime Day shopping event.

The event generated some staggering stats:

- Trillions of API calls were made to the database by Amazon applications.
- The peak load to the database reached 89 million requests per second.
- The database provided single-digit millisecond performance while maintaining high availability.

All of this was made possible by DynamoDB.

Amazon’s DynamoDB is a NoSQL cloud database service that promises consistent performance at any scale.

Besides Amazon’s in-house applications, hundreds of thousands of external customers rely on DynamoDB for high performance, availability, durability, and a fully managed serverless experience. Also, many AWS services such as AWS Lambda, AWS Lake Formation, and Amazon SageMaker are built on top of DynamoDB.

In this post, we will look at the evolution of DynamoDB, its operational requirements, and the techniques utilized by the engineers to turn those requirements into reality.

## **History of DynamoDB**

In the early years, Amazon realized that letting applications access traditional enterprise databases was an invitation to multiple scalability challenges such as managing connections, dealing with concurrent workloads, and handling schema updates.

Also, high availability was a critical property for always-online systems. Any downtime negatively impacted the company’s revenue.

There was a pressing need for a highly scalable, available, and durable key-value database for fast-changing data such as a shopping cart.

Dynamo was a response to this need.

However, there was one drawback of Dynamo. It was a single-tenant system and teams were responsible for managing their own Dynamo installations. In other words, every team that used Dynamo had to become experts on various parts of the database service, creating a barrier to adoption.

At about the same time, Amazon launched SimpleDB which reduced operational burden for the teams by providing a managed and elastic experience. The engineers within Amazon’s development team preferred using SimpleDB even though Dynamo might be more suitable for their use case.

But SimpleDB also had some limitations such as:

- The tables had a small storage capacity of 10 GB.
- Request throughput was low.
- Unpredictable read and write latencies because all table attributes were indexed.

Also, the operational burden wasn’t eliminated. Developers still had to take care of dividing data between multiple tables to meet their application’s storage and throughput requirements.

Therefore, the engineers concluded that a better solution would be to combine the best parts of Dynamo (scalability and predictable high performance) with the best parts of SimpleDB (ease of administration, consistency, and a table-based data model).

This led to the launch of DynamoDB as a public AWS service in 2012. It was a culmination of everything they had learned from building large-scale, non-relational databases for Amazon.

Over the years, DynamoDB has added several features based on customer demand.

The below timeline illustrates this constant progress.

[](https://ci3.googleusercontent.com/meips/ADKq_NbI1DKlpAoRmKQ4riAeNYUlFPRQv-SYZkoOJUixyStYin70P6EoAl-ZmEB4A_OfFjE5P01ZQtPcMD7G__-sDHtRAdKVj1r5mhnybb3fWXF7Keb86PLbboG0dNq1rjJpEnu1d5jLivKekS-mtJZdBuWBcIL0rHjTVW_mTfgR5R8UjcV2bMk92l-dDdTSUJQMnSOVlDVY4I0v399RQKTuCxrlcEe-tDaMa4dfmY0VPXyHNGgFJzTkB5eDIaYu3szICOTVl3254pbM5UO41ODQiYZ9dtWPvNe9Au_GUw8POFadJvOEUHSh0MKxtQ=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F778c5543-0e34-4bf0-89ef-767a0b27c545_1600x848.png)

## **Operational Requirements of DynamoDB**

DynamoDB has evolved over the years, much of it in response to Amazon’s experiences building highly scalable and reliable cloud computing services. A key challenge has been adding features without impacting the key operational requirements.

The below diagram shows the six fundamental operational requirements fulfilled by DynamoDB.

[](https://ci3.googleusercontent.com/meips/ADKq_Napd0MmNhqf7_1z-XmPCraW9ol9YrBwplfp2cRaiYuPcftDJIiE3KGLUkq6JYd1GP2vwP5Vd0Ks2lz5kQMJm0eOehqMgtR-kfm9aXyNypeXXbilvaEnq1sP-AbFGr57qH2wssmJs4nThC3FqHqcwRn9PlflrMfomJYpXnjxcSfNuhRnqnUz79e8K8Ep71N99f7BR4s3tXq52H2zp-61eSpqju56WS_jKQHn-ZRZT2TJY5IXjxKaSCRUpTEVb_afkdlVMUz1bonYNdIL0TiUdife3eXUpGXmBFl9zQdh0zbfwjyNTgKAJTiddRg=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1392,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9aaee84e-f1a0-458f-9f70-64762b733d31_1345x1600.png)

Let’s look at each of them in a little more detail.

### **Fully Managed Cloud Service**

A fundamental goal of DynamoDB is to free developers from the burden of running their database system. This includes things like patching software, configuring a distributed database cluster, and taking care of hardware needs.

The applications can just talk to the DynamoDB API for creating tables. They can read and write data without worrying about where those tables are physically stored or how they’re being managed.

DynamoDB handles everything for the developer right from resource provisioning to software upgrades, data encryption, taking backups, and even failure recovery.

### **Multi-Tenant Architecture**

DynamoDB also aims to create cost savings for the customers.

One way to achieve this is using a multi-tenant architecture where data from different customers is stored on the same physical machines. This ensures better resource utilization and lets Amazon pass on the savings to the customers.

However, you still need to provide workload isolation in a multi-tenant system.

DynamoDB takes care of it via resource reservations, tight provisioning, and monitoring usage for every customer.

### **Boundless Scale for Tables**

Unlike SimpleDB, there are no predefined limits for how much data can be stored in a DynamoDB table.

DynamoDB is designed to scale the resources dedicated to a table from several servers to many thousands as needed. A table can grow elastically to meet the demands of the customer without any manual intervention.

### **Predictable Performance**

DynamoDB guarantees consistent performance even when the tables grow from a few megabytes to hundreds of terabytes.

For example, if your application is running in the same AWS region as its data, you can expect to see average latency in the low single-digit millisecond range.

DynamoDB handles any level of demand through horizontal scaling by automatically partitioning and repartitioning data as and when needed.

### **Highly Available**

DynamoDB supports high availability by replicating data across multiple data centers or availability zones.

Customers can also create global tables that are geo-replicated across selected regions and provide low latency all across the globe. DynamoDB offers an availability SLA of 99.99% for regular tables and 99.999% for global tables.

### **Flexible Use Cases**

Lastly, DynamoDB has a strong focus on flexibility and doesn’t force developers to follow a particular data model.

There’s no fixed schema and each data item can contain any number of attributes. Tables use a key-value or document data model where developers can opt for strong or eventual consistency while reading items from the table.

---

## **Latest articles**

If you’re not a paid subscriber, here’s what you missed this month.

[](https://ci3.googleusercontent.com/meips/ADKq_NbvA7zFmsanKSWdbuc5RI9W43W7hKDBjLd71ni7obK_rhZhHs_21MHynfFsCtc_ODr_TmxGZf5eiZhS3FXJRrNrK13clK6tKrXtLTkziQHaMH7Zn-kXjvvwDrGdyH3E0_NPSYfoepc7bK3c6VVFh5KQVY4bw7qB2Qnm2RL1Z4gQA8D-4bgDX34qVS-SWKCUHbtaq2Dcv9GLbthOGFOT8wCNNeKWjCgGjsS6gFGztLi_0BHizpXYO1iLr79kPOisbmLkTe9zGqFqJE8SqOt9ddr6PuERtIB6dlt9XkAdcb1oFtUlkLFy-ZGEVA=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_2912,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9f07074-c898-408e-b9f9-7ec2fb547247_1600x813.png)

1. [The Top 3 Resume Mistakes Costing You the Job](https://substack.com/redirect/d5524a64-77a2-416d-b953-ed3e18d42f9a?j=eyJ1IjoiMThlcGE3In0.x_DzjRt_5gqhD2Uq0iXKHyPR4G7eSDHwK8iCQGZH4rk)
2. [How Video Recommendations Work - Part 1](https://substack.com/redirect/4509de5a-b1cb-477b-9ab3-f60f89bb19e9?j=eyJ1IjoiMThlcGE3In0.x_DzjRt_5gqhD2Uq0iXKHyPR4G7eSDHwK8iCQGZH4rk)
3. [How to Design a Good API?](https://substack.com/redirect/fa5bffcc-29c2-449f-967e-1d2678192201?j=eyJ1IjoiMThlcGE3In0.x_DzjRt_5gqhD2Uq0iXKHyPR4G7eSDHwK8iCQGZH4rk)
4. [How do We Design for High Availability?](https://substack.com/redirect/fa4eac16-07a2-421e-ba5e-ad1d3229fea4?j=eyJ1IjoiMThlcGE3In0.x_DzjRt_5gqhD2Uq0iXKHyPR4G7eSDHwK8iCQGZH4rk)
5. [Good Code vs. Bad Code](https://substack.com/redirect/25037aee-9aeb-456a-81e7-7a0dfb799a41?j=eyJ1IjoiMThlcGE3In0.x_DzjRt_5gqhD2Uq0iXKHyPR4G7eSDHwK8iCQGZH4rk)

To receive all the full articles and support ByteByteGo, consider subscribing:

[**Upgrade to paid**](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZibG9nLmJ5dGVieXRlZ28uY29tJTJGcCUyRmEtZGVlcC1kaXZlLWludG8tYW1hem9uLWR5bmFtb2RiJnI9MThlcGE3JnRva2VuPWV5SjFjMlZ5WDJsa0lqbzNORFU0T1RBMU5Td2lhV0YwSWpveE56RXdNalU0TkRFM0xDSmxlSEFpT2pFM01USTROVEEwTVRjc0ltbHpjeUk2SW5CMVlpMDRNVGN4TXpJaUxDSnpkV0lpT2lKamFHVmphMjkxZENKOS5fZ1UzSmNMU0N1RVVKdkN1Wld4S0UxaXpHbjFDT1E5REhSMnpEUkxVaVQ0IiwicCI6MTQyNTMwNDU0LCJzIjo4MTcxMzIsImYiOnRydWUsInUiOjc0NTg5MDU1LCJpYXQiOjE3MTAyNTg0MTcsImV4cCI6MTcxMjg1MDQxNywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.ssUyhfqe0g8-OvRM0sAulP9mIOxTHol1ne2hNsHEbNQ?&utm_medium=email&utm_source=subscribe-widget&utm_content=142530454)

---

## **Architecture of DynamoDB**

Now that we’ve looked at the operational requirements of DynamoDB, time to learn more about the architecture that helps fulfill these requirements.

To simplify the understanding, we will look at specific parts of the overall architecture one by one.

### **DynamoDB Tables**

A DynamoDB table is a collection of items where each item is a collection of attributes.

[](https://ci3.googleusercontent.com/meips/ADKq_NYHjnAKjnZsFfGcj9NclccGdngO-31mRXigjnuz8f-TTCJ8lP2qGykq_HYB8mKv2KTMXzvz5QUTJpw5d7LeVgkmnNWF9DdGS2vEW0l8iwhpddTUlOFj6HgE8tkmka_6bdrL8U-BF2bctw5qU-rCXUjhebrAFyObdZU0o4k2ielBh22heIaQWG8VJdEw0w9kclySmSOc94NTYsMn7TOCbdLCpqC6ALJmJkKSe2Bv-K32ssDU_h3DNpademMje0KRBIfZruvh3kiv7lOmuQwpJWDD4RQnzitCzSzSI5tIBrOxzBNdFECTJCDKQY8=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1376,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c81e173-0796-4f00-9688-9d8278bcbe84_1600x1081.png)

Each item is uniquely identified by a primary key and the schema of this key is specified at the time of table creation. The primary key’s schema contains a partition key or it can be a composite key (consisting of a partition and sort key).

The partition key is important as it helps determine where the item will be physically stored. We will look at how that works out in a later section.

DynamoDB also supports secondary indexes to query data in a table using an alternate key. A particular table can have one or more secondary indexes.

### **Interface**

DynamoDB provides a simple interface to store or retrieve items from a table.

The below table shows the primary operations that can be used by clients to read and write items in a DynamoDB table.

[](https://ci3.googleusercontent.com/meips/ADKq_NZXDe0tWCRzTBZBzUXmUoCLB2IyvO87Ur8B-KsDjRFsIA5iYnsnIk48snAaH9y4SIk9c_qebDk7kC24SEDY9BgD1CAZgg4l5X6WT_jaXR7nacsF-yj58vVTND3GSAEbUV5myUy7Ngi8F3FVK1TSTdT9AW9WFrRPLt5lBWV5bVddZJ5sMw0UCjkU8v8Y3NKG-Mrc2olO05-H2kyqVF1d9QBbSCfVqVA_JTI7QwrNOcNoVmYCnrWRObYqyf2c51_DgBbPki2hlhcHd3LdnURKKgYXaMalMrSySzW3aRkQRLStIrs0k7uTi6uz3L8=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0eaa1f36-cdc8-4023-a844-b6a0884a1c97_1600x1098.png)

Also, DynamoDB supports ACID transactions that can update multiple items while ensuring atomicity, consistency, isolation, and durability. The key point to note is that this is managed without compromising on the other operational guarantees related to scaling and availability.

### **Partitioning and Replication**

A DynamoDB table is divided into multiple partitions. This provides two benefits:

- Handling more throughput as requests increase
- Store more data as the table grows

Each partition of the table hosts a part of the table’s key range. For example, if there are 100 keys and 5 partitions, each partition can hold 20 keys.

But what about the availability guarantees of these partitions?

Each partition has multiple replicas distributed across availability zones. Together, these replicas form a replication group and improve the partition’s availability and durability.

A replication group consists of storage replicas that contain both the write-ahead logs and the B-tree that stores the key value data. Also, a group can contain replicas that only store write-ahead log entries and not the key-value data. These replicas are known as log replicas. We will learn more about their usage in a later section.

[](https://ci3.googleusercontent.com/meips/ADKq_NYLXIqID9HwCAwc4cu5KVzHwJG4XGhp_UiEKqreRF7T0EXOv3bw-LZRJ-2AtsGni3-y_6s5MCIqc069yW56_NvbmjombZdTQMARzFABYGeNgt66_OnTe9WGiicDVY2_-5n2k_hVMB7PIEROw7vshKWRmttGus_LcUgubZZwzIrTOC3rAd-ftz339Fa6JLyIZT-nuGEtC36_EULgjfrkoYJo2CPGpiGlSV4D0zeHmrVrk07wFv2ImUDx7XI5uoyZyZqFeQYzAbiqwRS7SQxM5VwiFxBGdYyNU3JJPazbAZasmblQooQK_K35GZI=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1416,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6381a107-676d-4e2b-b5ff-dcdc1f2b13d9_1600x1555.png)

But whenever you replicate data across multiple nodes, guaranteeing a consensus becomes a big issue. What if each partition has a different value for a particular key?

The replication group uses Multi-Paxos for consensus and leader election. The leader is a key player within the replication group:

- The leader serves all write requests. On receiving a write request, the leader of the group generates a write-ahead log record and sends it to the other replicas. A write is acknowledged to the application once a quorum of replicas stores the log record to their local write-ahead logs.
- The leader also serves strongly consistent read requests. On the other hand, any other replica can serve *eventually consistent* reads.

But what happens if the leader goes down?

The leader of a replication group maintains its leadership using a lease mechanism. If the leader of the group fails and this failure is detected by any of the other replicas, the replica can propose a new round of the election to elect itself as the new leader.

### **DynamoDB Request Flow**

DynamoDB consists of tens of microservices. However, there are a few core services that carry out the most critical functionality within the request flow.

The below diagram shows the request flow on a high level.

[](https://ci3.googleusercontent.com/meips/ADKq_NbTsQ5Vd3h0YGMOrrXZDCVWR6BhX9C9MulwI5cqdEIE08goleJZw5UPPsnyTuVXsAAgYc-fft1b0z4gnZDxpfOlLq5Bz7BuOPTLJyYemEEBYyU9tOOFvqpwSty9hcD0gSFa_5MpO5S58awJr-Yekot22YzDr5MSbLbG_x3PMrPL3y0vNsTesBFtuorSSzFalytFWOS6RrrF5EctLYDTdVWeM1CuDsuckMD2DxnAE3kLVccS8SVPcGyJ4rhEZEPcA8KPZfGQgh1aW2Ya54HwhBq-4wN2ujXz12M5kyipLzNYtQXbLbrgmj9iGg=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dd04d59-7ea9-487c-911b-3ccc225e7b9a_1600x944.png)

Let’s understand how it works in a step-by-step manner.

- Requests arrive at the request router service. This service is responsible for routing each request to the appropriate storage node. However, it needs to call other services to make the routing decision.
- The request router first checks whether the request is valid by calling the authentication service. The authentication service is hooked to the AWS IAM and helps determine whether the operation being performed on a given table is authorized.
- Next, the request router fetches the routing information from the metadata service. The metadata service stores routing information about the tables, indexes, and replication groups for keys of a given table or index.
- The request router also checks the global admission control to make sure that the request doesn’t exceed the resource limit for the table.
- Lastly, if everything checks out, the request router calls the storage service to store the data on a fleet of storage nodes. Each storage node hosts many replicas belonging to different partitions.

## **Hot Partitions and Throughput Dilution**

As you may have noticed, partitioning is a key selling point for DynamoDB. It provides a way to dynamically scale both the capacity and performance of tables as the demand changes.

In the initial release, DynamoDB allowed customers to explicitly specify the throughput requirements for a table in terms of read capacity units (RCUs) and write capacity units (WCUs). As the demand from a table changed (based on size and load), it could be split into partitions.

For example, let’s say a partition has a maximum throughput of 1000 WCUs. When a table is created with 3200 WCUs, DynamoDB creates 4 partitions with each partition allocated 800 WCUs. If the table capacity was increased to 6000 WCUs, then partitions will be split to create 8 child partitions with 750 WCUs per partition.

All of this was controlled by the admission control system to make sure that storage nodes don’t become overloaded. However, this approach assumed a uniform distribution of throughput across all partitions, resulting in some problems.

Two consequences because of this approach were hot partitions and throughput dilation.

- Hot partitions arose in applications that had non-uniform access patterns. In other words, more traffic consistently went to a few items on the tables rather than an even distribution.
- Throughput dilution was common for tables where partitions were split for size. Splitting a partition for size would result in the throughput of the partition being equally divided among the child partitions. This would decrease the per-partition throughput.

The static allocation of throughput at a partition level can cause reads and writes to be rejected if that partition receives a high number of requests. The partition’s throughput limit was exceeded even though the total provisioned throughput of the table was sufficient. Such a condition is known as throttling.

The below illustration shows this concept:

[](https://ci3.googleusercontent.com/meips/ADKq_NYCFEi2mhcvhLTVnWpLUxevttHYpWIIhk8upsp9h1gxmhq5Hv7kawXZpN8aEHNke95Nxu8uo-JiYL6yQVksGTM4-EHTTXc34tokrMZmWfgvLv8xHrbprOIvTgIYbjbh2_nEpeEJua_YA0su_q82vva1Zui5Iu1HkMwFHEn4xG68gCAoVDcQpqDGQFIeCoXBXDVYL5AvSB-EFyetf8gcQeKoJ00fJPvJbENtXOwKE7oKQFluPWMe-fYqTbdzN9CBoe42xOZvouWE-OsqTCHmyza14b2C85IjaotGywt7BImmd7XpIvJO0RRua2I=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f43b0c8-cd80-4f6e-b084-11ee6169559b_1600x1101.png)

From a customer’s perspective, throttling creates periods of unavailability even though the service behaved as expected. To solve this, the customer will try to increase the table’s provisioned throughput but not be able to use all that capacity effectively. In other words, tables would be over-provisioned, resulting in a waste of resources.

To solve this, DynamoDB implemented a couple of solutions.

### **Bursting**

While non-uniform access to partitions meant that some partitions exceeded their throughput limit, it also meant that other partitions were not using their allocated throughput. In other words, there was unused capacity being wasted.

Therefore, DynamoDB introduced the concept of bursting at the partition level.

The idea behind bursting was to let applications tap into this unused capacity at a partition level to absorb short-lived spikes for up to 300 seconds. The unused capacity is called the *burst* capacity.

It’s the same as storing money in the bank from your salary each month to buy a new car with all those savings.

The below diagram shows this concept.

[](https://ci3.googleusercontent.com/meips/ADKq_NbXcnj7ULt0zDguElscF5ILj-nkgaZSVeUzsvr9iIEL0AfqR6aHuq6EVb6rv6i_hhHLEd8ohFPEHieP6tJl7Kg0TLNq-VTWuw-DICUVnlq1Mn4Y1_sWg95AHNDxC-xGdXCNPQDTTROH8EyHQ0V0PhDAT8wcRdoEo8MBEWN2fLEvHgXHEof_-Zfug-GlQhbpFTW_PdKUah6waRf87sH80QgK9vnTz4qgodcs7tiJP0cS4auAGi4B9WlKkxmD9oIzNHrA2ATzygE556gm0YHusFWukBhiincyGANeV69vWy6J1DvZYdX0cWYuFko=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1448,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe535fbe-f880-4b2e-920d-ab802b1de874_1600x1098.png)

The capacity management was controlled using multiple token buckets as follows:

- Allocated token bucket for a partition
- Burst token bucket for a partition
- Node-level token bucket

Together, these buckets provided admission control:

- If a read request arrived on a storage node and there were tokens in the partition’s allocated bucket, the request was admitted and the tokens were deducted from the partition bucket and node-level bucket
- Once a partition exhausted all provisioned tokens, requests were allowed to burst only when tokens were available both in the burst token and the node-level token bucket

### **Global Admission Control**

Bursting took care of short-lived spikes. However, long-lived spikes were still a problem in cases that had heavily skewed access patterns across partitions.

Initially, the DynamoDB developers implemented an adaptive capacity system that monitored the provisioned and consumed capacity of all tables. In case of throttling where the table level throughput wasn’t exceeded, it would automatically boost the allocated throughput.

However, this was a reactive approach and kicked in only after the customer had experienced a brief period of unavailability.

To solve this problem, they implemented Global Admission Control or GAC.

Here’s how GAC works:

- It builds on the idea of token buckets by implementing a service that centrally tracks the total consumption of a table’s capacity using tokens.
- Each request router instance maintains a local token bucket to make admission decisions.
- The routers also communicate with the GAC to replenish tokens at regular intervals.
- When a request arrives, the request router deducts tokens.
- When it runs out of tokens, it asks for more tokens from the GAC.
- The GAC instance uses the information provided by the client to estimate global token consumptions and provides the tokens available for the next time unit to the client’s share of overall tokens.

## **Managing Durability with DynamoDB**

One of the central tenets of DynamoDB is that the data should never be lost after it has been committed. However, in practice, data loss can happen due to hardware failures or software bugs.

To guard against these scenarios, DynamoDB implements several mechanisms to ensure high durability.

### **Hardware Failures**

In a large service like DynamoDB, hardware failures such as memory and disk failures are common. When a node goes down, all partitions hosted on that node are down to just two replicas.

The write-ahead logs in DynamoDB are critical for providing durability and crash recovery.

Write-ahead logs are stored in all three replicas of a partition. To achieve even higher levels of durability, the write-ahead logs are also periodically archived to S3 which is designed for 11 nines of durability.

### **Silent Data Errors and Continuous Verification**

Some hardware failures due to storage media, CPU, or memory can cause incorrect data to be stored. Unfortunately, these issues are difficult to detect and they can happen anywhere.

DynamoDB extensively maintains checksums within every log entry, message, and log file to detect such data. Data integrity is validated for every data transfer between two nodes.

DynamoDB also continuously verifies data at rest using a scrub process. The goal of this scrub process is to detect errors such as bit rot.

The process verifies two things:

- All three copies of the replicas in the replication group have the same data
- Data of the live replicas matches with a copy of a replica built offline using the archived write-ahead log entries

The verification is done by computing the checksum of the live replica and matching that with a snapshot of one generated from the log entries archived in S3.

### **Backups and Restores**

A customer’s data can also get corrupted due to a bug in their application code.

To deal with such scenarios, DynamoDB supports backup and restore functionalities. The great part is that backups and restores don’t affect the performance or availability of the table since they are built using the write-ahead logs that are archived in S3.

Backups are full copies of DynamoDB tables and are stored in an S3 bucket. They are consistent across multiple partitions up to the nearest second and can be restored to a new table anytime.

DynamoDB also supports point-in-time restore allowing customers to restore the contents of a table that existed at any time in the previous 35 days.

## **Managing Availability with DynamoDB**

Availability is a major selling point of a managed database service like DynamoDB.

Customers expect almost 100% availability and even though it may not be theoretically possible, DynamoDB employs several techniques to ensure high availability.

DynamoDB tables are distributed and replicated across multiple Availability Zones (AZs) within a region. The platform team regularly tests resilience to node, rack, and AZ failures.

However, they also had to solve several challenges to bring DynamoDB to such a high level of availability

### **Write and Read Availability**

The write availability of a partition depends on a healthy leader and a healthy write quorum that consists of two out of three replicas from different AZs.

In other words, a partition becomes unavailable for writes if the number of replicas needed to achieve the minimum quorum requirements is unavailable. If one of the replicas goes down, the leader adds a log replica in the group since it is the fastest way to ensure that the write quorum is always available.

As mentioned earlier, the leader replica serves consistent reads while other replicas can serve *eventually consistent* reads.

### **Failure Detection**

The availability of a database is highly dependent on the ability to detect failures.

Failure detection must be quick to minimize downtime. Also, it should be able to detect false positives because triggering a needless failover can lead to bigger disruptions in the service.

For example, when all replicas lose connection to the leader, it’s clear that the leader is down and a new election is needed.

However, nodes can also experience gray failures due to communication issues between a leader and followers. For instance, a replica doesn’t receive heartbeats from a leader due to some network issue and triggers a new election. However, a newly elected leader has to wait for the expiry of the old leader’s lease resulting in unavailability.

To get around gray failures like this, a replica that wants to trigger a failover confirms with the other replicas whether they are also unable to communicate with the leader. If the other replicas respond with a healthy leader message, the follower drops its leader election attempt.

### **Metadata Availability**

As we saw in the DynamoDB’s request flow diagram, metadata is a critical piece that makes the entire process work.

Metadata is the mapping between a table’s primary keys and the corresponding storage nodes. Without this information, the requests cannot be routed to the correct nodes.

In the initial days, DynamoDB stored the metadata in DynamoDB itself. When the request router received a request for a table it had not seen before, it downloaded the routing information for the entire table and cached it locally for subsequent requests. Since this information didn’t change frequently, the cache hit rate was almost 99.75 percent.

However, bringing up new router instances with empty caches would result in a huge traffic spike to the metadata service, impacting performance and stability.

To reduce the reliance on local caching of the metadata, DynamoDB built an in-memory distributed datastore called MemDS.

See the below diagram for the role of MemDS.

[](https://ci3.googleusercontent.com/meips/ADKq_NYk5Cx8uTB0oG_LrDNdTVqyugEXn7oI4FMtXX9ie9cJIbSsWPiJgjsHS20HeGBHHGO5nK_RmE9ClcmPEe5VdIm8K01gEec6FXzP9fiWGla8mDLdOINaZui3Fc7wv5VR3Ob_JZBq3LeHg2I9R8BfpR8Bt3hz7EJjQ3dE7Nk39hrVBT4hBBwEUv1zDKvDS7gL9a_DDn-mWtH3YaMa8vL9lpyuQhRqLJBoKuIn-UqfOfBmwE6FGuzMBRISTHtmZY0wnpce5Om6EFJGECYqZpih5O4UQbuxGcYB0vUGb_Wy6_pDOlnIPY8fKRh5SQ=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2559302-f9cd-46a4-8681-fb09dfe71cb0_1600x946.png)

As you can see, MemDS stores all the metadata in memory and replicates it across the fleet of MemDB servers.

Also, a partition map cache (MemDS cache) was deployed on each request router instance to avoid a bi-modal cache setup. Whenever there is a cache hit, an asynchronous call is made to MemDS to refresh the cache, ensuring that there is a constant flow of traffic to the MemDS fleet rather than traffic spikes.

## **Conclusion**

DynamoDB has been a pioneer in the field of NoSQL databases in the cloud-native world.

Thousands of companies all across the world rely on DynamoDB for their data storage needs due to its high availability and scalability properties.

However, behind the scenes, DynamoDB also packs a lot of learnings in terms of designing large-scale database systems.

Some of the key lessons the DynamoDB team had were as follows:

- Adapting to the traffic patterns of user applications improves the overall customer experience
- To improve stability, it’s better to design systems for predictability over absolute efficiency
- For high durability, perform continuous verification of the data-at-rest
- Maintaining high availability is a careful balance between operational discipline and new features

These lessons can act as great takeaways for us.
