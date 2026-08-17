---
title: Grafana
type: project
status: active
confidence: high
cluster: observability
domain: [observability]
sources: []
updated: 2025-02-28
tags: [Observability]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# Description

Grafana is an open-source platform for monitoring and observability that allows you to query, visualize, alert on, and understand your metrics no matter where they are stored. It provides tools to turn your time-series database (TSDB) data into beautiful graphs and visualizations.

.png)

Grafana's architecture is modular and includes the following components:

- **Frontend**: Grafana's user interface is built using HTML, JavaScript, and CSS. It's a single-page application (SPA) that communicates with the backend via a REST API. The frontend provides the dashboard interface through which users can create and view visualizations.
- **Backend**: The backend is written in Go and serves the Grafana web application, handles API requests, and performs authentication and authorization checks. It is responsible for querying data sources and returning the results to the frontend for visualization.
- **Data Sources**: Grafana supports a variety of data sources, including Prometheus, Graphite, InfluxDB, Elasticsearch, MySQL, PostgreSQL, and many others. Each data source has a dedicated backend plugin that understands how to query the database and parse the response.
- **Plugins**: Grafana has a robust plugin system that allows developers to extend its functionality. There are three main types of plugins:
    - **Data Source Plugins**: Add support for new databases or APIs.
    - **Panel Plugins**: Provide new visualization options beyond the built-in graph, table, and single-stat panels.
    - **App Plugins**: Bundle data sources and panels to provide features like custom pages or direct integration with other tools or systems.
- **Database**: Grafana uses an SQL database to store user data, dashboard definitions, and other persistent data. By default, Grafana uses SQLite, but it also supports MySQL and PostgreSQL.
- **Alerting Engine**: Grafana has a built-in alerting engine that evaluates defined alert rules against the data and sends notifications when conditions are met. The alerting engine supports multiple notification channels, including email, Slack, and webhooks.
- **API**: Grafana provides a comprehensive HTTP API for interacting with the backend programmatically. The API can be used for tasks such as querying for data, creating or updating dashboards, managing users, and configuring data sources.
- **Authentication**: Grafana supports various authentication methods, including built-in user accounts, LDAP, OAuth, and proxy authentication.
- **HTTP Server**: Grafana includes its own HTTP server to serve the application and handle API requests. It can also be placed behind a reverse proxy for additional security or scalability.
