---
type: Explanation
title: API Gateway
description: Step 1 - The client sends an HTTP request to the API gateway.
tags: ["API", "Architecture"]
timestamp: 2025-02-28T08:58:00Z
---

![5073760f-5d61-4ce2-8469-bf21cc640e09_1280x1664.webp](Explanation%20API%20Gateway/5073760f-5d61-4ce2-8469-bf21cc640e09_1280x1664.webp)

Step 1 - The client sends an HTTP request to the API gateway.

Step 2 - The API gateway parses and validates the attributes in the HTTP request.

Step 3 - The API gateway performs allow-list/deny-list checks.

Step 4 - The API gateway talks to an identity provider for authentication and authorization.

Step 5 - The rate limiting rules are applied to the request. If it is over the limit, the request is rejected.

Steps 6 and 7 - Now that the request has passed basic checks, the API gateway finds the relevant service to route to by path matching.

Step 8 - The API gateway transforms the request into the appropriate protocol and sends it to backend microservices.

Steps 9-12: The API gateway can handle errors properly, and deals with faults if the error takes a longer time to recover (circuit break). It can also leverage ELK (Elastic-Logstash-Kibana) stack for logging and monitoring. We sometimes cache data in the API gateway.
