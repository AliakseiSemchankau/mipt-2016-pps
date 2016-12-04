
class Order(Object):
	def __init__(self, task, resource, order_id):
		self.task = task
		self.resource = resource
		self.order_id = order_id
}

class Task(Object):
	# list of subtasks
	def __init__(self, sub_tasks):
		self.sub_tasks = sub_tasks
}

class SubTask(Object):
	def __init__(self, url):
		self.url = url

class Resourse(Object):
	def __init__(self, processors_count, time_durability):
		self.processors_count = processors_count
		self.time_durability = time_durability
}

class StatusMsg(Object):

	DONE = 0
	UNDONE = 1
	FAILED = 2

	def __init__(self, status, result)
		self.status = status
		self.result = result
}

