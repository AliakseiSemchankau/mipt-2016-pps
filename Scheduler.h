/**
 * @(#) Scheduler.h
 */

#ifndef SCHEDULER_H_H
#define SCHEDULER_H_H

#include "ALGO.h"
#include "Task queue.h"
#include "Cluster.h"
class Scheduler
{
	void sendSubTaskToCluster( );
	ALGO * algo_what;
	
	Cluster * clusters;
	
	Task_queue * task_queues;
	
	
};

#endif
