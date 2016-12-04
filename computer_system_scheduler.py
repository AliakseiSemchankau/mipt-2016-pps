
class SubTaskOrder(object):
	def __init__(self, order_id, sub_task, cluster_id):
		self.order_id = order_id
		self.sub_task = sub_task
		self.cluster_id = cluster_id
}

class ComputingSystemMsg(object):
	def __init__(self, clusters):
		self.clusters = clusters
}

class ClusterMsg(object):
	def __init__(self, processors):
		self.processors = processors
}

class ProcessorMsg(object):
	def __init__(self, power, reserved_time):
		self.power = power
		self.reserved_time = reserved_time
}
