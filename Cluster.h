/**
 * @(#) Cluster.h
 */

#ifndef CLUSTER_H_H
#define CLUSTER_H_H

#include "Sub queue.h"
#include "Processor.h"
class Cluster
{
	void putSubTaskInSubQueue( );
	void sendSubTask( );
	Processor * processors;
	
	Sub_queue * sub_queues;
	
	
};

#endif
