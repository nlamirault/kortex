---
title: SLI/SLO/SLA
type: concept
status: active
confidence: high
cluster: platform
domain: [platform]
sources: []
updated: 2025-02-28
tags: [Reliability]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
Google SRE Book: [https://sre.google/sre-book/service-level-objectives/](https://sre.google/sre-book/service-level-objectives/)

# Definitions

![](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2024/06/11/SLAs.jpg)

# **Service Level Indicators (SLIs)**

SLIs are the metrics employed to assess the quality of our service as perceived by our users. Accurately identifying and measuring SLIs is fundamental to setting meaningful SLOs and ultimately ensuring customer satisfaction.

For example, an SLI could be the time taken to process a request (latency) or the frequency of errors in a service (error rate).

# **Service Level Objectives (SLOs)**

SLOs are the targets that we set for our SLIs. They define the level of service we aim to provide in order to make our users happy. In essence, they represent the goals that our service aspires to achieve in terms of performance and reliability.

For example, an SLO could be that “99.99% of requests to a service should be processed in less than 300ms”.

# **Service Level Agreements (SLAs)**

SLAs are formalized agreements between the service provider and the user. They outline the expected level of service, including the SLOs, and often come with penalties for the service provider, if the SLOs are not met.

It is important to note that SLAs are legally binding agreements, and failing to meet the agreed-upon levels of service, can have financial or other contractual repercussions.

SLAs can be the same as SLOs, or more relaxed. For example, an SLA could be that “99.9% of requests to a service should be processed in less than 300ms”.

# **Error Budget**

The error budget represents the amount of acceptable downtime of errors for a service over a specific period, calculated based on the SLO.

As the service operates, any downtime or errors will consume the error budget. If the service operates perfectly, the error budget will remain intact.

Once the error budget is depleted, it indicates that the service is not meeting its agreed-upon objectives (meaning the SLO has been breached).

# **Burn Rate**

The burn rate is the rate at which the error budget is being consumed.

If the error budget is consumed too quickly (e.g., half of the monthly error budget is consumed in a day), this indicates that the service is not operating as expected and corrective actions may be needed.

This is especially useful for operations because you can build alerting on top of it. For more details on how to build alerting on burn rates, refer to this [Google SRE workbook](https://sre.google/workbook/alerting-on-slos/).

# **Rolling Windows**

SLOs are usually associated to a rolling window, which is a continuously moving time window. For example, if we have a rolling window of 30 days, then at any given point, we are calculating the Availability and Error Budget based on the data from the past 30 days.
