Project: Distributed Task Processing System
Project Overview
You'll build a distributed task processing system where different types of tasks are sent to a RabbitMQ exchange and routed to different workers (consumers) based on the task type. The system will include the following components:
Task Producer: A service that generates tasks of different types (e.g., image processing, data analysis, file conversion) and sends them to RabbitMQ.
Task Processor Workers: Multiple workers that consume tasks from the queue. Each worker processes a specific type of task.
Task Status Monitoring: A monitoring system that keeps track of the status of each task and reports completion.
Key Concepts to Implement
Work Queues: Distribute tasks among multiple workers to balance the load.
Routing: Use direct or topic exchanges to route tasks to the appropriate worker based on task type.
Persistence: Ensure that tasks are not lost by making queues durable and messages persistent.
Acknowledgments: Use acknowledgments to ensure that tasks are only marked as complete when a worker has successfully processed them.
RPC: Implement an RPC mechanism to allow the task producer to request the status of a task and get the result back once it’s processed.
Monitoring: Create a simple monitoring dashboard that tracks the status of tasks and displays statistics like how many tasks are in the queue, how many are being processed, and how many have been completed.
Steps to Implement
Setup RabbitMQ and Basic Components:
Set up RabbitMQ on your local machine or use a cloud-hosted RabbitMQ instance.
Create a basic producer that sends tasks to a RabbitMQ exchange.
Implement basic workers that consume tasks from the queue.
Implement Task Routing:
Use direct or topic exchanges to route different types of tasks to different queues.
Make sure each worker subscribes to the appropriate queue for the task type it can process.
Handle Persistence and Durability:
Mark queues as durable and messages as persistent to ensure that tasks aren’t lost if RabbitMQ restarts.
Implement Acknowledgments:
Ensure that workers send acknowledgments after successfully processing a task to prevent message loss or duplication.
Add RPC for Task Status:
Implement an RPC mechanism so the task producer can query the status of tasks and retrieve results once processing is complete.
Create a Monitoring Dashboard:
Use a simple web framework (like Flask) to create a dashboard that visualizes the status of tasks in real-time.
Extensions
Scaling: Deploy the system across multiple servers to handle a higher volume of tasks.
Fault Tolerance: Implement retry mechanisms for failed tasks and ensure that the system can recover from worker crashes.
Advanced Routing: Implement more complex routing logic using topic exchanges to handle a variety of task types.
This project will give you hands-on experience with RabbitMQ’s capabilities and help you deepen your understanding of how to build scalable, reliable distributed systems.

