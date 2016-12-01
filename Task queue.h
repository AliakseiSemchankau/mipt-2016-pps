/**
 * @(#) Task queue.h
 */

#ifndef TASK QUEUE_H_H
#define TASK QUEUE_H_H

#include "User.h"
#include "Task.h"
class Task_queue
{
	
public:
	void pop( );
	int result;
	
	int status;
	
	
private:
	void Define Priority( );
	int Interaction;
	
	int SaveSubTask;
	
	int SaveTask;
	
	Task * tasks;
	
	User * users;
	
	User * users1;
	
	
};

#endif
