Postmortem: Outage of Web Application Authentication Service
Duration: The outage was for 3 and the half hours on the 31st of July, 2024, 9:15 AM to 11:30 PM WAT.

Impact: The authentication service of our web application was down, preventing 45% of users from logging in. Those already logged in experienced slow response times when accessing account-related features. The impact was particularly severe in the U.S. East Coast region.

Root Cause: A misconfiguration in the load balancer’s health check parameters caused the primary authentication server to be marked as unhealthy, leading to traffic being routed to an under-resourced backup server, which then became overwhelmed.

Timeline
9:15 AM: Monitoring system triggered an alert for increased login failures and slow response times.
9:20 AM: Support team noticed multiple complaints from users on social media about login issues.
9:25 AM: Incident escalated to the engineering team for investigation
9:30 AM: Initial assumption was a database issue due to the authentication service's dependency on user data storage.
9:45 AM: Database logs reviewed; no anomalies found. Issue suspected to be with the authentication microservice
10:00 AM: Load balancer settings reviewed, leading to the discovery of the primary server being marked as unhealthy.
10:15 AM: Health check parameters for the load balancer were identified as the probable cause, but further checks on network connectivity were performed to rule out other issues.
10:45 AM: Health check parameters for the load balancer were identified as the probable cause, but further checks on network connectivity were performed to rule out other issues.
11:00 PM: Authentication service manually restarted, and traffic rerouted to the primary server after adjusting the health check parameters.
11:15 PM: Service stability confirmed with login success rates returning to normal.
11:30 PM: Service stability confirmed with login success rates returning to normal.

Root Cause and Resolution

Root Cause: The load balancer was configured with overly strict health check parameters that caused the primary authentication server to be marked as unhealthy due to a transient spike in response time. As a result, traffic was rerouted to a backup server that was not sufficiently resourced to handle the increased load. The backup server became overwhelmed, causing login failures and slow response times for a significant portion of users.

Resolution: The health check parameters were adjusted to be less sensitive to transient spikes. The backup server was also scaled up to better handle potential future traffic increases. After making these changes, the primary server was brought back online, and traffic was rerouted to it. Monitoring was intensified to ensure the stability of the service post-resolution.

Corrective and Preventive Measures

Improvements and Fixes:

Load Balancer Configuration: Review and adjust health check parameters to prevent premature failover in the future.
Backup Server Resources: Scale backup server resources to handle unexpected traffic spikes without performance degradation.
Monitoring: Enhance monitoring to include more granular alerts on load balancer health check failures and server resource utilization.
Incident Response: Improve incident response protocols to quickly rule out potential issues with dependent services (e.g., database) and focus on primary suspects.

Task
These are task taken so solve the problem.
I reviewed and updated load balancer health check settings across all environments.
Then Increased resource allocation for backup authentication servers.
After which I Implemented additional monitoring on load balancer health check failures.
Then conducted a training session for the support and engineering teams on identifying and resolving load balancer-related issues.
And finally performed a post-incident review meeting to discuss lessons learned and further improvement opportunities.






The load balancer is depicted as a circus performer, juggling servers with one slipping out of control, causing chaos as the backup server struggles to keep up. The playful illustration highlights the incident's challenges while adding a light-hearted touch to the technical explanation.

