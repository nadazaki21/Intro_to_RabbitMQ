Project: Distributed Task Processing System
Project Overview

You'll build a distributed task processing system where different types of tasks are sent to a RabbitMQ exchange and routed to different workers (consumers) based on the task type.


 The system will include the following components:

1- Task Producer: A service that generates tasks of different types (e.g., image processing, data analysis, file conversion) and sends them to RabbitMQ.

2- Task Processor Workers: Multiple workers that consume tasks from the queue. Each worker processes a specific type of task.

Key Concepts to Implement:

a. Work Queues: Distribute tasks among multiple workers to balance the load.

b. Routing: Use direct or topic exchanges to route tasks to the appropriate worker based on task type.

c. Persistence: Ensure that tasks are not lost by making queues durable and messages persistent.
Acknowledgments: Use acknowledgments to ensure that tasks are only marked as complete when a worker has successfully processed them.

d. RPC: Implement an RPC mechanism to allow the task producer to request the status of a task and get the result back once it’s processed.

